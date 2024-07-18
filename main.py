from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

class PostData(BaseModel):
    device_id: str
    temperature: float
    file_name: str

@app.post("/upload/")
async def upload_data(
    device_id: str = Form(...),
    temperature: float = Form(...),
    file_name: str = Form(...),
    image: UploadFile = File(...)
):
    # Create a directory for the device ID if it doesn't exist
    device_dir = f"./{device_id}"
    '''
    #os.makedirs(device_dir, exist_ok=True)
    
    # Path to the CSV file
    #csv_file_path = os.path.join(device_dir, "temp.csv")
    
    # Append temperature data to the CSV file
    new_data = pd.DataFrame([{"temperature": temperature}])
    if os.path.exists(csv_file_path):
        existing_data = pd.read_csv(csv_file_path)
        combined_data = pd.concat([existing_data, new_data])
    else:
        combined_data = new_data
    combined_data.to_csv(csv_file_path, index=False)
    
    # Save the uploaded image to the device directory
    image_path = os.path.join(device_dir, file_name)
    with open(image_path, "wb") as f:
        f.write(await image.read())
    '''
    return {"message": "Data uploaded successfully"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
