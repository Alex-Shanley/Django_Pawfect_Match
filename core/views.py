from django.shortcuts import render
from django.contrib import messages
from contact.forms import ContactForm


# Create your views here.


def index(request):
   
    steps = [
        {
            "title": " Find your pet",
            "description": "Browse loving pets waiting for their forever home. Use our simple search to meet your perfect match and start your adoption journey today."
        },
        {
            "title": " Reach out to us",
            "description": "Got questions or ready to take the next step? Our friendly team is here to help with anything you need just a message or call away."
        },
        {
            "title": " Have A Meeting",
            "description": "Schedule a meet-and-greet to get to know your future furry friend. It's the perfect way to see if it's a match made in pawradise."
        }
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!!')
            return render(request, 'index.html', {'steps': steps, 'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'index.html', {'steps': steps, 'form': form})


def about(request):
    """About page"""
    sections = [
        {
            'image': "images/woman.png",
            'alt': 'woman and dog',
            'title': 'Our Mission',
            'paragraphs': [
                'At Pawfect, our mission is to ensure that every pet finds a loving and forever home.',
                'We believe in creating meaningful connections between caring people and animals in need, making the adoption process simple, safe, and joyful for everyone involved.'
            ],
            'reverse': False
        },
        {
            'image': "images/bulldog.png",
            'alt': 'woman and dog',
            'title': 'What We Do',
            'paragraphs': [
                'We provide a trusted platform where adopters can explore detailed profiles of pets looking for new families.',
                'Beyond just matching pets and people, we offer guidance, resources, and support throughout the entire adoption journey to help create lasting bonds.'
            ],
            'reverse': True
        },
        {
            'image': "images/man.png",
            'alt': 'woman and dog',
            'title': 'Our Promise',
            'paragraphs': [
                'We are committed to transparency, compassion, and the well-being of every animal in our care.',
                'Whether you\'re adopting, volunteering, or simply learning more, Pawfect is dedicated to fostering a community where every paw finds the perfect place to call home.'
            ],
            'reverse': False
        },
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!!')
            return render(request, 'about.html', {'sections': sections, 'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'about.html', {'sections': sections, 'form': form})


def faq(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!!')
            return render(request, 'faq.html', {'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'faq.html', {'form': form})


