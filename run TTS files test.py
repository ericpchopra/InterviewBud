import pygame
for i in range(7):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    audio_file = f"C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\TTS generated questions\\TTS_question_{i+1}.mp3"
    pygame.mixer.music.load(audio_file)

    # Play the audio
    pygame.mixer.music.play()

    # Wait while the audio is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop the playback
    pygame.mixer.music.stop()