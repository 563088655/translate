import azure.cognitiveservices.speech as speechsdk
from openai import OpenAI
import sys
import time
import datetime

# ** API **
OPENAI_API_KEY = "your-api-key"
AZURE_SPEECH_KEY = "your-azure-speech-key"
AZURE_REGION = "your-area"

# ** Azure **
speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_REGION)
speech_config.speech_recognition_language = "set a labguage"  
audio_config = speechsdk.AudioConfig(use_default_microphone=True)

# ** OpenAI **
client = OpenAI(api_key=OPENAI_API_KEY)

# ** write to your file **
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"subtitles_{timestamp}.txt"

# ** STT **
def recognize_speech():
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("waiting for input...")
    
    result = recognizer.recognize_once()  # recognize once
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"recognized: {result.text}")
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Warning: no speech detected")
        return None
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("cancelled")
        return None

# ** translate with openai **
def translate_text(text, source_lang="source_language", target_lang="target_lanhguage"):
    if not text:
        return None  

    prompt = f"please translate the following text from {source_lang} to {target_lang}:\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}],
            temperature=0.3,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        translated_text = response.choices[0].message.content
        print(f"translated: {translated_text}")
        return translated_text
    
    except Exception as e:
        print(f"failed: {e}")
        return None

# wirite to file
def write_to_file(original, translated):
    with open(log_file, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(f"[{timestamp}] {original}\n[{timestamp}] {translated}\n\n")

def main_loop():
    while True:
        spoken_text = recognize_speech()
        if spoken_text:
            translated_text = translate_text(spoken_text)
            if translated_text:
                print(f"\n📜 {spoken_text}\n🌍 {translated_text}\n")
                write_to_file(spoken_text, translated_text)
        time.sleep(2)  # you can change the time to loop

if __name__ == "__main__":
    print("sub will be shown at terminal and saved to a file, press ctrl+c to stop")
    print(f"log file: {log_file}\n")
    main_loop()