from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Pet
from .forms import PetForm
from contact.forms import ContactForm



def list_pets(request):
    """List and filter pets"""
    
    name = request.GET.get('name', '').strip()
    age = request.GET.get('age', '').strip()
    breed = request.GET.get('breed', '').strip()
    species = request.GET.get('species', '').strip()

    
    pets = Pet.objects.all()

    
    if name:
        pets = pets.filter(name__icontains=name)
    if age:
        try:
            pets = pets.filter(age=int(age))
        except ValueError:
            messages.error(request, "Age must be a number")
    if breed:
        pets = pets.filter(breed__icontains=breed)
    if species:
        pets = pets.filter(species=species)

    
    species_options = Pet.objects.values_list('species', flat=True).distinct()

  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!!')
            return render(request, 'pets.html', {
                'pets': pets,
                'name': name,
                'age': age,
                'breed': breed,
                'selected_species': species,
                'species_options': species_options,
                'form': ContactForm()
            })
    else:
        form = ContactForm()

        page_title = "Pets"

    return render(request, 'pets.html', {
        'pets': pets,
        'name': name,
        'age': age,
        'breed': breed,
        'selected_species': species,
        'species_options': species_options,
        'form': form,
        'title': page_title
    })


@login_required
def add_pet(request):
    page_title = "Add pet"

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save()
            messages.success(request, f"Pet '{pet.name}' added successfully!")
            return redirect('pets:list_pets')
    else:
        form = PetForm()

    return render(request, 'add.html', {'form': form, 'title': page_title})



@login_required
def edit_pet(request, pet_id):
   
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save()
            messages.success(request, 'Pet updated successfully!')
            return redirect('pets:list_pets')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PetForm(instance=pet)

        page_title = "Edit pet"

    return render(request, 'edit.html', {'form': form, 'pet': pet, 'title': page_title,})


@login_required
def delete_pet(request, pet_id):
   
    pet = get_object_or_404(Pet, id=pet_id)
    pet_name = pet.name
    pet.delete()
    messages.success(request, f"Deleted pet {pet_name} successfully.")
    return redirect('pets:list_pets')




