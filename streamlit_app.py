
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('internship_program_data.csv')

st.title('Internship Program Dashboard')

st.sidebar.header('Filters')
deps = st.sidebar.multiselect('Departments', options=df['department'].unique(), default=list(df['department'].unique()))

filtered = df[df['department'].isin(deps)]

st.subheader('Completion Rate by Department')
summary = filtered.groupby('department')['completed'].mean().reset_index()
fig, ax = plt.subplots()
ax = sns.barplot(x='department', y='completed', data=summary)
ax.set_ylabel('Completion Rate')
ax.set_ylim(0,1)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
st.pyplot(fig)

st.subheader('Mentor Interactions vs Completion')
fig2, ax2 = plt.subplots()
sns.scatterplot(x='mentor_interactions_per_week', y='completed', data=filtered, alpha=0.3, ax=ax2)
sns.lineplot(x='mentor_interactions_per_week', y='completed', data=filtered, ci=None, estimator='mean', color='red', ax=ax2)
ax2.set_yticks([0,1])
ax2.set_yticklabels(['Dropped', 'Completed'])
st.pyplot(fig2)
