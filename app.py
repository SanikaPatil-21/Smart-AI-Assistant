import streamlit as st

# Import the assistant's response function.
from assistant import assistant_response


# --------------------------------------------------
# 1. Configure the web page
# --------------------------------------------------

st.set_page_config(
    page_title="Smart AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# 2. Display the title and introduction
# --------------------------------------------------

st.title("🤖 Smart AI Assistant")

st.write(
    "Welcome! I can answer predefined questions and "
    "perform basic tasks using Python."
)

st.info(
    "Try asking about AI, checking the date and time, "
    "performing calculations, or opening websites."
)


# --------------------------------------------------
# 3. Initialize the conversation history
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I am your Smart AI Assistant. "
                "Type 'help' to see what I can do."
            )
        }
    ]


# --------------------------------------------------
# 4. Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# 5. Accept user input
# --------------------------------------------------

user_input = st.chat_input("Type your message here...")


# --------------------------------------------------
# 6. Process the user's request
# --------------------------------------------------

if user_input:

    # Display and save the user's message.
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Get a response from the assistant logic.
    reply = assistant_response(user_input)

    # Save the assistant's response.
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    # Display the response.
    with st.chat_message("assistant"):
        st.write(reply)


# --------------------------------------------------
# 7. Clear the conversation
# --------------------------------------------------

if st.button("Clear Chat"):

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Chat cleared! How can I help you?"
            )
        }
    ]

    st.rerun()


# --------------------------------------------------
# 8. Display available features
# --------------------------------------------------

with st.expander("Available Commands"):

    st.write(
        """
        - `hello` — Get a greeting.
        - `what is ai` — Learn about AI.
        - `what is python` — Learn about Python.
        - `what is machine learning` — Learn about ML.
        - `what is today's date` — Check the date.
        - `what time is it` — Check the time.
        - `calculate 25 * 4` — Perform a calculation.
        - `open youtube` — Open YouTube.
        - `search Python tutorials` — Search the web.
        - `help` — Show available commands.
        - `exit` — Exit the terminal assistant.
        """
    )