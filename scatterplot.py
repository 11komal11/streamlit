import streamlit as st
import matplotlib.pyplot as plt

study_hours = [1,2,2.5,3,3.5,4,5,6,6.5,7]
exam_scores = [40,50,55,60,62,65,70,78,80,85]

fig, ax = plt.subplots()
ax.scatter(study_hours, exam_scores, color = "green")
ax.set_title("Study hours vs exam score")
ax.set_xlabel("Study hours")
ax.set_ylabel("Exam score (%)")

st.pyplot(fig)