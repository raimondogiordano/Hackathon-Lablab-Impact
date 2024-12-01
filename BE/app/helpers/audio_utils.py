from pydub import AudioSegment
from app.config import config
import os
import io
from pathlib import Path
import ffmpeg 
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile, Depends
config()

def chuncker_audio(file):
    print("chunker")
    source = AudioSegment.from_mp3(file)
    print("source",source)
    if len(source)>int(os.environ['MAX_TIME_HANDLEBLE']):
        ten_minutes = 10 * 60 * 1000
        num_chunks = len(source) // ten_minutes 
        chunks = [source[i*ten_minutes:(i+1)*ten_minutes] for i in range(num_chunks)]
    else:
        return [source]

def chuncker_audio_test(file):
    try:
        print("chunker")
        source = AudioSegment.from_file(io.BytesIO(file))
        ten_minutes = 10 * 60 * 1000
        chunks = [source[:ten_minutes]]
        print("chunks",chunks)
        return chunks
    except Exception as e:
        print("Error in chuncker",e)   

def convert_in_audio_buffer(chunk,name):
    buffer = io.BytesIO()
    buffer.name = name+".mp3"
    chunk.export(buffer, format="mp3")
    return buffer

def upload_file(file):
    # Define the folder where you want to save the file
    upload_folder = "app/archive"
    # Create the folder if it doesn't exist
    Path(upload_folder).mkdir(parents=True, exist_ok=True)
    # Combine folder path and file name to get the full path
    file_path = Path(upload_folder) / file.filename

    # Save the file to the server
    with open(file_path, "wb") as buffer:
        buffer.write(file)

async def convert_audio_to_mp3(audio_file: UploadFile):
    try:
        contents = await audio_file.read()
        flag=False
        audio=None
        file_format = audio_file.filename.split('.')[-1]
        print(file_format)
        if file_format == 'mp3':
            audio = AudioSegment.from_mp3(io.BytesIO(contents))
        elif file_format == 'wav':
            flag=True
            audio = AudioSegment.from_wav(io.BytesIO(contents))
        elif file_format == 'aac':
            flag=True
            audio = AudioSegment.from_file(io.BytesIO(contents), format='aac')
        elif file_format == 'mp4':
            flag=True
            audio = AudioSegment.from_file(io.BytesIO(contents), format='mp4')
        else:
            raise ValueError("Unsupported file format")
        
        mp3_audio = audio.export(format='mp3')
        result=dict()
        result["status"]=flag
        result["source"]=mp3_audio
        return result
    except Exception as e:
        print("Error into conversion",e)

           
