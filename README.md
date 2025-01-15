# Discord Bot

A simple Discord bot built using `discord.py`. This bot connects to Discord and performs automated tasks. Follow the instructions below to download, set up, and run the bot.

---

## Steps to Set Up the Bot

### Step 1: Download the Project
1. Go to the repository on GitHub.
2. Click the **Code** button and select **Download ZIP**.
3. Once downloaded, extract the ZIP file to a folder on your computer.

---

### Step 2: Install Python
Make sure you have [Python 3.9 or higher](https://www.python.org/downloads/) installed on your computer.

To check your Python version, open a terminal/command prompt and run:
```bash
python --version
```

If the version is lower than 3.9 or Python is not installed, download and install it from [Python's download page](https://www.python.org/downloads/).

---

### Step 3: Install Dependencies
1. Open a terminal/command prompt.
2. Navigate to the folder where the bot files were extracted:
   ```bash
   cd path/to/extracted-folder
   ```
3. Run the following command to install all required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 4: Create a `.env` File
The `.env` file is used to store your bot’s token securely. Here's how to create it:

#### Instructions:
1. In the folder where you extracted the files, create a new text file and name it `.env`. Ensure the file has no extension (Windows users may need to remove the `.txt` extension manually).
2. Open the `.env` file in a text editor.
3. Add the following line to the `.env` file:
   ```env
   DISCORD_BOT_TOKEN=your-discord-bot-token-here
   ```
   Replace `your-discord-bot-token-here` with the actual bot token.

---

### Step 5: Get Your Discord Bot Token
To run this bot, you’ll need a bot token from the Discord Developer Portal.

#### Steps to Get Your Token:
1. **Go to the Discord Developer Portal**:
    - Visit [https://discord.com/developers/applications](https://discord.com/developers/applications) and log in with your Discord account.

2. **Create a New Application**:
    - Click the **New Application** button.
    - Provide a name for your bot (e.g., `My Bot`).
    - Click **Create**.

3. **Set Up a Bot**:
    - Go to the **Bot** section on the left-hand menu.
    - Click **Add Bot**.
    - Confirm by clicking **Yes, do it!**.

4. **Copy the Bot Token**:
    - Under the **Token** section, click the **Reset Token** button (or **Reveal Token**, if it's already there).
    - Copy the token provided and paste it into your `.env` file next to `DISCORD_BOT_TOKEN=`.

⚠️ **Important**:
- Keep the token private. DO NOT share it or commit it to GitHub.

---

### Step 6: Invite the Bot to Your Server
To invite your bot to a server:

1. Go back to the **OAuth2** section in the Discord Developer Portal.
2. Under **OAuth2 URL Generator**, do the following:
    - Check the box for `bot` under **Scopes**.
    - Under **Bot Permissions**, select the necessary permissions (e.g., `Send Messages`, `Manage Messages`).
3. Copy the generated URL and paste it into your browser.
4. Choose the server where you want to add the bot and click **Authorize**.

---

### Step 7: Run the Bot
Now that everything is ready, you can start the bot:

#### Instructions:
1. Open a terminal/command prompt in the folder where the bot files were extracted.
2. Run the following command:
   ```bash
   python bot.py
   ```
3. You should see a message like:
   ```
   Logged in as [Your Bot Name]
   ```

The bot will now be running and connected to Discord.

---

## Troubleshooting

- **Python Compatibility Issues**:
    - Ensure you have Python 3.9 or higher: `python --version`.

- **Missing Libraries**:
    - Install required libraries with:
      ```bash
      pip install -r requirements.txt
      ```

- **Bot Token Issues**:
    - Double-check your `.env` file to ensure the token is correct.
    - If needed, regenerate the token on the Discord Developer Portal.

- **Bot Not Responding**:
    - Make sure the bot is invited to your server.
    - Check that the bot has sufficient permissions.

---

## File Structure Example

Your folder should look like this after setup: