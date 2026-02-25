import streamlit as st
import requests

st.set_page_config(page_title="TinyLlama Chatbot")

st.title("💬 TinyLlama Local Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask something..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "tinyllama:latest",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )
                result = response.json()
                reply = result.get("response", "No response received")

            except Exception as e:
                reply = f"Error: {e}"

            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})