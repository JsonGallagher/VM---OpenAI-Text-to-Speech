# Text-to-Speech Voicemail Generator

## Overview

This project demonstrates how to use OpenAI's Text-to-Speech (TTS) capabilities to generate a voicemail greeting. It utilizes the OpenAI API to convert text input into lifelike spoken audio, saved as an MP3 file. This example specifically generates a voicemail message for Jason Gallagher, showcasing the potential use case of enhancing user experience with AI-generated audio content.

## 🔊 Example Output:

<https://bit.ly/AI_VM_Greeting>

## Features

- **Text-to-Speech Conversion**: Converts predefined text into spoken audio using OpenAI's TTS API.
- **High-Quality Voice Models**: Utilizes the `tts-1-hd` model for high-definition audio quality.
- **Customizable Voice Options**: The script uses the "nova" voice, but OpenAI provides various voices that can be easily switched to match different tones and contexts.

## Technologies Used

- Python 3
- [OpenAI API](https://openai.com/api/)
- `requests` library for making HTTP requests in Python
- `dotenv` library for loading environment variables
- `venv` for creating isolated Python environments

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/JsonGallagher/VM---OpenAI-Text-to-Speech
   cd VM---OpenAI-Text-to-Speech
   ```

2. **Set Up a Virtual Environment (recommended):**
**For Windows:**

    ```bash
    Copy code
    python -m venv venv
    venv\Scripts\activate
    ```

    **For macOS and Linux:**

    ```bash
    Copy code
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Required Python Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:

   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:

     ```bash
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Running the Script**:
   - Simply execute the script to generate the voicemail MP3 file:

     ```bash
     python app.py
     ```

## Project Structure

- `app.py`: The main Python script that contains the logic for text-to-speech conversion.
- `.env`: A file to store environment variables securely (not included in the repository for security reasons).
- `requirements.txt`: A file listing the project's dependencies for easy installation.

## Usage Example

The script is designed to be easily customizable. Here's the default text used for the voicemail message:

```python
voicemail_text = "Hello! You've reached the voicemail of Jason Gallagher. He is currently either on another call or unavailable. Please leave your name, number, and a brief message after the tone. For a quicker response, feel free to text this number. We appreciate your call and look forward to speaking with you soon. Thank you!"
```

You can modify the `voicemail_text` variable in `app.py` to suit your needs.

## Contributing

Contributions to enhance the functionality or documentation of this project are welcome. Please feel free to submit a pull request or open an issue.

---

This project is a demonstration of integrating OpenAI's Text-to-Speech API with Python and is intended for educational and demonstration purposes.
