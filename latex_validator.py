import streamlit as st

# Add a checkbox to show the LaTeX input option
use_latex = st.checkbox("Use LaTeX input")

# If the checkbox is selected, show the LaTeX input area
if use_latex:
    st.subheader("Enter LaTeX text")
    latex_input = st.text_area("Insert LaTeX here...", height=200)

    # If the user inputs LaTeX text, store it as a string variable
    if latex_input:
        latex_string = str(latex_input)
        st.write("You entered:", latex_string)
        print(latex_string)



