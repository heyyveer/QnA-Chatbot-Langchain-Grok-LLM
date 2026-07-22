# 🤖 Groq Q&A Chatbot

A simple AI-powered Q&A chatbot built with **Streamlit**, **LangChain**, and **Groq LLM**. The application provides a ChatGPT-like interface where users can ask questions and receive intelligent responses while maintaining recent conversation context.

---

## 🚀 Features

* 💬 Interactive chat interface using Streamlit
* 🤖 Powered by Groq's **Llama 3.3 70B Versatile** model
* 🧠 Maintains the last **5 messages** as conversation context
* ⚡ Fast inference using Groq API
* 📜 Chat history stored using Streamlit Session State
* 👋 Supports exit commands (`bye`, `exit`, `quit`)
* ⏳ Loading spinner while generating responses

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* python-dotenv

---

## 📂 Project Structure

```text
QnA-Chatbot/
│
├── app.py               # Main Streamlit application
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/qna-chatbot.git
cd qna-chatbot
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally and can be accessed in your browser.

---

## 💻 Usage

1. Enter your question in the chat input.
2. The chatbot sends the last **5 messages** as context to the LLM.
3. The AI generates a contextual response.
4. Continue chatting naturally.
5. Type `bye`, `exit`, or `quit` to end the conversation.

---

## 📌 Conversation Memory

The chatbot maintains the **last five chat messages** in the context window before sending the request to the LLM. This enables follow-up questions while keeping token usage efficient.

Example:

```text
User: What is Python?
AI: Python is a programming language.

User: Who created it?
AI: Guido van Rossum.

User: When?

AI: Python was first released in 1991.
```

---

## 📦 Requirements

```text
streamlit
langchain
langchain-groq
python-dotenv
```

Or install directly:

```bash
pip install streamlit langchain langchain-groq python-dotenv
```

---

## 🔮 Future Improvements

* Conversation summarization for long chats
* Streaming responses
* File upload (PDF, DOCX, CSV)
* Multiple LLM selection
* Dark/Light theme toggle
* Persistent chat history (SQLite/PostgreSQL)
* User authentication
* Voice input and text-to-speech

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it for personal or commercial purposes.

---

## 👨‍💻 Author

Developed using **Python**, **Streamlit**, **LangChain**, and **Groq** to demonstrate conversational AI with contextual memory.
