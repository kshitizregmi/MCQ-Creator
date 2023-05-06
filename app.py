import streamlit as st
import json

st.set_page_config(layout="wide")

# Set up the Streamlit app
st.title("Interview Optimization MCQ")

question = st.text_input("Enter the question: *", key='question')

# Create a textbox to input the question
with st.expander("Upload Image (optional)", expanded=False):
    question_image = st.file_uploader("Upload an image for the question", type=["jpg", "jpeg", "png"])


# Create four columns to hold the options and image buttons
col1, col2, col3, col4 = st.columns(4)

# Create a text input and image upload button for each option
options = {f"Option {i+1}": {"option": "", "image": "", 'answer': False, 'latex': False, "has_image" : False } for i in range(4)}
for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        options[f"Option {i+1}"]["latex"] = st.checkbox("Use LaTeX input", key=f'lip{i+1}')
        options[f"Option {i+1}"]["has_image"] = st.checkbox("Use Image", key=f'useimage{i+1}')
        if options[f"Option {i+1}"]["latex"]:
            option_input = st.text_area(f"Option {i+1}:", key=f"op{i+1}")
            option_text = st.latex(option_input)
        else:
            option_input = st.text_area(f"Option {i+1}:", key=f"op{i+1}")
            option_text = option_input
            st.write(option_text)

        
        options[f"Option {i+1}"]["option"] = option_input

        if options[f"Option {i+1}"]["has_image"]:
            name = st.file_uploader(f"Add an image to Option {i+1}", type=["jpg", "jpeg", "png"], key=f"op{i+1}img")
            if name:
                name = name.name
            else:
                name = None
            options[f"Option {i+1}"]["image"] = name
        else:
            options[f"Option {i+1}"]["image"] = None

        options[f"Option {i+1}"]["answer"] = st.checkbox("Correct Answer: ", key=f"c{i+1}")


explatex = st.checkbox("Use LaTeX input", key='latexexp')
explanation = st.text_area(f"Explanation: \n ", key = "exp")
if explatex:
    st.latex(explanation)
else:
    st.write(explanation)




# Create a button to submit the options
if st.button("Submit Options"):
    data = {"question": {"text": question, "image": question_image}, "options": options, "explanation": {'text': explanation, 'latex': explatex}}
    st.write(data)
    with open('data.json', "w") as f:
        json.dump(data, f)
