import streamlit as st
from crewai_tools import FirecrawlSearchTool

# Set your Firecrawl API key
FIRECRAWL_API_KEY = "fc-005b2f5f027f46edbadbe2c77cde6206"

# Initialize the Firecrawl search tool
web_search_tool = FirecrawlSearchTool(api_key=FIRECRAWL_API_KEY)

st.title("Firecrawl API Connection Check")

user_question = st.text_input("Enter your search question:")

if st.button("Search"):
    if user_question:
        st.info(f"Searching Firecrawl for: '{user_question}'...")
        try:
            results = web_search_tool.run(user_question)
            if results:
                st.subheader("Search Results:")
                st.write(results)
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a search question.")
