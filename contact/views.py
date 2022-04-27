from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    View for contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                f'This Mail is from {name}, with email {email}, Contact you about {subject}',
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            messages.success(request, 'Thank you for your Email!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Somethings wrong, Please Try send your Email again')
    else:
        form = ContactForm()

        context = {
            'form': form,
        }
    return render(request, 'contact/contact.html', context)
