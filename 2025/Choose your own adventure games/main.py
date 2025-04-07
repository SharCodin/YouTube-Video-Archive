import random

from api import API_KEY, chat
from prompts import initial_prompt


def main():
    if not API_KEY:
        raise ValueError("Set up an environment variable with your API key "
                         "using the variable name: 'GEMINI_API_KEY'")
    # initial prompt
    response = chat.send_message(initial_prompt)
    print(response.text)
    stop_index = random.randint(4, 6)
    current_index = 0
    while True:
        if current_index >= stop_index:
            choice = ("The next section is the ending. "
                      "Choose yourself and Continue the story "
                      "to its ending. Decide for a good, neutral or bad ending."
                      "Finish with 'The End - {good/neutral/bad} Ending!'")
            response = chat.send_message(choice)
            print(f"Story:\n\n{response.text}")
            break
        else:
            # user choice
            choice = input("Type in your choice: ")
            current_index += 1
            if choice == "exit":
                break
            response = chat.send_message(choice)
            print(f"Story:\n\n{response.text}")


if __name__ == "__main__":
    main()
