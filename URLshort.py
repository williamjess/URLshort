import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, long_url):
        short_url = self.generate_short_url()
        self.url_mapping[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        return self.url_mapping.get(short_url, "Short URL not found")

# Example usage
shortener = URLShortener()

long_url = "https://www.example.com/very/long/url/that/we/want/to/shorten"
short_url = shortener.shorten_url(long_url)
print("Short URL:", short_url)

expanded_url = shortener.expand_url(short_url)
print("Expanded URL:", expanded_url)