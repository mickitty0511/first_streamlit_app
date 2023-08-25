import streamlit as st

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect(
     "Pick some fruits:"
     , list(my_fruit_list.index)
     , ['Avocado', 'Strawberries']     
)
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

# New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input(
     'What fruit would you like information about?'
     , 'Kiwi'
)
st.write(
     'The user entered'
     , fruit_choice
) # display a text on screen

import requests as req
fruityvice_response = req.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response.json()) # just writes the data to the screen

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

import snowflake.connector as sf
my_cnx = sf.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

fruit_ingest = st.text_input(
     'What fruit would you like to add'
     , placeholder = 'Input One of your fruit!'
)

st.write('Thanks for adding ', fruit_ingest)