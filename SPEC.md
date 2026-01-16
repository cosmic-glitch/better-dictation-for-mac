# Better Dictation for Mac - Native App Specification

## Overview

A native macOS menu bar application that provides high-quality speech-to-text transcription using OpenAI's Whisper API. The app runs in the background and allows users to dictate text into any application via a customizable hotkey.

---

## Core Features

### 1. Speech-to-Text Dictation

- User activates recording via a global hotkey
- Audio is captured from the system's default microphone
- Recording stops when user presses the hotkey again
- Audio is sent to OpenAI Whisper API for transcription
- Transcribed text is automatically typed at the current cursor position in any application

### 2. Recording Behavior

- Maximum recording duration: 100 seconds (configurable)
- Recording automatically stops and transcribes when max duration is reached
- Audio feedback (short beep/buzz) plays when recording starts and stops
- Visual indicator shows recording state

---

## User Interface

### Menu Bar Presence

- App lives in the macOS menu bar (no Dock icon)
- Menu bar icon indicates current state:
  - **Idle**: Default icon
  - **Recording**: Animated or highlighted icon
  - **Processing**: Distinct icon showing transcription in progress

### Menu Bar Dropdown

Clicking the menu bar icon reveals:

1. **Status display**: Current state (Idle / Recording / Processing)
2. **Start/Stop Recording**: Manual trigger (in addition to hotkey)
3. **Settings...**: Opens preferences window
4. **About**: App version and credits
5. **Quit**: Exit the application

### Preferences Window

Organized into sections:

#### General
- **Launch at Login**: Toggle to start app automatically on system boot
- **Audio Feedback**: Toggle to enable/disable start/stop sounds
- **Feedback Sound**: Choose from preset sounds or custom sound file

#### Hotkey
- **Recording Hotkey**: Configurable keyboard shortcut
  - Default: Double-tap Right Option key
  - Alternative: Single key combination (e.g., Cmd+Shift+D)
- **Hotkey Style**:
  - Double-tap single key
  - Key combination (hold modifier + press key)

#### Transcription
- **Language**: Select transcription language (or "Auto-detect")
- **Max Recording Duration**: Slider or input (10-300 seconds)

#### API
- **OpenAI API Key**: Secure text field for entering API key
- **Test Connection**: Button to verify API key is valid

---

## Notifications & Feedback

### Audio Feedback
- Short tone when recording starts
- Different tone when recording stops
- Optional: Error sound on transcription failure

### Visual Feedback
- Menu bar icon changes during recording
- Optional: Floating indicator showing recording duration

### System Notifications
- Notification on transcription error (with error message)
- Notification if API key is missing or invalid
- Notification if microphone access is denied

---

## Permissions & Security

### Required Permissions
- **Microphone Access**: For audio recording
- **Accessibility Access**: For typing text into other applications
- **Input Monitoring**: For global hotkey detection

### First Launch Experience
- App guides user through granting necessary permissions
- Clear explanations of why each permission is needed
- Settings opens relevant System Preferences pane if permission denied

### API Key Storage
- API key stored securely in macOS Keychain
- Never displayed in plain text after entry

---

## Error Handling

### User-Facing Error States

| Scenario | Behavior |
|----------|----------|
| No API key configured | Prompt to enter API key in settings |
| Invalid API key | Notification with "Check API key" message |
| No microphone access | Notification with link to System Preferences |
| No accessibility access | Notification with link to System Preferences |
| Network error during transcription | Notification with retry suggestion |
| Recording too short (< 0.5s) | Discard without API call, optional notification |
| Transcription returns empty | No text typed, optional notification |

---

## Behavior Details

### Text Insertion
- Text is typed character-by-character at current cursor position
- Works in any application that accepts keyboard input
- Preserves focus in the target application

### Recording
- Uses system default input device
- Mono audio capture
- Recording indicator visible at all times during recording

### App Lifecycle
- Runs silently in background after launch
- Minimal resource usage when idle
- No windows open by default (menu bar only)

---

## Future Considerations (Out of Scope for v1)

These features are noted for potential future versions but are NOT part of the initial specification:

- Multiple transcription service support (local Whisper, other APIs)
- Transcription history/log
- Custom text processing (auto-punctuation rules, text replacement)
- Multiple hotkey profiles
- Transcription prompt/context for better accuracy
- Audio input device selection
- Integration with other apps (Shortcuts, AppleScript)

---

## Success Criteria

The app is considered complete when:

1. User can record and transcribe speech using a global hotkey
2. Transcribed text appears at cursor in any application
3. App runs reliably in the menu bar without Dock presence
4. All required permissions are properly requested and handled
5. API key can be configured and stored securely
6. Recording state is clearly indicated visually and audibly
7. Errors are communicated clearly to the user
