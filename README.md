# Telegram Bot

This is a simple and interactive Telegram bot built using Python. It responds to various commands like greetings, provides useful links, and handles casual interactions. Additionally, it integrates a deep learning model for generating advanced responses using the `transformers` library.

## Dependencies

- Python 3.8 or higher
- `python-telegram-bot` for Telegram API interaction
- `transformers` for deep learning-based response generation
- `torch` for PyTorch-based operations

## Files Overview

- **main.py**: Contains the core logic for the Telegram bot with command and message handlers.
- **deepseek.py**: Implements the integration of the `transformers` model to generate advanced responses.
- **virtual environment**: It's recommended to use a virtual environment to manage your Python packages and dependencies.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/telegram-bot.git
   cd telegram-bot
   ```

2. **Set up a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install python-telegram-bot transformers torch
   ```

4. **Configure your bot token**:

   Open the `main.py` file and replace `"YOUR-BOT-TOKEN"` with your actual Telegram bot token and also use your username in `"username"`. you can get both from telegram.

5. **Run the bot**:

   ```bash
   python main.py
   ```

Now your bot should be up and running!
