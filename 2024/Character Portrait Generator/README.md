# Character Portrait Generator with ComfyUI, Python, and WebSockets

This repository contains the code and resources for building a Character Portrait Generator web application using ComfyUI, Python, and WebSockets. This project is designed to help you create character portraits through a web interface, progressing from a basic setup to more advanced features.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project demonstrates how to build a character portrait generator using ComfyUI, Python, and WebSockets. It includes three versions of the application:
1. **Basic Version:** A simple prompt-based image generator.
2. **Intermediate Version:** Allows users to upload images to use as references.
3. **Advanced Version:** Features a dynamic character creation menu with sliders and checkboxes.

## Features

- **Basic Version:**
  - Simple positive prompt input.
  - Generates character portraits based on the prompt.
- **Intermediate Version:**
  - Image upload feature.
  - Generates portraits based on the style and composition of the uploaded image.
- **Advanced Version:**
  - Dynamic character creation menu.
  - Programmatically connects and disconnects nodes.

## Requirements

- Python 3.7 or higher
- ComfyUI
- Gradio
- Pillow
- NumPy
- WebSocket-Client

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/character-portrait-generator.git
   cd character-portrait-generator
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure ComfyUI:**
   - Ensure ComfyUI is installed, properly configured and running.
   - Set the `server_address` in `settings.py` to match the ComfyUI server URL.
   - Set the `comfy_ui_path` in `settings.py` to the path of your ComfyUI installation.

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Access the application:**
   - Open the provided local URL in your web browser.
   - Use the web interface to generate character portraits.

## Project Structure

- `main.py`: Main script to run the application.
- `settings.py`: Configuration file for server address and ComfyUI path.
- `websockets_api.py`: Utility functions for connecting to ComfyUI and retrieving images.
- `workflow.json files`: workflow files for ComfyUI.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License.

## Show your Support

- [Patreon](https://bit.ly/44js1Xx)

- [Paypal](https://bit.ly/45lJsIg)

- [YouTube Channel](https://bit.ly/4b0o8dQ)

- [Twitter X](https://bit.ly/3ReP9D3)
