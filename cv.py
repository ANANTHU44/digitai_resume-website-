import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title=" Ananthu k s",page_icon=":heart_on_fire:",layout="wide",initial_sidebar_state="expanded")
def load_lottieurl(url):
   r= requests.get(url)
   if r.status_code != 200 :
      return None
   return r.json()
img_cont1=Image.open(r"C:\Users\anant\Downloads\20220908170633_IMG_5313 (1).jpg")
lts="https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
lts1="https://lottie.host/51b154e1-df22-473a-a0e1-13c96883d539/jyCJY0Wos7.json"
lts2="https://lottie.host/0b4926f6-9d89-4e5d-ae24-17ba789878c7/TjTuepPqyP.json"
with st.container():
  left_column,right_column = st.columns((3,1))
  with left_column:
    
   st.subheader("Hi I am Ananthu k s :wave:")
   st.title("Data Analyst from india")
   
   st.write("Dynamic and skilled data scientist with comprehensive knowledge and expertise in diverse machine learningalgorithms. Seeking a position on the Data Analytics team to apply my proficiency in Python programming, dataanalysis, and machine learning techniques. Committed to delivering insightful and actionable reports, I aim tocontribute to complex reporting tasks, generating valuable information for customers")
   st.write("---")
   st.write("[ Visit my linked in profile>](https://www.linkedin.com/in/ananthu-k-s/)")
   st.write("[Visit my github profile](https://github.com/ANANTHU44)")
  with right_column:
     st.image(img_cont1,width=200)
    
with st.container():
   st.write("---")
   left_column,right_column = st.columns(2)
   with left_column:
     st.header("What I do")
     st.write("##")
     st.subheader("Experience:")
     st.write("         *Data Science Intern at Luminar Technolab")
     st.write("         *Developed proficiency in Python programming language and data analytics libraries (Numpy, Pandas, Scikit-learn, Matplotlib & Seaborn).")
     st.write("         *Learned data preprocessing and machine learning model building.")
     st.write("         *Worked with ML algorithms like KNN, SVM, Naive-Bayes, Decision Tree, Random Forest, Ada Boost, Gradient Boost, XG Boost, Linear Regression & Multiple linear Regression.")
     
   with right_column:
     st_lottie(lts,height=300,key="coding")
     
with st.container():
    left_column,right_column = st.columns(2)
    with left_column:
     st.write("##")
     st.subheader("Education:")
     st.write("  *Bachelor of Arts in Economics from Calicut University with a grade of B+.")
     st.write("  *Secondary School Leaving Certificate (SSLC) from Lourde Matha Higher Secondary School Mangalam Dam with 99%.")
     st.write("  *Plus Two (Commerce, Statistics) from Lourde Matha Higher Secondary School Mangalam Dam with 85.75%.")
    with right_column:
     st_lottie(lts1,height=300,key="cod")
with st.container():
    left_column,right_column = st.columns(2)
    with left_column:
     st.write("##")
     st.subheader("Skills:")
     st.write("*Proficient in Python programming.")
     st.write("*Experienced with data analysis and visualization using Pandas, Seaborn, and Matplotlib.")
     st.write("*Knowledgeable in a variety of machine learning algorithms, including Simple Linear Regression, Ensemble models, Regression algorithms, K-means clustering algorithm, and Principal Component Analysis (PCA).")
     st.write("*Skilled in SQL for data manipulation and retrieval.")
     st.write("*Strong communication skills.")
     st.write("*Customer service expertise.")
    
    with right_column:
     st_lottie(lts2,height=300,key="codi")
