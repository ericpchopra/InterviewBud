import os
from pathlib import Path
from openai import OpenAI
import pygame
import pyaudio
import wave
import soundfile as sf
import subprocess
import time

client = OpenAI()

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Navigate to the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Create a new text file in the parent directory
file_path = os.path.join(parent_directory,'InterviewBud','resources', 'initial questions.txt')
questions = ['What is your age? ','How many questions would you like in your interview? (maximum 10) ', 'For what position are you taking this interview? ','For what organisation is this interview being held for? ','Which country is this interview being held?']
# Open the file in write mode
with open(file_path, 'w') as file:
    # Ask the user 5 questions and write their answers to the file
    for i in questions:
        question = i
        print(i)
        answer = input("Answer: ")
        file.write(f"{answer}\n\n")

print("Answers saved to:", file_path)


# Specify the path to the text file
file_path = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\initial questions.txt"  # Update this with the path to your text file

# Open the text file in read mode
with open(file_path, 'r') as file:
    # Read the third line of the file
    lines = file.readlines()
    
    
    
    a1 = lines[0]
    a2 = lines[2]
    a3 = lines[4]
    a4 = lines[6]
    a5 = lines[8]



completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {f"role": "system", "content": f"""You are the following technological tool: Interview Simulator: Create a tool for job interview practice where users can simulate interviews by speaking their responses to common interview questions. The tool would transcribe the user's responses, provide feedback, and generate synthesized speech for the interviewer's questions.

The interviewer is {a1} years of age and would like to be asked {a2} questions. The interview is for a {a3} position at the organisation called {a4}. The interview will be held in the country {a5}

Please now give {a2} mock interview questions to be asked to the user relevant to the given information, with each new question being seperated with a new line."""},
  ]
)



generatedqs_path = os.path.join(parent_directory,'InterviewBud','resources', 'generated questions.txt')
# Open the file in write mode
with open(generatedqs_path, 'w') as file:
    # Ask the user 5 questions and write their answers to the file
    
    file.write(completion.choices[0].message.content)
    print("Generated questions saved to:", generatedqs_path)
#convert generated questions text file to a tuple
def read_numbered_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Remove leading/trailing whitespaces and convert to tuple
        genquestionlist = tuple(line.strip() for line in lines if line.strip())
    return genquestionlist

filename = 'C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\generated questions.txt'
genquestionlist = read_numbered_list(filename)

###TTS audo file generation module ##############################################################################

#generate the TTS audio files
for i in genquestionlist:
    speech_file_path = f"C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS generated questions\\TTS_question_{genquestionlist.index(i)+1}.mp3"
    response = client.audio.speech.create(
      model="tts-1",
      voice="shimmer",
      input= i
    )
    response.stream_to_file(speech_file_path)

numberofquestions = len(genquestionlist)
#########################STT module################################################################################
# Path to the Python file to be run
def useraskSTT():
    runsttpath = "C:\\Users\\Admin\\Documents\\InterviewBud\\running other files test.py"
    subprocess.run(['python', runsttpath])

# run tts file whichever one needed
def runTTSfile(i):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    audio_file = f"C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS generated questions\\TTS_question_{i}.mp3"
    pygame.mixer.music.load(audio_file)

    # Play the audio
    pygame.mixer.music.play()

    # Wait while the audio is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop the playback
    pygame.mixer.music.stop()
    
for i in range(numberofquestions):
    runTTSfile(i+1)
    print(genquestionlist[i])
    time.sleep(2)
    print("Now answer question!")
    useraskSTT()