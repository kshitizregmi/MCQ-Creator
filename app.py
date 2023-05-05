import streamlit as st
import json

st.set_page_config(layout="wide")

# Set up the Streamlit app
st.title("Interviw Optimization MCQ")

question = st.text_input("Enter the question: *", key='question')

# Create a textbox to input the question
with st.expander("Upload Image (optional)", expanded=False):
    question_image = st.file_uploader("Upload an image for the question", type=["jpg", "jpeg", "png"])


# Create four columns to hold the options and image buttons
col1, col2, col3, col4 = st.columns(4)

# Create a text input and image upload button for each option
options = {}
for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        option_input = st.text_input(f"Option {i+1}:", key=f"op{i+1}")
        if "\\" in option_input:
            option_text = st.latex(option_input)
        else:
            option_text = option_input
        image = st.file_uploader(f"Add an image to Option {i+1}", type=["jpg", "jpeg", "png"], key = f"op{i+1}img")
        correct_answer = st.multiselect(f"Option {i+1}: Correct answer? ", [True], key=f"opc{i+1}")
        if not correct_answer:
            correct_answer = [False]

        options[f"Option {i+1}"] = {"option": option_text, "image": image, 'answer': correct_answer}


# Create a button to submit the options
if st.button("Submit Options"):
    # Print the question and options to the console
    data = {"question": {"text": question, "image": question_image}, "options": options}
    st.write(json.dumps(data))