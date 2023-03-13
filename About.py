import streamlit as st
import webbrowser
st.title("Shaik Nagma Anjum")
st.subheader("Intern in Innomatics Research Labs")

tab1,tab2,tab3,tab4=st.tabs(["Education","Experience","Skills","Contact"])
with tab1:
    st.subheader("Education")
    st.markdown("I completed my :blue[B.Tech] in :blue[Electrical and Electronics Engineering] with  CGPA of 6.6 during 2011-2015. ")
    st.markdown("I completed my :blue[M.Tech] in :blue[Power Electronics] with  CGPA of 6.9 during 2015-2017.")

with tab2:
    st.subheader("Experience")
    st.markdown("I have worked as an :blue[Assistant Professor] in :blue[Ashoka Women’s Engineering College] for 2 years during July 2018-Aug2020")
    st.markdown("Due to my interest in I.T field, I wanted improve my skills and face challenges in Data Science... I started my Internship in :blue[Innomatics Research Labs] from Feb 2023")
    st.markdown("As a part of my internship in :blue[Innomatics Research Labs], i have done this project on web application using :blue[Streamlit]")

with tab3:
    st.subheader("Skills")
    st.markdown("Languages-Python")
    st.markdown("DataBase-MySQL")
    st.markdown("Machine Learning")
    st.markdown("Visualization Tool-Tableau")
    st.markdown("Web Application-Streamlit")

with tab4:
    st.subheader("Contact")
    st.write("My gmail nagmashaik6594@gmail.com")
    st.write("Linkedin https://www.linkedin.com/in/shaik-nagma-anjum/")
    st.write("Github https://github.com/SNagmaAnjum")