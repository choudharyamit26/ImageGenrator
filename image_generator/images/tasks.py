import requests
from celery import shared_task
from django.core.files.base import ContentFile

from .models import GeneratedImage
from .utils import STABILITY_URL, generate_random_string


@shared_task
def generate_image(prompt, api_key):
    response = requests.post(
        STABILITY_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
        file_name = generate_random_string() + '.webp'
        image_file = ContentFile(response.content, file_name)
        image_instance = GeneratedImage(prompt=prompt, image=image_file)
        image_instance.save()
        return {
            'prompt': prompt,
            'msg': "Success",
        }
    else:
        raise Exception(str(response.json()))
