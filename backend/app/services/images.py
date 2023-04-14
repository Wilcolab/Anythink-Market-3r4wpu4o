from loguru import logger
import openai


def generate_image_by_description(image_description: str) -> str:
    try:
        response = openai.Image.create(
            prompt=image_description,
            n=1,
            size="256x256"
        )
        return response['data'][0]['url']
    except openai.error.OpenAIError as e:
        logger.error(e.error)
        return ""
