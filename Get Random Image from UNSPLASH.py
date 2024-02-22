import requests
import random


def get_random_image_url(topic, client_id, landscape_or_portrait='landscape'):
    """
    Fetches a random image URL for a given place name from Unsplash with specified orientation.

    Parameters:
    - topic: str. What you want an image of.
    - client_id: str. Your Unsplash Access Key.
    - landscape_or_portrait: str. Desired orientation of the image ('landscape' or 'portrait').

    Returns:
    - str: A URL to an image of the topic if found, else a message indicating no image was found.
    """
    base_url = "https://api.unsplash.com/search/photos"
    query_params = {
        "query": topic,
        "client_id": client_id,
        "orientation": landscape_or_portrait,
        "page": 1,
        "per_page": 10  # Request more images to choose from
    }

    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()

        data = response.json()
        results = data["results"]
        if results:
            random_image = random.choice(results)  # Randomly select one image
            return random_image["urls"]["regular"]
        else:
            return "No image found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


# Example usage
client_id   = "Access Key"  # Replace with your actual Unsplash Access Key
topic       = "spain"
orientation = "landscape"  # Try changing to "portrait" to see different results
# orientation = "portrait"
image_url   = get_random_image_url(topic, client_id, orientation)
print(image_url)
