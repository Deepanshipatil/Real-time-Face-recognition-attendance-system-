# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# # from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload
# from google.oauth2.service_account import Credentials
# import io
# import numpy as np
# import cv2

# SCOPES = ['https://www.googleapis.com/auth/drive']

# SERVICE_ACCOUNT_FILE = 'database.json'


# PARENT_FOLDER_ID = "1-oPqaBIKXrrftpi7t7OVhHwZGktFlIhq"



# creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)


# service=build('drive', 'v3', credentials=creds)

# request = service.files().get_media(fileId=PARENT_FOLDER_ID)
# file_buffer = io.BytesIO()
# downloader = MediaIoBaseDownload(file_buffer, request)
    
# done = False
# while not done:
#     status, done = downloader.next_chunk()

# # Convert the downloaded file into a NumPy array and then into an OpenCV image
# file_buffer.seek(0)
# array = np.frombuffer(file_buffer.read(), np.uint8)
# imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

# # Display the image (optional)
# cv2.imshow('Image', imgStudent)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import io
import numpy as np
import cv2

# Google Drive API setup
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'database.json'

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Google Drive folder ID (replace this with your folder's ID)
folder_id = "1XfmnvrAb--u8EVESpD1KoEwlyQuz_3dS"

# Step 1: List all files in the folder
query = f"'{folder_id}' in parents and mimeType contains 'image/'"  # Get only image files
results = drive_service.files().list(q=query, fields="files(id, name, mimeType)").execute()
files = results.get('files', [])

if not files:
    print("No image files found in the folder.")
else:
    print(f"Found {len(files)} image(s) in the folder.")

# Step 2: Download and process each image sequentially
for file in files:
    file_id = file['id']
    file_name = file['name']
    print(f"Processing file: {file_name}")

    # Download the file
    request = drive_service.files().get_media(fileId=file_id)
    file_buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(file_buffer, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    # Step 3: Convert the downloaded file into an OpenCV image
    file_buffer.seek(0)
    array = np.frombuffer(file_buffer.read(), np.uint8)
    imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

    # Step 4: Use or display the image
    cv2.imshow('Image', imgStudent)
    cv2.waitKey(1000)  # Wait for a key press to display the next image
    cv2.destroyAllWindows()

print("All images processed.")

