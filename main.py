from fastapi import FastAPI, UploadFile
import os

app = FastAPI()

@app.get("/")
def root():
    return "Hello RAG fellow!"

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    folder = "sources"
    os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist

    file_location = os.path.join(folder, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())  # Write the file to the directory

    return {"info": "File saved", "filename": file.filename}