from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import ContactForm

def handle_contact_form(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect(request.path)
    else:
        form = ContactForm()
    return form

def index(request):
    steps = [
        {"title": "Find your pet", "description": "Browse loving pets waiting for their forever home. Use our simple search to meet your perfect match and start your adoption journey today."},
        {"title": "Reach out to us", "description": "Got questions or ready to take the next step? Our friendly team is here to help with anything you need just a message or call away."},
        {"title": "Have A Meeting", "description": "Schedule a meet-and-greet to get to know your future furry friend. It’s the perfect way to see if it’s a match made in pawradise."},
    ]
    form = handle_contact_form(request)
    return render(request, 'index.html', {'steps': steps, 'form': form})

def about(request):
    sections = [
        {'image': "images/woman.png", 'title': 'Our Mission', 'paragraphs': ['At Pawfect, our mission is to ensure every pet finds a loving home. We believe in creating meaningful connections between caring people and animals in need, making the adoption process simple, safe, and joyful for everyone involved. '], 'reverse': False},
        {'image': "images/bulldog.png", 'title': 'What We Do', 'paragraphs': ['We provide a trusted platform to explore pets looking for new families. Beyond just matching pets and people, we offer guidance, resources, and support throughout the entire adoption journey to help create lasting bonds.'], 'reverse': True},
        {'image': "images/man.png", 'title': 'Our Promise', 'paragraphs': ['We are committed to transparency, compassion, and animal well-being. Whether you’re adopting, volunteering, or simply learning more, Pawfect is dedicated to fostering a community where every paw finds the perfect place to call home.'], 'reverse': False},
    ]
    form = handle_contact_form(request)

    page_title = "About Us"
    
    return render(request, 'about.html', {'sections': sections, 'form': form, 'title': page_title, })

def faq(request):
    form = handle_contact_form(request)
    page_title = "FAQ"
    return render(request, 'faq.html', {'form': form, 'title': page_title,})







