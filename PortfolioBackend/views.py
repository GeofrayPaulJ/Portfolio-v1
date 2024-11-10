# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from form fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send an email using the user's email address as the sender
            send_mail(
                subject=f"Message from {name} ({email})",
                message=f"Subject: {subject}\n\nMessage:\n{message}\n\nPhone: {phone}",
                from_email=email,  # Set the user's email as the sender
                recipient_list=['geofraypaul1223@gmail.com'],  # Your email as the recipient
                fail_silently=False,
            )

            # Redirect to avoid resubmission on page reload
            return redirect('index')

    return render(request, 'index.html', {'form': form})

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from form fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send an email using the user's email address as the sender
            send_mail(
                subject=f"Message from {name} ({email})",
                message=f"Subject: {subject}\n\nMessage:\n{message}\n\nPhone: {phone}",
                from_email=email,  # Using the sender's email dynamically
                recipient_list=['geofraypaul1223@gmail.com'],  # Your receiving email
                fail_silently=False,
            )


            # Redirect after successful form submission
            return redirect('contact')

    return render(request, 'index.html', {'form': form})
