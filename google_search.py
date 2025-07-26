import requests

def google_search(query):
    API_KEY = "b4c167976d5f816385dedb0048ffe6d65f4fdbe77835a508f45857f8ce3c10eb"
    params = {
        "q": query,
        "api_key": API_KEY,
        "engine": "google"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    try:
        return data["answer_box"]["snippet"]
    except KeyError:
        try:
            return data["organic_results"][0]["snippet"]
        except (KeyError, IndexError):
            return "Sorry, I couldn't find an answer."
