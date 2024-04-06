import pyaudio
import wave
import soundfile as sf
import os
from openai import OpenAI

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # Adjust this value for the desired duration of the recording
numberofquestions = 3
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)


print("Recording...")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording user input.")

stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
uinputpath = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\STT user speech\\STT AUDIO.wav"
wf = wave.open(uinputpath, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

    

# Convert the WAV file to MP3
# mp3_file_path = os.path.splitext(file_path)[0] + '.mp3'
# audio_data, _ = sf.read(file_path)
# sf.write(mp3_file_path, audio_data, RATE)

# print("Audio saved as:", mp3_file_path)
# print(os.path.abspath(os.path.join(os.path.dirname(__file__),'resources','recorded_audio3.wav')))

# =======================speech to text component=======================================
# client = OpenAI()

# audio_file= open(os.path.abspath(os.path.join(os.path.dirname(__file__),"resources",'recorded_audio3.wav')), "rb")
# transcription = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(transcription.text)


