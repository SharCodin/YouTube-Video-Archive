import json
import random
from pathlib import Path

import gradio as gr
import numpy
from PIL import Image

from settings import COMFY_UI_PATH
from websockets_api import get_prompt_images


def save_input_image(img):
    input_img = Path(COMFY_UI_PATH) / "input/intermediate_style_img.jpg"
    pillow_image = Image.fromarray(img)
    pillow_image.save(input_img)


def process(gender, race, hair, color, remove_bg, use_input_img, img, slider):
    with open("advance_workflow.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)

    prompt["6"]["inputs"]["text"] = (f"a half-portrait of a {gender}, {race} with {hair} hair, with {color} skin tone,"
                                     " highly detail, high resolution")
    # prompt["3"]["inputs"]["seed"] = random.randint(0, 999999999999)
    if not use_input_img:
        # prompt["14"]["inputs"]["weight"] = 0.5
        # default_img = numpy.asarray(Image.open("default_style.jpg"))
        # save_input_image(default_img)

        prompt["3"]["inputs"]["model"] = ["10", 0]
    else:
        prompt["3"]["inputs"]["model"] = ["14", 0]
        prompt["14"]["inputs"]["weight"] = slider
        save_input_image(img)

    if remove_bg:
        prompt["39"]["inputs"]["images"] = ["36", 0]
        prompt["35"]["inputs"]["images"] = ["34", 0]
        prompt["32"]["inputs"]["images"] = ["30", 0]
    else:
        del prompt["39"]["inputs"]["images"]
        del prompt["35"]["inputs"]["images"]
        del prompt["32"]["inputs"]["images"]

    images = get_prompt_images(prompt)
    return images


advance = gr.Interface(
    fn=process,
    inputs=[
        gr.Dropdown(choices=["Male", "Female"], label="Gender"),
        gr.Dropdown(choices=["Elf", "Human", "Sorcerer", "Alien"], label="Race"),
        gr.Dropdown(choices=["Short", "Long"], label="Hair"),
        gr.Dropdown(choices=["White", "Black", "Blue", "Yellow"], label="Color"),
        gr.Checkbox(label="Enforce white background"),
        gr.Checkbox(label="use_input_img"),
        gr.Image(label="Style Image: "),
        gr.Slider(label="Image Weight: ", minimum=0.0, maximum=1.0, step=0.05)
    ],
    outputs=[gr.Gallery(label="Outputs: ")]
)
