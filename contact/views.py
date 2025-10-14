from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact(request):
  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!!')
            return redirect('contact:contact')
    else:
        form = ContactForm()

        page_title = "Contact Us"

    return render(request, 'contact.html', {'form': form, 'title': page_title,})
