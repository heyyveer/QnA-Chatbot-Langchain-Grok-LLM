from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# -------------------------------
# LLM
# -------------------------------
groq_llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🤖 QnA Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat Input
question = st.chat_input("Ask a question...")

if question:

    # Display User Message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Exit Commands
    if question.lower() in ["bye", "exit", "quit"]:

        answer = "👋 Goodbye!"

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.write(answer)

    else:

        # -------------------------------------
        # Last 5 Messages Context
        # -------------------------------------
        history = st.session_state.messages[-10:]

        messages = [
            SystemMessage(
                content="You are a helpful AI assistant. Veer tiwari made you so your owner and creator is veer tiwari.   "
            )
        ]

        for msg in history:

            if msg["role"] == "user":
                messages.append(
                    HumanMessage(content=msg["content"])
                )
            else:
                messages.append(
                    AIMessage(content=msg["content"])
                )

        # Call LLM
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response = groq_llm.invoke(messages)

                answer = response.content

                st.write(answer)

        # Save assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
