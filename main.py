from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
    You are an AI chatbot.
    You think step by step and use reasoning to form accurate answers.
    When appropriate, you ask clarifying questions before answering.
    You respond from your own point of view in a clear, calm, and helpful tone.
    Your goal is to help the user understand ideas, not just receive answers.
    """

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()

print("Hi, I am Mihail's chatbot, how can I help you today?")

history = []
def chat(user_input, hist):

    langchain_history = []
    for item in hist:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'system':
            langchain_history.append(AIMessage(content=item['content']))

    response = chain.invoke({"input": user_input, "history": langchain_history})


    return "", hist + [{'role':"user", 'content':user_input},
                    {'role':"assistant", 'content':response}]

def clear_chat():
    return "", []


page = gr.Blocks(
    title="Mihail's chatbot",
    )

with page:
    gr.Markdown(
        """
        # Chat with Mihail's chatbot
        Welcome to your personal conversation with Mihail's chatbot!
        """
    )

    chatbot = gr.Chatbot(avatar_images=[None, 'chatbot.png'],
                         show_label=False)

    msg = gr.Textbox(placeholder="Ask me anything...",
                     show_label=False)

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat,
                outputs=[msg, chatbot])


page.launch(
    theme=gr.themes.Soft(),
)