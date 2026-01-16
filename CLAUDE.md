# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Better Dictation for Mac is a Python-based speech-to-text tool that replaces macOS's built-in dictation with OpenAI's Whisper API for more accurate transcription. It runs as a background process that listens for a global hotkey, records audio, transcribes it via the Whisper API, and types the result into the active application.

## Running the Application

```bash
# Set up virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the main application (uses OpenAI API)
python better_dictation_api.py
```

Requires a `.env` file with `OPENAI_API_KEY=your-api-key-here`.

## Architecture

The project has two script variants:
- `better_dictation_api.py` - Main script using the new OpenAI client API (`from openai import OpenAI`)
- `better_dictation_local.py` - Legacy script using the old OpenAI API format (`openai.Audio.transcribe`)

Both scripts share the same structure:
1. **Keyboard listener** (`pynput`): Listens for Cmd+Option+K (detected as `˚` character)
2. **Audio recording** (`sounddevice`): Captures audio at 16kHz mono via an `InputStream` with callback
3. **Transcription** (`openai`): Sends recorded WAV to Whisper API
4. **Text insertion** (`pyautogui`): Types transcribed text at cursor position

Global state variables (`is_recording`, `audio_data`, `start_time`) control recording flow. The `play_buzz()` function provides audio feedback when recording starts/stops.

## Key Configuration

- `MAX_RECORDING_TIME = 100` seconds (auto-stops recording if exceeded)
- Audio format: 16kHz sample rate, mono channel, 16-bit depth
- Hotkey: Cmd+Option+K (toggled start/stop)
