from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import wikipediaapi
import wolframalpha
import requests
import re 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API keys
wolfram_alpha_api_key = os.environ.get('WOLFRAM_ALPHA_API_KEY')
openweathermap_api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

if not wolfram_alpha_api_key or not openweathermap_api_key:
    raise ValueError("API keys are missing. Check your .env file.")

# Create a new chat bot
chatbot = ChatBot('ChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI, user_agent='ChatBot/1.0 (abiolaalalade)')

# Wolfram Alpha API key
wolfram_alpha = wolframalpha.Client(wolfram_alpha_api_key)


# Function to get information from Wikipedia
def get_wikipedia_summary(query):
    page_py = wiki_wiki.page(query)
    if page_py.exists():
        return page_py.summary[:300]  # Limit the summary length
    else:
        return "I couldn't find information on that topic. Can you ask something else?"

# Function to get information from Wolfram Alpha
def get_wolfram_alpha_result(query):
    res = wolfram_alpha.query(query)
    try:
        return next(res.results).text
    except StopIteration:
        return "I couldn't find information on that topic. Can you ask something else?"

# Function to get detailed weather information in Fahrenheit
def get_weather(city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}&units=imperial'
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] == '404':
        return "I couldn't find information for that city. Please try again."

    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    return f"The weather in {city} is currently {description} with a temperature of {temperature}°F. Humidity: {humidity}%, Wind Speed: {wind_speed} mph."


# Function to perform basic math operations
def calculate_math_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Define a function for chatting with the bot
def chat_with_bot():
    print("ChatBot: Hello! I'm here to impress you. Ask me anything, and I'll do my best to provide information.")

    while True:
        user_input = input("You: ")
        response = ""  # Initialize response variable

        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye! It was impressive chatting with you.")
            break

        elif 'capabilities' in user_input.lower() or 'what can you do' in user_input.lower():
            capabilities_response = (
                "I can provide information on various topics. You can ask me about:\n"
                "- General knowledge (e.g., 'Tell me about Abraham Lincoln')\n"
                "- Weather (e.g., 'What's the weather in Paris?')\n"
                "- Math (e.g., 'Calculate 2 + 2')\n"
                "- Wikipedia information (e.g., 'Wikipedia on Python programming language')\n"
                "- Wolfram Alpha queries (e.g., 'Wolfram Alpha about quadratic equations')"
            )
            response = capabilities_response

        elif 'wikipedia' in user_input.lower():
            query = user_input.split('on')[-1].strip()
            response = get_wikipedia_summary(query)
        elif 'wolfram' in user_input.lower():
            query = user_input.split('about')[-1].strip()
            response = get_wolfram_alpha_result(query)
        elif 'weather' in user_input.lower():
            city = user_input.split('in')[-1].strip()
            response = get_weather(city)
        elif any(char.isdigit() for char in user_input):  # Check if the input contains a digit
            math_expression = re.sub(r'[^0-9+*/\-]', '', user_input)  # Remove unwanted characters
            response = calculate_math_expression(math_expression)
        else:
            response = chatbot.get_response(user_input)

        print("ChatBot:", response)

# Start the chat
chat_with_bot()
