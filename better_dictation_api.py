import numpy as np
import sounddevice as sd
from pynput import keyboard
import os
import pyautogui
import wavio
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

is_recording = False
audio_data = []
start_time = 0
MAX_RECORDING_TIME = 100  # Maximum recording time in seconds

def on_press(key):
    global is_recording, audio_data, start_time
    try:
        # Check if the key combination is Command + Option + K
        if hasattr(key, 'char') and key.char == '˚':
            if not is_recording:
                print("Started recording...")
                is_recording = True
                audio_data = []
                start_time = time.time()
                play_buzz()
                stream.start()
            else:
                # Stop recording
                print("Stopped recording...")
                is_recording = False
                stream.stop()
                handle_recording()
                play_buzz()
    except AttributeError:
        pass

def handle_recording():
    global audio_data, start_time

    recording_duration = time.time() - start_time
    filename = 'recording.wav'
    wavio.write(filename, np.array(audio_data), 16000, sampwidth=2)

    audio_data = []
    
    if recording_duration >= MAX_RECORDING_TIME:
        print("Recording exceeded maximum duration. No text will be typed.")
        return

    try:
        # Open the audio file
        with open(filename, "rb") as audio_file:
            # Call OpenAI's Whisper API using the new format
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="en"
            )
            
            # Get the transcribed text
            text = transcript.text.strip()
            print(text)
            pyautogui.typewrite(text)
            
    except Exception as e:
        print(f"Failed to transcribe audio: {str(e)}")

def callback(indata, frames, time_info, status):
    global is_recording, start_time, audio_data
    if status:
        print(status)
    audio_data.extend(indata[:, 0])  # Ensure we are extending with 1D data
    
    # Check if recording time exceeds MAX_RECORDING_TIME
    current_time = time.time()
    if is_recording and (current_time - start_time) >= MAX_RECORDING_TIME:
        print("Maximum recording time reached. Stopping recording...")
        is_recording = False
        stream.stop()
        handle_recording()
        play_buzz()

def play_buzz(duration=0.1, frequency=440):
    fs = 44100  # Sample rate
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    sd.play(wave, samplerate=fs)
    sd.wait()

stream = sd.InputStream(samplerate=16000, channels=1, callback=callback)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
