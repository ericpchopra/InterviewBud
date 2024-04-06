import os
from pathlib import Path
from openai import OpenAI
import pygame
import pyaudio
import wave
import soundfile as sf

client = OpenAI()

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Navigate to the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Create a new text file in the parent directory
file_path = os.path.join(parent_directory,'InterviewBud','resources', 'initial questions.txt')
questions = ['What is your age? ','How many questions would you like in your interview? (maximum 7) ', 'For what position are you taking this interview? ','For what organisation is this interview being held for? ','Which country is this interview being held?']
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

print(genquestionlist)



# #######################################     text to speech module      ########################################


# speech_file_path = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="shimmer",
#   input=completion.choices[0].message.content
# )

# response.stream_to_file(speech_file_path)

# # Initialize pygame mixer
# pygame.mixer.init()

# # Load the audio file
# audio_file = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS.mp3"
# pygame.mixer.music.load(audio_file)

# # Play the audio
# pygame.mixer.music.play()

# # Wait while the audio is playing
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# # Stop the playback
# pygame.mixer.music.stop()

# # Delete the audio file
# os.remove(audio_file)


# ############################### speech to text module ##########################################
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5  # Adjust this value for the desired duration of the recording

# audio = pyaudio.PyAudio()

# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                     rate=RATE, input=True,
#                     frames_per_buffer=CHUNK)

# print("Recording...")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("Finished recording.")

# stream.stop_stream()
# stream.close()
# audio.terminate()

# # Save the recorded audio to a WAV file
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"resources",'recorded_audio3.wav'))
# wf = wave.open(file_path, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(audio.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

# # Convert the WAV file to MP3
# mp3_file_path = os.path.splitext(file_path)[0] + '.mp3'
# audio_data, _ = sf.read(file_path)
# sf.write(mp3_file_path, audio_data, RATE)

# print("Audio saved as:", mp3_file_path)
# print(os.path.abspath(os.path.join(os.path.dirname(__file__),'resources','recorded_audio3.wav')))

# # =======================speech to text component=======================================
# audio_file= open(os.path.abspath(os.path.join(os.path.dirname(__file__),"resources",'recorded_audio3.wav')), "rb")
# transcription = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(transcription.text)
