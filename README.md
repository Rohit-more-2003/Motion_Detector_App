# Motion Detector App with Email Alerts 📷📧

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Status](https://img.shields.io/badge/Status-Active-success)

A real-time **motion detection application** built using Python and OpenCV that detects movement through a webcam, captures images of the detected object, and **automatically sends an email alert with the image attached**.

---

## 📌 Project Overview

This project continuously monitors webcam footage and detects motion by comparing video frames.  
When motion is detected and then stops, the system:
1. Captures multiple frames
2. Selects the most relevant image
3. Sends an email alert with the detected image
4. Cleans up stored images automatically

The project demonstrates practical use of:
- Computer vision
- Multithreading
- Email automation

---

## 🚀 Features

- Real-time motion detection using webcam
- Motion area detection with contour filtering
- Automatic image capture on detection
- Email alert with image attachment
- Background threading for non-blocking email sending
- Automatic cleanup of captured images
- Graceful exit using keyboard input

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|------------|
| Language | Python |
| Computer Vision | OpenCV |
| Image Processing | NumPy |
| Email | SMTP (Gmail) |
| Concurrency | threading |
| Utilities | glob, os, time |

---

## 📂 Project Structure

```text
Motion_Detector_App/
├── main.py             # Core motion detection logic
├── emailing.py         # Email sending functionality
├── info.py             # Email credentials and configuration
├── images/             # Captured images (created at runtime)
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

git clone <repository_url><br>
cd Motion_Detector_App

python -m venv venv<br>
source venv/bin/activate      # Linux / macOS<br>
venv\Scripts\activate         # Windows

pip install -r requirements.txt

---

## 🔐 Email Configuration

Before running the application, update info.py with valid email credentials:

sender = "your_email@gmail.com"<br>
receiver = "receiver_email@gmail.com"<br>
password = "your_app_password"

---

## ▶️ Run the Application

Start the motion detector with:

python main.py

---

## Controls

Press q to stop the application and release the webcam
