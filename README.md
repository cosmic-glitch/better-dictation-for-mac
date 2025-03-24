# Better Dictation for Mac

A replacement for macOS's built-in dictation feature that provides more accurate transcription using OpenAI's Whisper speech-to-text model.  This is the same model that is used by OpenAI to transcribe voice inputs in the ChatGPT app.

## Prerequisites

Before using this tool, you must have [whisper.cpp](https://github.com/ggerganov/whisper.cpp) installed on your Mac. Follow the installation instructions in their repository.

## Features

- More accurate speech-to-text transcription compared to macOS's default dictation
- Uses the high-quality Whisper speech recognition model from OpenAI
- Seamlessly integrates with your Mac's keyboard shortcuts

## Usage

1. Press Command + Option + K to start dictation
2. Speak into your microphone, and then press Command + Option + K again
3. The transcribed text will be automatically typed where your cursor is located

## How it Works

This tool records audio when activated, processes it through whisper.cpp for transcription, and then types out the result as if it were typed from your keyboard. It provides a more accurate alternative to the built-in macOS dictation feature.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/better-dictation-mac.git
   cd better-dictation-mac
   ```

2. Install the required Python dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python better_dictation.py
   ```

