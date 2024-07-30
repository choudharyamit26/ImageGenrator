import random
import string

STABILITY_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
