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
image = None
for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        use_latex = st.checkbox("Use LaTeX input", key = f'lip{i+1}')
        use_image = st.checkbox("Use Image", key = f'useimage{i+1}')

        if use_latex:
            option_input = st.text_area(f"Option {i+1}:", key=f"op{i+1}")
            option_text = st.latex(option_input)
        else:
            option_input = st.text_area(f"Option {i+1}:", key=f"op{i+1}")
            option_text = option_input
            st.write(option_text)

        if use_image:
            image = st.file_uploader(f"Add an image to Option {i+1}", type=["jpg", "jpeg", "png"], key = f"op{i+1}img")
            image_path = image.name

        else:
            image_path = None

        correct_answer = st.checkbox("Correct Answer: ", key=f"c{i+1}")
        options[f"Option {i+1}"] = {"option": option_input, "image": image_path, 'answer': correct_answer, 'latex': use_latex, "has_image" : use_image }


# # Create a button to submit the options
if st.button("Submit Options"):
    data = {"question": {"text": question, "image": question_image}, "options": options}
    st.write(data)
    with open('data.json', "w") as f:
        json.dump(data, f)
        # st.write("JSON data written to file:",data.json)
