from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from school.models import *

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")
        message = request.POST.get("message")

        if not email:  # Ensure email is provided
            return HttpResponse("Email is required.", status=400)

        # Save to database
        contact = ContactUs.objects.create(
            name=name, email=email, phone=phone, message=message
        )

        # Send confirmation email to user
        send_mail(
            subject="Thank You for Contacting Us",
            message=f"Hello {name},\n\nWe have received your message:\n\n{message}\n\nWe will get back to you soon!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Send to the user who submitted the form
        )

        # Optional: Notify admin about the new contact
        send_mail(
            subject="New Contact Us Submission",
            message=f"New message from {name} ({email}):\n\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # Admin's email
        )

        return HttpResponse("Message sent successfully!")
    
    return render(request, "contact_form.html")  # Render the contact form page
