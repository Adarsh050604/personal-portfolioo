from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactMessageForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Render email template
            email_content = render_to_string('email/contact_message.html', {
                'name': contact_message.name,
                'email': contact_message.email,
                'message': contact_message.message,
            })
            # Send email notification
            send_mail(
                subject=f"New Contact Message from {contact_message.name}",
                message=email_content,
                from_email='adarshsajeevan050604@gmail.com',
                recipient_list=['adarshsajeevan050604@gmail.com'],
                fail_silently=False,
                html_message=email_content,
            )
            return redirect('contact_success')  # Redirect to a success page or the same page
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')