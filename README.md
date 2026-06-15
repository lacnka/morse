# Morse Code Keyboard Bot

An automation script that converts plain text into international Morse code and physically simulates your choice of keyboard taps (like the spacebar) at any target Words Per Minute (WPM) speed.

## Quick Start Guide

### 1. Download to Desktop
Ensure that both your `morse_bot.py` file and this `README.md` file are downloaded and saved directly onto your **Desktop**.

### 2. Install the Required Library
Before running the script, you must install the keyboard automation library.
* Open your Command Prompt (Windows) or Terminal (Mac).
* Type the following command and press **Enter**:
  ```bash
  pip install keyboard
  ```

### 3. Open Terminal on Desktop
* Go to your **Desktop**.
* **Right-click** on an empty space on your Desktop screen.
* Click **Open in Terminal** (or *Open in Command Prompt* / *Open in PowerShell* depending on your operating system).

### 4. Run the Script
Inside the terminal window that just opened, type the following command exactly and press **Enter**:
```bash
python morse_bot.py
```

---

## How to Use the Bot

1. **Enter Message:** Type the sentence or text you want to send (supports letters, numbers, and punctuation symbols).
2. **Enter WPM:** Type your desired speed (e.g., `5` for slow testing, `15` for standard, `25` for fast).
3. **Enter Key:** Choose which key the bot should tap. Type `space` for the spacebar, or type any letter/number (like `e` or `1`).
4. **Switch Windows:** You will have a **3-second countdown** to click inside your game, chat app, or text file before the automated tapping starts.

⚠️ **EMERGENCY STOP:** If the bot goes wild or you need to cancel the transmission immediately, press and hold the **`Esc`** key on your keyboard to instantly force the script to stop.
