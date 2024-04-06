import pyaudio
import wave
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAIT_SECONDS = 2

def record_audio(n):
    audio = pyaudio.PyAudio()

    for i in range(n):
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        print("Recording...")

        frames = []
        frames_recorded = 0

        # Record until the desired number of frames is reached
        while frames_recorded < int(RATE / CHUNK * RECORD_SECONDS):
            data = stream.read(CHUNK)
            frames.append(data)
            frames_recorded += CHUNK

        print("Finished recording user input.")

        stream.stop_stream()
        stream.close()

        # Save the recorded audio to a WAV file
        directory = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\STT_user_speech\\"
        filename = f"STT_AUDIO{i + 1}.wav"
        uinputpath = directory + filename
        wf = wave.open(uinputpath, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        time.sleep(WAIT_SECONDS)

    audio.terminate()

n = 3  # Set the number of recordings
record_audio(n)
