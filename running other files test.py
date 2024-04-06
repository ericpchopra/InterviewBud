import subprocess
from openai import OpenAI
import time 
client = OpenAI()


# Path to the Python file to be run
recorduserpath = "C:\\Users\\Admin\\Documents\\InterviewBud\\recording voice test.py"

# Run the Python file as a separate process
subprocess.run(['python', recorduserpath])

def recorduserinput():
    audio_file= open("C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\STT user speech\\STT AUDIO.wav", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )

    
    print(transcription.text)
    return transcription.text


# Define the file path
STTtranscriptpath = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\STT user generated text\\transcription.txt"

# Write the content to the file
with open(STTtranscriptpath, 'w') as file:
    file.write(recorduserinput())

print(f"File saved to {STTtranscriptpath}")
