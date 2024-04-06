# Specify the path to the text file
file_path = "C:\\Users\\Admin\\Documents\\InterviewBud\\resources\\initial questions.txt"  # Update this with the path to your text file

# Open the text file in read mode
with open(file_path, 'r') as file:
    # Read the third line of the file
    lines = file.readlines()
    
    third_line = lines[1]
    print("Text in the third line:", third_line.strip())
    
