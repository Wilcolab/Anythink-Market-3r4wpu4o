import openai


def generate_image(description: str) -> str:
    generated_image = openai.Image.create(
        prompt=description,
        size="256x256",
        n=1
    )
    image_url = generated_image["data"][0]["url"]
    return image_url