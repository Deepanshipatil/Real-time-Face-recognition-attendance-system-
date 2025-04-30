import cv2
import face_recognition
import pickle
import os

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['google-api-link']

SERVICE_ACCOUNT_FILE = 'path-to-json-file'


PARENT_FOLDER_ID = ""

def authenticate():

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)
    return creds

def upload_photo(file_path,Name):

    creds = authenticate()

    service=build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': Name,
        'parents': [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
# upload_photo("debu.png")  

folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    print("printing",type(os.path.splitext(path)[0]))
    # Read the image and append it to the list
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    upload_photo(os.path.join(folderPath, path),os.path.splitext(path)[0])
    # # File path and metadata for Google Drive
    # fileName = os.path.join(folderPath, path)
    # file_metadata = {'name': path}  # File name in Google Drive

    # Replace this Firebase upload block with Google Drive upload
    # media = MediaFileUpload(fileName, mimetype='image/jpeg')  # Adjust MIME type if needed
    # uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Print uploaded file details
    print(f"Uploaded: {path}")
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")