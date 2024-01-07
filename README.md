# Interactive Python-Based Chatbot

**ChatBot** is an interactive Python-based chatbot that leverages various APIs to provide information on general knowledge, weather, mathematics, Wikipedia, and Wolfram Alpha queries. The chatbot is built using the [ChatterBot](https://chatterbot.readthedocs.io/) library for conversational AI.

## Features

- **General Knowledge**: Ask questions about various topics, and the chatbot will provide information.
- **Weather Information**: Get detailed weather information for a specific city, including temperature, description, humidity, and wind speed.
- **Math Operations**: Perform basic math operations by typing mathematical expressions, and the chatbot will calculate the result.
- **Wikipedia Queries**: Retrieve a summary of a topic by asking the chatbot to provide information from Wikipedia.
- **Wolfram Alpha Queries**: Ask the chatbot to query Wolfram Alpha for specific information or calculations.

## Prerequisites

Before running the chatbot, make sure you have the following:

- Python installed on your machine.
- Required Python libraries installed. You can install them using:

```bash
pip install chatterbot wikipedia-api wolframalpha requests python-dotenv
```

## Setup

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/ChatBot.git
cd ChatBot
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
.\venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your API keys:

```makefile
WOLFRAM_ALPHA_API_KEY=your_wolfram_alpha_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

## Usage

Run the chatbot using the following command:

```bash
python main.py
```

The chatbot will greet you and await your input. Type your questions or commands, and the chatbot will respond accordingly.

### Exit

To exit the chatbot, type:

```bash
exit
```

Make sure to replace "your_wolfram_alpha_api_key" and "your_openweathermap_api_key" in the `.env` file with your actual Wolfram Alpha and OpenWeatherMap API keys.
