# DM ALL BOT

A simple Discord bot to send direct messages (DMs) to all members in a server.

## Features
- `$dmall [message]`: Send a DM to all members in the server (admin only).
- `$info`: Show help and command usage.
- Permission check: Only allowed users (by user ID) can use the DM all command.
- Console logging for sent and failed DMs.

## Setup

### Prerequisites
- Python 3.8+
- `discord.py` library

### Installation
1. **Download this respository**
2. **Install dependencies**
   ```sh
   pip install -U discord.py
   ```
3. **Configure the bot**
   - Edit `config.json` and add your bot token and replace the current user ID to your user ID:
     ```json
     {
       "TOKEN": "YOUR_BOT_TOKEN",
       "allowed_user_ids": [1025029483847241738]
     }
     ```

## Usage
- Run the bot:
  ```sh
  python main.py
  ```
- In Discord, use:
  - `$dmall your message here` to DM all server members (if allowed)
  - `$info` to see help

## Notes
- The bot must have permission to read members and send DMs.
- Use responsibly! Spamming users may violate Discord's Terms of Service.