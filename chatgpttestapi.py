from openai import OpenAI
client = OpenAI()

# prompt = """You are the following technological tool: Interview Simulator: Create a tool for job interview practice where users can simulate interviews by speaking their responses to common interview questions. The tool would transcribe the user's responses, provide feedback, and generate synthesized speech for the interviewer's questions.

# The interviewer is {a1} years of age and would like to be asked {a2} questions. The interview is for a {a3} position at the organisation called {a4}. The interview will be held in the country {a5}

# After each question asked you will receive an answer. After asking all questions and receiving their respective answers after each question asked, you will give feedback on the user's response based on the nature of the interview to improve their chances of success on an interview like this, during feedback you will provide strengths and weaknesses of their responses, referring to specific examples from their responses."""
#prompt = "hey can you help me with some math?"
    
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {f"role": "system", "content": """You are the following technological tool: Interview Simulator: Create a tool for job interview practice where users can simulate interviews by speaking their responses to common interview questions. The tool would transcribe the user's responses, provide feedback, and generate synthesized speech for the interviewer's questions.

The interviewer is {a1} years of age and would like to be asked {a2} questions. The interview is for a {a3} position at the organisation called {a4}. The interview will be held in the country {a5}

After each question asked you will receive an answer. After asking all questions and receiving their respective answers after each question asked, you will give feedback on the user's response based on the nature of the interview to improve their chances of success on an interview like this, during feedback you will provide strengths and weaknesses of their responses, referring to specific examples from their responses."""},
  ]
)

print(completion.choices[0].message.content)

# from pathlib import Path
# from openai import OpenAI
# client = OpenAI()

# speech_file_path = Path(__file__).parent / "speech.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="alloy",
  # input=)

# response.stream_to_file(speech_file_path)