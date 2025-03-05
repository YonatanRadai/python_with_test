import requests

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to fetch a joke."

if __name__ == "__main__":
    print(fetch_random_joke())
