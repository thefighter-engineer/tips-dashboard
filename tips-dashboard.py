import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Tips Dashboard", layout="wide", initial_sidebar_state="expanded")

# Load data
df = pd.read_csv('tips.csv')

# Sidebar
st.sidebar.header("Restaurant Tips Dashboard")
st.sidebar.image('tips.png')
st.sidebar.write("Welcome to the Restaurant Tips Dashboard! Here, you can explore various insights and trends to help you make informed decisions about dining experiences. Enjoy your visit!")

# Filters in Sidebar
st.sidebar.write("Filter your data:")
cat_filter = st.sidebar.selectbox("Categorical Filtering", ["None", "sex", "smoker", "day", "time"], index=0)
num_filter = st.sidebar.selectbox("Numerical Filtering", ["None", "total_bill", "tip"], index=0)

if num_filter != "None":
    min_value, max_value = st.sidebar.slider(f"Filter {num_filter}", float(df[num_filter].min()), float(df[num_filter].max()), 
                                             (float(df[num_filter].min()), float(df[num_filter].max())))
    df = df[(df[num_filter] >= min_value) & (df[num_filter] <= max_value)]

pie_cat = st.sidebar.selectbox("Select Category for Pie Chart", ["sex", "smoker", "day", "time"], index=0)

st.sidebar.markdown("Made with ❤️ by [Yousef Abdalnasser](https://www.linkedin.com/in/youssef-abdalnasser-33705b262)")

# Main body

# Row A: Metrics
a1, a2, a3, a4 = st.columns(4)
a1.metric("Max Total Bill", f"${df['total_bill'].max():.2f}")
a2.metric("Max Tip", f"${df['tip'].max():.2f}")
a3.metric("Min Total Bill", f"${df['total_bill'].min():.2f}")
a4.metric("Min Tip", f"${df['tip'].min():.2f}")

# Row B: Scatter Plot
st.subheader("Total Bills vs Tips")
fig = px.scatter(df, x='total_bill', y='tip', 
                 color=df[cat_filter] if cat_filter != "None" else None,
                 size=df[num_filter] if num_filter != "None" else None)
st.plotly_chart(fig, use_container_width=True)

# Row C: Detailed Visualizations
st.header("Detailed Analysis")
c1, c2, c3 = st.columns((4, 3, 4))

# C1: Violin Plot (Distribution of Tips by Day)
with c1:
    st.markdown("Total Bill by Day")
    fig = px.bar(df, x='day', y='total_bill', color='day')
    st.plotly_chart(fig, use_container_width=True)
    

# C2: Pie Chart (Proportion of Tips by Category)
with c2:
    st.markdown(f"Proportion of Tips by {pie_cat.capitalize()}")
    fig = px.pie(df, names=pie_cat, values='tip', color=df[cat_filter] if cat_filter != "None" else None)
    st.plotly_chart(fig, use_container_width=True)

# C3: Box Plot (Total Bill by Category)
with c3:
    st.markdown("Distribution of Tips by Day")
    fig = px.violin(df, x='day', y='tip', color=df[cat_filter] if cat_filter != "None" else None, box=True, points="all")
    st.plotly_chart(fig, use_container_width=True)





