# Telegram AI Bot

This bot connects Telegram with OpenAI's chat completions API.

## Setup

1. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   export TELEGRAM_BOT_TOKEN="<your telegram token>"
   export OPENAI_API_KEY="<your openai api key>"
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```
