import requests
import json

# URL for the DALL-E 2 API
url = "https://api.openai.com/v1/images/generations"

# Your API key for OpenAI
api_key = "[API KEY HERE]"

# Prompt to generate an image
prompt = "Man in pig suit playing the drums"

# Parameters for the API request
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "1024x1024",
    "response_format": "url",
}

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {api_key}",
}

# Send the API request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Extract the URL of the generated image from the response
result = json.loads(response.content)
image_url = result["data"][0]["url"]

# Print the URL of the generated image
print(image_url)
