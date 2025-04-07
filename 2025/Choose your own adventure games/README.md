# Choose Your Own Adventure Game with Python and Gemini AI

This project is an interactive story chatbot that generates a dynamic narrative based on user choices.

## Features
- Starts with a predefined prompt.
- Users make choices to influence the story.
- The story progresses through a randomized number of interactions.
- The user chooses between a good, neutral, or bad ending.

## Setup

### 1. Set up your API key

#### **Windows (GUI method)**
1. Click **Start** and search for **"Edit the system environment variables"**, then open it.
2. In the **System Properties** window, click **Environment Variables**.
3. Under **User variables**, click **New...**.
4. Set the **Variable name** to `GEMINI_API_KEY`.
5. Set the **Variable value** to your API key.
6. Click **OK**, then **OK** again to save.
7. Restart your terminal or command prompt to apply the changes.

#### **Windows (Command Line method)**
Run the following command in **Command Prompt**:
```sh
setx GEMINI_API_KEY "your_api_key_here"
```
Restart the terminal to apply the changes.

#### **MacOS/Linux**
Run this command in your terminal:
```sh
export GEMINI_API_KEY="your_api_key_here"
```
To make it permanent, add it to your `~/.bashrc` or `~/.zshrc` file:
```sh
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc  # For Bash
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.zshrc  # For Zsh
```
Then, reload the file:
```sh
source ~/.bashrc  # or source ~/.zshrc
```

### 2. Create and activate a virtual environment

- **Windows:**
  ```sh
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **MacOS/Linux:**
  ```sh
  python -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the script
```sh
python main.py
```

## Usage
- Enter choices `1, 2, or 3` and press `Enter` to continue the story.
- Type `"exit"` to quit anytime.

Enjoy your interactive storytelling adventure! 🚀