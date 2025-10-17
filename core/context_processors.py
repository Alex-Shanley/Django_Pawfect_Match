import requests
from django.core.cache import cache

def dog_facts(request):
    cached_facts = cache.get('dog_facts')
    if cached_facts:
        return {'dog_facts': cached_facts}

    def get_dog_facts(limit=3):
        try:
            response = requests.get(f"https://dogapi.dog/api/v2/facts?limit={limit}", timeout=2)
            if response.status_code == 200:
                data = response.json()
                return [item['attributes']['body'] for item in data.get('data', [])]
        except Exception as e:
            print("Error fetching dog facts:", e)
        return [
            "All my dogs were named Charlie",
            "Dogs can learn over 1000 words",
            "They dream just like humans!"
        ]

    facts = get_dog_facts()
    cache.set('dog_facts', facts, 60*60)  
    return {'dog_facts': facts}
