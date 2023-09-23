import pyautogui
import sqlite3
from datetime import datetime
import io
import time


def save_screenshot():

    screenshot = pyautogui.screenshot()


    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    screenshot_bytes = buffer.getvalue()


    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ss (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            image BLOB
        )
    ''')

    cursor.execute('''
        INSERT INTO ss (timestamp, image)
        VALUES (?, ?)
    ''', (timestamp, screenshot_bytes))

    conn.commit()
    conn.close()


    filename = f"Images/Screenshot_{timestamp}.png"
    screenshot.save(filename)

    print("Screenshot saved as an image file and in the database.")


time.sleep(3)

