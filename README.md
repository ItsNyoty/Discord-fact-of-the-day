# Wikipedia Featured Article Discord Bot

A Discord bot that sends the **Wikipedia Featured Article** of the day to a specified channel every 24 hours. The message includes an embed with a short description of the article, a thumbnail (if available), and a URL button to read the full article on Wikipedia.

## Features
- Fetches the featured article from the Wikipedia API daily.
- Sends an embedded message with the article's title, description, and thumbnail.
- Includes a URL button for users to easily read the full article on Wikipedia.
- Fully automated to post every 24 hours.

## Requirements
To run this bot, you need to have:
- Python 3.8 or higher
- A Discord bot token ([create one here](https://discord.com/developers/applications))
- The following Python libraries:
  - `discord.py`
  - `requests`

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/ItsNyoty/Discord-fact-of-the-day.git
   cd wikipedia-discord-bot
   ```

2. **Install the required libraries**:
   Run the following command to install the dependencies:
   ```bash
   pip install discord.py requests
   ```

3. **Configure the bot**:
   - Open the `main.py` file.
   - Replace the placeholders for:
     - `YOUR_DISCORD_BOT_TOKEN`: Your Discord bot token.
     - `YOUR_CHANNEL_ID`: The ID of the Discord channel where you want the bot to send the message.

## Usage

1. **Run the bot**:
   After setting up the bot, you can start it by running:
   ```bash
   python bot.py
   ```

2. The bot will automatically send a daily message to the specified channel with the featured article, along with a clickable URL button to read the full article on Wikipedia.


The embed includes:
- **Title**: The featured article title (e.g., *Apollo 11*).
- **Description**: A short summary of the article.
- **Thumbnail**: A thumbnail image from the article (if available).
- **URL Button**: A button labeled "Click here to read more" that links to the article.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

Made with 💻 and ❤️ by [ItsNyoty](https://github.com/ItsNyoty)

