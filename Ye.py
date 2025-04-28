import requests

# URL
url = "https://api.kanye.rest"


response = requests.get(url)
data = response.json()

# The quote
quote = data['quote']

# Sends the quote to Discord
webhook_url = "https://discord.com/api/webhooks/..."
message = {"content": f"Kanye Westin lainaus: '{quote}'"}
requests.post(webhook_url, json=message)