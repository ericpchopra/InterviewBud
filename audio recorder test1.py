import pyaudio
import wave
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10  # Duration to record in seconds

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []
start_time = time.time()

while (time.time() - start_time) < RECORD_SECONDS:
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a file
wf = wave.open("recorded_audio.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("Audio saved as recorded_audio.wav")
