from dotenv import load_dotenv
import requests
from pathlib import Path
import os

# Load environment variables from .env file
load_dotenv()

# Now, accessing the API key from the environment variables
API_KEY = os.getenv("OPENAI_API_KEY")

def save_text_to_speech_direct(text, filename):
    # Set up the headers with the Authorization token
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    # Define the data payload for the POST request
    data = {
        "model": "tts-1-hd",
        "input": text,
        "voice": "nova",
        # You can add other parameters here if needed
    }
    
    # Make the POST request to the OpenAI API
    response = requests.post("https://api.openai.com/v1/audio/speech", json=data, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the audio content to the specified file
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved speech to: {filename}")
    else:
        # Print the error if the request was not successful
        print("Error generating speech:", response.text)

# Define the path where you want to save the speech file
speech_file_path = Path(__file__).parent / "voicemail.mp3"

# Example usage of the function to generate speech from text
voicemail_text = "Hello! You've reached the voicemail of Jason Gallagher. He is currently either on another call or unavailable. Please leave your name, number, and a brief message after the tone. For a quicker response, feel free to text this number. We appreciate your call and look forward to speaking with you soon. Thank you!"
save_text_to_speech_direct(voicemail_text, speech_file_path)