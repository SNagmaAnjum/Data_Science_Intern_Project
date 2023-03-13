import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resourses")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "images.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "mcd.csv")

st.title("Dashboard - McDonald's Data")

img = image.imread(IMAGE_PATH)
st.image(img)
st.header("About Dataset")

st.text("McDonald's dataset contains information about ech product in the McDonald's menu.")
st.text('''It gives information about the proteins, calories, energy, sugar levels, etc.
in each and every product in the McDonald's menu.''')



df = pd.read_csv(DATA_PATH)
st.dataframe(df)

tab1, tab2,tab3,tab4,tab5,tab6= st.tabs(["Energy", "Protein","Total_fat","Carbs","Added_sugar","Serving_size"])

with tab1:
   st.subheader("Graph between Energy and name of food")
   fig_2 = px.scatter(x=df['name'], y=df["energy"])
   tab1.plotly_chart(fig_2, use_container_width=True)

with tab2:
   st.subheader("Graph between Protein and name of food")
   fig_2 = px.scatter(x=df['name'], y=df["protein"])
   tab2.plotly_chart(fig_2, use_container_width=True)


with tab3:
   st.subheader("Graph between Total_fat and name of food")
   fig_2 = px.scatter(x=df['name'], y=df["total_fat"])
   tab3.plotly_chart(fig_2, use_container_width=True)


with tab4:
   st.subheader("Graph between Carbs and name of food")
   fig_2 = px.scatter(x=df['name'], y=df["carbs"])
   tab4.plotly_chart(fig_2, use_container_width=True)


with tab5:
   st.subheader("Graph between Added sugar name of food")
   fig_2 = px.scatter(x=df['name'], y=df["added_sugar"])
   tab5.plotly_chart(fig_2, use_container_width=True)


with tab6:
   st.subheader("Graph between Serving_size and name of food")
   fig_2 = px.scatter(x=df['name'], y=df["serving_size"])
   tab6.plotly_chart(fig_2, use_container_width=True)

food=st.selectbox("select the Name of food:",df['name'].unique())
idx = df.index[df["name"]==food][0]

st.write(df.iloc[idx],column_width="auto")
ing = df.loc[idx,"ingredients"]
st.subheader("Ingredients:")
st.markdown(ing)

allergy=df.loc[idx,'allergy']
st.subheader("Allergy for the selected food:")
st.markdown(allergy)

des=df.loc[idx,'description']
st.subheader("Description for the selected food:")
st.markdown(des)




