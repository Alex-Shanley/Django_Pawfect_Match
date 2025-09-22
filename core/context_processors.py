import requests


def dog_facts(request):
    """Context processor to inject dog facts into all templates"""
    def get_dog_facts(limit=3):
        try:
            response = requests.get(f"https://dogapi.dog/api/v2/facts?limit={limit}")
            if response.status_code == 200:
                data = response.json()
                return [item['attributes']['body'] for item in data.get('data', [])]
        except Exception as e:
            print("Error fetching dog facts:", e)
        # Fallback facts if API fails
        return [
            "All my dogs were named Charlie",
            "Dogs can learn over 1000 words",
            "They dream just like humans!"
        ]
    
    return {'dog_facts': get_dog_facts()}