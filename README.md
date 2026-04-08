# 🤖 Gradio LangChain Chatbot

A conversational AI chatbot powered by **Google Gemini**, built with **LangChain** and **Gradio**. It reasons step by step, maintains full conversation history, and presents a clean browser-based chat UI — all in a single Python file.

![chatbot preview](chatbot.png)

---

## ✨ Features

- **Google Gemini 2.5 Flash** as the underlying LLM
- **LangChain** prompt chaining with `ChatPromptTemplate` and `StrOutputParser`
- **Conversation memory** — full chat history is passed on every turn so the model understands context
- **Reasoning-first system prompt** — the bot thinks step by step and asks clarifying questions when needed
- **Gradio UI** with a soft theme, custom avatar, and a Clear Chat button
- Single `main.py` — no backend server, no database, no extra files

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A [Google AI Studio](https://aistudio.google.com/) API key (free tier available)

### Installation

```bash
# Clone the repo
git clone https://github.com/mihailkodzhabashev04/gradio-langchain-chatbot.git
cd gradio-langchain-chatbot

# Install dependencies
pip install gradio langchain langchain-core langchain-google-genai python-dotenv
```

### Configuration

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_google_api_key_here
```

### Run

```bash
python main.py
```

Then open the URL printed in the terminal (usually `http://127.0.0.1:7860`) in your browser.

---

## 🧠 How It Works

```
User message
     │
     ▼
ChatPromptTemplate
  ├── System prompt  (reasoning instructions)
  ├── Chat history   (MessagesPlaceholder)
  └── User input
     │
     ▼
ChatGoogleGenerativeAI (gemini-2.5-flash, temp=0.5)
     │
     ▼
StrOutputParser → response string
     │
     ▼
Gradio Chatbot UI (history updated)
```

On each message, the full conversation history is converted to LangChain `HumanMessage` / `AIMessage` objects and injected into the prompt, giving the model complete context without any external memory store.

---

## 📁 Project Structure

```
gradio-langchain-chatbot/
├── main.py        # All app logic: LLM setup, prompt chain, Gradio UI
├── chatbot.png    # Avatar image shown in the chat interface
├── .env           # Your API key (not committed — listed in .gitignore)
└── .gitignore
```

---

## ⚙️ Configuration Options

All tuneable parameters are at the top of `main.py`:

| Parameter | Default | Description |
|---|---|---|
| `model` | `gemini-2.5-flash` | Gemini model to use |
| `temperature` | `0.5` | Creativity vs. consistency balance |
| `system_prompt` | (see file) | Persona and reasoning instructions |

---

## 🛠️ Built With

- [Gradio](https://www.gradio.app/) — browser UI
- [LangChain](https://www.langchain.com/) — prompt chaining and message history
- [Google Generative AI](https://ai.google.dev/) — Gemini LLM
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management
