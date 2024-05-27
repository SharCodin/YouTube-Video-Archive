import json
from pathlib import Path

import gradio as gr
from PIL import Image

from settings import COMFY_UI_PATH
from websockets_api import get_prompt_images


def save_input_image(img):
    input_img = Path(COMFY_UI_PATH) / "input/intermediate_style_img.jpg"
    pillow_image = Image.fromarray(img)
    pillow_image.save(input_img)


def process(gender, race, hair, hair_color, skin_color, eye_color, clothing_style, accessories, expression, remove_bg,
            use_input_img, img, slider):
    with open("flagged/advance_workflow.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)

    prompt["6"]["inputs"]["text"] = (
        f"a half-portrait of a {gender}, {race} with {hair} hair ({hair_color}), with {skin_color} skin tone, "
        f"{eye_color} eyes, wearing {clothing_style}, {accessories}, {expression} expression, highly detailed, high resolution"
    )

    if not use_input_img:
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


def advance_app():
    with gr.Blocks() as advance:
        with gr.Row():
            with gr.Column():
                with gr.Accordion("Character Attributes"):
                    gender = gr.Dropdown(choices=["Male", "Female", "Non-binary"], label="Gender")
                    race = gr.Dropdown(choices=["Human", "Elf", "Dwarf", "Orc", "Alien", "Sorcerer", "Fairy", "Vampire"],
                                       label="Race")
                    hair = gr.Dropdown(choices=["Short", "Long", "Curly", "Straight", "Wavy", "Bald"], label="Hair Style")
                    hair_color = gr.Dropdown(
                        choices=["Black", "Brown", "Blonde", "Red", "Gray", "Blue", "Green", "Pink", "Purple"],
                        label="Hair Color")
                    skin_color = gr.Dropdown(choices=["Pale", "Fair", "Medium", "Olive", "Brown", "Dark"], label="Skin Tone")
                    eye_color = gr.Dropdown(choices=["Blue", "Green", "Brown", "Hazel", "Amber", "Gray", "Red"],
                                            label="Eye Color")
                    clothing_style = gr.Dropdown(
                        choices=["Casual", "Formal", "Sporty", "Armor", "Robe", "Steampunk", "Futuristic"],
                        label="Clothing Style")
                    accessories = gr.Dropdown(choices=["None", "Glasses", "Hat", "Earrings", "Necklace", "Scarf"],
                                              label="Accessories")
                    expression = gr.Dropdown(choices=["Happy", "Sad", "Angry", "Surprised", "Neutral", "Smiling", "Frowning"],
                                             label="Expression")
                    remove_bg = gr.Checkbox(label="Enforce white background")
                    use_input_img = gr.Checkbox(label="Use input image")
                    img = gr.Image(label="Style Image: ")
                    slider = gr.Slider(label="Image Weight: ", minimum=0.0, maximum=1.0, step=0.05)

            with gr.Column():
                outputs = gr.Gallery(label="Outputs: ", height=800)

        gr.Button("Generate").click(
            fn=process,
            inputs=[gender, race, hair, hair_color, skin_color, eye_color, clothing_style, accessories, expression,
                    remove_bg, use_input_img, img, slider],
            outputs=outputs
        )

    return advance
