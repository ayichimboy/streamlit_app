import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Title and Introduction
st.title("Grocery Spending Tracker")
st.write("Track your grocery expenses over time by entering the date and amount spent.")

# Step 2: Initialize or Load Data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Amount"])

# Step 3: Input Form
with st.form("grocery_form"):
    st.write("Enter your grocery expense:")
    date = st.date_input("Date of purchase:")
    amount = st.number_input("Amount spent ($):", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        # Create a DataFrame from the new input
        new_data = pd.DataFrame({"Date": [date], "Amount": [amount]})
        # Concatenate and ensure consistent Date format
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.session_state.data["Date"] = pd.to_datetime(st.session_state.data["Date"])
        st.success("Expense added successfully!")

# Step 4: Display Data
st.write("### Your Grocery Expenses")
if not st.session_state.data.empty:
    st.dataframe(st.session_state.data)
else:
    st.write("No expenses recorded yet.")

# Step 5: Visualization
if not st.session_state.data.empty:
    st.write("### Expense Over Time")
    # Ensure Date column is datetime and sorted
    st.session_state.data["Date"] = pd.to_datetime(st.session_state.data["Date"])
    st.session_state.data.sort_values("Date", inplace=True)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(st.session_state.data["Date"], st.session_state.data["Amount"], marker="o", linestyle="-")
    plt.title("Grocery Spending Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Amount Spent ($)", fontsize=14)
    plt.grid(True)
    st.pyplot(plt)
else:
    st.write("No data available for visualization.")
