from pathlib import Path
from openai import OpenAI

import os

client = OpenAI()

Gquestionlist = ['1. Tell me about a challenging project you worked on as a software engineer and how you overcame obstacles to successfully complete it.', '2. How do you stay updated with the latest technologies and trends in the software engineering field?', '3. Can you walk me through your experience with developing applications for iOS and MacOS platforms?', '4. How do you approach problem-solving when working on a complex coding issue?', '5. Describe a situation where you had to work within a team to deliver a software project. What was your role and how did you ensure successful collaboration?', '6. How do you ensure the security and integrity of the code you write when developing software applications?', "7. Why do you want to work specifically at Apple and how do you see yourself contributing to the company's success as a software engineer?"]

#speech_file_path = Path(__file__).parent / "TTS.mp3"

for i in Gquestionlist:
    speech_file_path = f"C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS generated questions\\TTS_question_{Gquestionlist.index(i)+1}.mp3"
    response = client.audio.speech.create(
      model="tts-1",
      voice="shimmer",
      input= i
    )
    response.stream_to_file(speech_file_path)



# # Initialize pygame mixer
# pygame.mixer.init()

# # Load the audio file
# audio_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'TTS.mp3'))
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

