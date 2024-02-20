import streamlit as st
import csv

def main():
    st.title("CSV Viewer with Streamlit")

    # Upload CSV file through Streamlit widget
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file using the uploaded file handler
        csv_content = uploaded_file.read()

        # Decode bytes to string and split the lines
        csv_lines = csv_content.decode('utf-8').splitlines()

        # Use Streamlit to display the CSV content
        st.table(csv.reader(csv_lines))

if __name__ == "__main__":
    main()
