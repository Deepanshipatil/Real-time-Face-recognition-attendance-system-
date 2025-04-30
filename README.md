# Face Recognition Attendance System

This project is a **Face Recognition-based Attendance System** that uses machine learning and computer vision to automate attendance marking. It eliminates the need for traditional manual attendance by identifying and recognizing faces in real time using a camera feed.

---

## 🚀 Features

- Real-time face detection and recognition
- Automatic attendance marking
- Integration with **Firebase Realtime Database** for storing attendance logs
- Uses **Google Drive** for storing and accessing student images
- Face encodings generated for accuracy and fast matching

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV** – for video capture and face detection
- **NumPy** – for numerical operations
- **Firebase** – for real-time database storage
- **Google Drive API** – for storing student photos
- `os`, `pickle`, and other standard libraries

---

## 📦 Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/dsheikh2684/Face-Recognition-Attendance-System
cd face-recognition-attendance

✅ 2. Install Required Libraries

Make sure Python is installed (preferably Python 3.9+). Then, install the dependencies:

pip install opencv-python numpy firebase-admin google-api-python-client google-auth google-auth-oauthlib

✅ 3. Firebase Configuration
Create a Firebase project at https://console.firebase.google.com.

Enable Realtime Database (in test mode for development).

Copy the database URL and paste it in the appropriate sections of:

main.py

AddDataToDatabase.py

Download the service account credentials:

Go to Project Settings → Service Accounts

Generate a new private key (JSON)

Save it in your project folder

Reference the file path in AddDataToDatabase.py where it asks for the Firebase credential file

✅ 4. Google Drive Setup
Go to the Google Cloud Console.

Create a new project (or select your existing one).

Navigate to APIs & Services > Library.

Enable the Google Drive API.

Go to APIs & Services > Credentials:

Click Create Credentials > OAuth client ID or Service account

Download the JSON key file and save it in your project directory

Use it to authenticate the Drive API in your code

Create a folder in Google Drive to store student images.

Share this folder (and any uploaded files) with your service account email.

📂 Running the Project
Step-by-step Flow
Add Student Data
Run AddDataToDatabase.py to input student details and upload their photos to Drive.

Generate Encodings
Run EncodeGenerator.py to process images and create facial encodings.

Start Attendance System
Run main.py to start the real-time face recognition and mark attendance.

📌 Notes & Tips
Ensure your system clock is accurate to avoid JWT signature errors with Google APIs.

Ensure that the service account has proper permissions on both Firebase and Drive.

Check that images are clear, frontal faces for better recognition accuracy.

You can customize the system further to support logging, user feedback, or dashboards.

✅ Future Improvements
Add a web-based dashboard for attendance reports

Integrate with SMS/Email APIs for notifications

Improve UI using Tkinter or PyQt

🧑‍💻 Author
Developed by: Danish Khan

Feel free to contribute or raise issues!
