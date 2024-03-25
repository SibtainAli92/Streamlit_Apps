import streamlit as st
import  pandas as pd
import  numpy as np
 
# adding tittle of your app
st.title("My First Testing App for Codanics course (6 month long)")

# adding simple test
st.write('Here is a simple text')

# user input
number = st.slider("Pick a number", 0, 100, 10)

# print the text of number 
st.write(f'You selected: {number}')

# adding a button
if st.button("Greething"):
    st.write('Hi, hello there')
else:
    st.write('Goodbye')

# add radio button with options
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

# print the text of genere
st.write(f'You selected: {genre}')

# add a drop down list 
# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# add a drop down list on the left sidebar
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

# add your whatsapp number
st.sidebar.text_input("Enter your whatsapp number")

# add a file uploader 
uploaded_file = st.sidebar.file_uploader('Choose a CSV file', type='csv')

# create a line plot
# Plotting
data = pd.DataFrame({
  'first column': list(range(1, 11)),
  'second column': np.arange(number, number + 10)
})
st.line_chart(data)