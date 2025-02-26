# **Real-Time Speech Translation Script with Azure & OpenAI**  

Most commercial real-time speech translation solutions are **expensive and complex** (about 0.1 usd for 1 min), making them less accessible for students.  
This project provides a **simple, lightweight, and cost-effective SaaS script**  
that leverages **Azure Speech-to-Text (STT)** and **OpenAI GPT-4o Mini API** for real-time speech translation.  

**Perfect for students who need real-time subtitles for (online and offline) courses, lectures, or study sessions!**  
It runs **directly in the terminal**, displays translations in real time, and automatically logs results to a file.

---

## Features
- **Real-time Speech Recognition**: Uses **Azure Speech-to-Text** to transcribe speech.
- **AI-powered Translation**: Uses **OpenAI GPT-4o Mini** for fast and accurate translation with a avaliable price.
- **Terminal Output**: Displays both the original and translated text.
- **Automatic Logging**: Saves transcription and translation results with a timestamp.
- **Adjustable Recognition Interval**: Modify the recognition interval to balance performance.

---
## ** How to Use**
Using this script is **very simple**—ideal for students who need subtitles while attending online courses.  

### 1. Clone the Repository
```bash
git clone https://github.com/563088655/translate.git
cd translate
pip install azure-cognitiveservices-speech openai
```

### 2. Set the key and language

As be wittened at the code, you can chage them at here:

Firistlly, set your API keys and region:

```bash
OPENAI_API_KEY = "your-api-key"
AZURE_SPEECH_KEY = "your-azure-speech-key"
AZURE_REGION = "your-area"
```

And set the speech recognition language (e.g., "ja-JP" for Japanese, "en-US" for English).
Check the official Azure documentation for more language options.

```bash
speech_config.speech_recognition_language = "set a labguage"
```

Set the source and target languages (e.g., ja for Japanese, en for English).
Check the OpenAI API documentation for supported languages.

```bash
def translate_text(text, source_lang="source_language", target_lang="target_lanhguage"):
    if not text:
        return None
```

### 3. Just run the script to translate

Open your terminal and run:
```bash
python translate_at_terminal.py
```

Now, you can follow courses in foreign languages with real-time subtitles
and automatically save lecture notes for later review!

---
### Example log file:
A log file (subtitles_YYYY-MM-DD_HH-MM-SS.txt) is created:
```bash
[12:30:10] これはテストです。
[12:30:10] This is a test.
```

---
### Thanks
I read this file to check the openai api's usage, install of the offical page.

https://chatgpt-lab.com/n/nde17253a9bc7

---
### Fearure Work

I will develop a **simple subtitle software for macOS** in the future.  
Currently, I am learning **SwiftUI and AVFoundation** to create a native macOS application  
that provides **real-time speech recognition, translation, and subtitle overlay**.

I am also considering integrating a **local AI translator** to **reduce costs and enhance privacy**  
（mainly because I'm broke）
