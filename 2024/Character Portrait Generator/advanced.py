import json
import random
from pathlib import Path

import gradio as gr
from PIL import Image

from settings import COMFY_UI_PATH
from websockets_api import get_prompt_images


def save_input_image(img):
    input_img = Path(COMFY_UI_PATH) / "input/advance_input_img.jpg"
    pillow_image = Image.fromarray(img)
    pillow_image.save(input_img)


def process(positive, img, slider, remove_bg):
    with open("advance_workflow.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)

    prompt["6"]["inputs"]["text"] = f"a half-portrait of a {positive}, highly detail, high resolution"
    prompt["3"]["inputs"]["seed"] = random.randint(0, 999999999999)
    prompt["14"]["inputs"]["weight"] = slider

    if remove_bg:
        prompt["44"]["inputs"]["images"] = ["43", 0]
        prompt["45"]["inputs"]["images"] = ["46", 0]
    else:
        del prompt["44"]["inputs"]["images"]
        del prompt["45"]["inputs"]["images"]

    save_input_image(img)

    images = get_prompt_images(prompt)
    return images


advance = gr.Interface(
    fn=process,
    inputs=[
        gr.Textbox(label="Positive Prompt: "),
        gr.Image(label="Style Image: "),
        gr.Slider(label="Image Weight: ", minimum=0.0, maximum=1.0, step=0.05),
        gr.Checkbox(label="Remove BG")
    ],
    outputs=[gr.Gallery(label="Outputs: ")]
)
