import json
import random

import gradio as gr

from advance import advance
from intermediate import intermediate
from websockets_api import get_prompt_images


def process(positive):
    with open("basic_workflow.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)

    prompt["6"]["inputs"]["text"] = f"a half-portrait of a {positive}, highly detail, high resolution"
    prompt["3"]["inputs"]["seed"] = random.randint(0, 999999999999)
    images = get_prompt_images(prompt)
    return images


basic = gr.Interface(
    fn=process,
    inputs=[gr.Textbox(label="Positive Prompt: ")],
    outputs=[gr.Gallery(label="Outputs: ")]
)

demo = gr.TabbedInterface(interface_list=[basic, intermediate, advance],
                          tab_names=["Basic Workflow", "Intermediate Workflow", "Advance Workflow"])

demo.queue()
demo.launch()
