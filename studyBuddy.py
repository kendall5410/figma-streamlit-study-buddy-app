import streamlit as st
from PIL import Image
import google.generativeai as genai

# Add a logo to the app
st.image('https://previews.123rf.com/images/surfupvector/surfupvector1905/surfupvector190500088/121813892-machine-learning-line-icon-robot-in-graduation-cap-artificial-intelligence-concept-vector.jpg', width=200)

# Create a title for the app
st.title('StudyBuddy AI')

# Create an about section
st.markdown(
  'Your personal tutor that makes studying easier !\n\n'
  'StudyBuddy AI is an application for college students, offering personalized solutions, AI tutoring, and tools to boost academic performance and enhance learning efficiency. It\'s your ultimate companion for navigating college academics successfully.'
)
# Create a title after the markdown section
st.title('How To Study with StudyBuddy')

# Create a directions section
st.markdown('To Utilize StudyBuddy you must select the topic that you want to cover/get help over.  Once selected, you can drag and drop or browse through files to upload documents for StudyBuddy to analyze. A text input section is also provided for the user to input any instructions, questions etc that your studybuddy might need to know. Once submitted, your studyBuddy will present to you a responce to your inputs.')

# Create a selectbox that allows the user to choose a subject
subject = st.selectbox(
  'What Subject can your StudyBuddy help with?',
  ('Math','Science','Writing ','Computer Science','Foreign Language ','Research ',''),
  help='Help message goes here'
)

# Create a submit button
submit_button = st.button("Submit")

# Check if the user has clicked the submit button
if submit_button:
  # Provide help based on the user's selection
  if subject == 'Math':
    # Provide help with math
    pass
  elif subject == 'Science':
    # Provide help with science
    pass
  elif subject == 'Writing':
    # Provide help with writing
    pass
  elif subject == 'Computer Science':
    # Provide help with computer science
    pass
  elif subject == 'Foreign Language':
    # Provide help with foreign language
    pass
  elif subject == 'Research':
    # Provide help with research
    pass
  else:
    # Provide help with a general topic
    pass

  # Display the selected subject
  st.write(f"You selected {subject}.")

  # Create a file uploader that allows the user to upload an image
file = st.file_uploader("Upload a picture as a prompt")

  # Check if the user has uploaded an image
if file is not None:
  #Open the image
  img = Image.open(file)

  # Display the image on the app
  st.header("My prompt image: ")
  st.image(img)

  # Create a text input box that allows the user to describe the image
  description = st.text_input("message:")

  # Configure the Generative AI API
  genai.configure(api_key='AIzaSyB0GCONS3DqUjCGjUpu4LIN2iHeUfN1mm0')

  # # Create a model
  model = genai.GenerativeModel('gemini-pro-vision')

  # # Generate a description of the image
  response = model.generate_content(['Describe the subject of this photo', img])

  # # Wait for the API to finish generating the description
  response.resolve()

  # # Display the description of the image on the app
  st.header("This is the response: ")
  st.write(response.text)

  