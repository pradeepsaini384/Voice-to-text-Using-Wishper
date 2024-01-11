# import requests

# API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
# headers = {"Authorization": "Bearer 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"}

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# output = query("harvard.wav")
# print(output)

# import sounddevice as sd
# import scipy.io.wavfile as wav
# from openai import OpenAI
# client = OpenAI()

# file_path = audio_file_path = "recorded_audio.wav"

# print("Recording audio... Press Ctrl+C to stop.")
# duration = 10  # Set the recording duration in seconds

#     # Record audio from the microphone
# audio_data = sd.rec(int(duration * 44100), channels=2, dtype='int16')
# sd.wait()

#     # Save the audio file
# wav.write(file_path, 44100, audio_data)

# print(f"Audio recorded and saved to {file_path}")
# audio_file= open("recorded_audio.wav", "rb")
# transcript = client.audio.transcriptions.create(
# model="whisper-1", 
# file=audio_file
#     )
# print(transcript)


import sounddevice as sd
import scipy.io.wavfile as wav
from openai import OpenAI

# Set your OpenAI API key
# openai.api_key = 'YOUR_API_KEY'
client = OpenAI()

file_path = "recorded_audio.wav"
print("Recording audio... Press Ctrl+C to stop. or say stop ")
while True:
    # print("Recording audio... Press Ctrl+C to stop.")
    duration = 5  # Set the recording duration in seconds

    # Record audio from the microphone
    audio_data = sd.rec(int(duration * 44100), channels=2, dtype='int16')
    sd.wait()

    # Save the audio file
    wav.write(file_path, 44100, audio_data)
    # Use OpenAI API for transcription
    audio_file = open(file_path, "rb")
    try:
        transcript = client.audio.translations.create(
            model="whisper-1", 
            file=audio_file
        )
        print(transcript.text,end=" ")
    except Exception as e:
        print(f"Error in transcription: {e}")

    audio_file.close()
    if transcript.text.lower().strip() in ['stop', 'Stop.','stop. ', 'stop.', 'stopped', 'stopped.', 'stopped']:
        print("Stopping real-time speech recognition.")
        break