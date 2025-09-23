from django.db import migrations

def seed_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')
    
    # Only seed if no pets exist
    if Pet.objects.count() == 0:
        pets_data = [
            {'img': 'images/Golden-Retriever.png', 'name': 'Charlie', 'age': 3, 'breed': 'Golden Retriever', 'species': 'Dog'},
            {'img': 'images/Beagle.png', 'name': 'Max', 'age': 2, 'breed': 'Beagle', 'species': 'Dog'},
            {'img': 'images/Bulldogg.png', 'name': 'Rocky', 'age': 5, 'breed': 'Bulldog', 'species': 'Dog'},
            {'img': 'images/Husky.png', 'name': 'Ghost', 'age': 4, 'breed': 'Siberian Husky', 'species': 'Dog'},
            {'img': 'images/Tabby.png', 'name': 'Luna', 'age': 1, 'breed': 'Tabby', 'species': 'Cat'},
            {'img': 'images/Siamese.png', 'name': 'Simba', 'age': 3, 'breed': 'Siamese', 'species': 'Cat'},
            {'img': 'images/Persian.png', 'name': 'Nala', 'age': 4, 'breed': 'Persian', 'species': 'Cat'},
            {'img': 'images/Bengal.png', 'name': 'Tiger', 'age': 2, 'breed': 'Bengal', 'species': 'Cat'},
            {'img': 'images/Lop.png', 'name': 'Hazel', 'age': 1, 'breed': 'Lop', 'species': 'Rabbit'},
            {'img': 'images/Rex.png', 'name': 'Cinnamon', 'age': 2, 'breed': 'Rex', 'species': 'Rabbit'},
            {'img': 'images/Angora.png', 'name': 'Snowflake', 'age': 2, 'breed': 'Angora', 'species': 'Rabbit'},
            {'img': 'images/Macaw.png', 'name': 'Skye', 'age': 2, 'breed': 'Macaw', 'species': 'Bird'},
            {'img': 'images/Cockatiel.png', 'name': 'Sunny', 'age': 1, 'breed': 'Cockatiel', 'species': 'Bird'},
            {'img': 'images/Parakeet.png', 'name': 'Kiwi', 'age': 2, 'breed': 'Parakeet', 'species': 'Bird'},
            {'img': 'images/LeopardGecko.png', 'name': 'Leo', 'age': 1, 'breed': 'Leopard Gecko', 'species': 'Reptile'},
            {'img': 'images/BeardedDragon.png', 'name': 'Spike', 'age': 3, 'breed': 'Bearded Dragon', 'species': 'Reptile'},
            {'img': 'images/CornSnake.png', 'name': 'Slyther', 'age': 2, 'breed': 'Corn Snake', 'species': 'Reptile'},
            {'img': 'images/BoxTurtle.png', 'name': 'Shelly', 'age': 4, 'breed': 'Box Turtle', 'species': 'Reptile'},
            {'img': 'images/VeiledChameleon.png', 'name': 'Echo', 'age': 2, 'breed': 'Veiled Chameleon', 'species': 'Reptile'},
        ]
        
        for pet_data in pets_data:
            Pet.objects.create(**pet_data)


def reverse_seed_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')
    Pet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(seed_pets, reverse_seed_pets),
    ]
