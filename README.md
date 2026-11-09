# Smart AI Assistant

## 1. Project Overview

The Smart AI Assistant is a Python-based application that answers predefined questions and performs basic tasks using simple rule-based logic.

The application provides an interactive web interface built with Streamlit, allowing users to communicate with the assistant through a chat window.

## 2. Objectives

- Develop a simple interactive assistant using Python.
- Answer common questions about Artificial Intelligence, Python, and Machine Learning.
- Display the current date and time.
- Perform basic mathematical calculations.
- Open websites and search the web.
- Provide a user-friendly chatbot interface.

## 3. Technologies Used

- **Python:** Application logic and task processing.
- **Streamlit:** Interactive web interface.
- **Datetime:** Date and time functionality.
- **AST:** Safe parsing of supported mathematical expressions.
- **Webbrowser:** Opening websites and web searches.

## 4. Features

1. Greeting responses.
2. Answers to predefined questions.
3. Current date and time.
4. Basic mathematical calculations.
5. Website-opening commands.
6. Web-search functionality.
7. Help command for available features.
8. Interactive chat interface.
9. Chat history and clear-chat functionality.

## 5. Project Structure

```text
Smart_AI_Assistant/
├── assistant.py
├── app.py
├── requirements.txt
└── README.md
```

## 6. Installation

### Prerequisites

- Python installed on your computer.
- Visual Studio Code or another Python editor.

### Install Dependencies

Open the terminal inside the project folder and run:

```bash
python -m pip install -r requirements.txt
```

## 7. How to Run

Navigate to the project folder in your terminal and run:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local web address. Open that address in your browser to use the assistant.

## 8. Example Commands

| Command | Function |
|---|---|
| `hello` | Displays a greeting |
| `what is ai` | Explains Artificial Intelligence |
| `what is python` | Explains Python |
| `what is machine learning` | Explains Machine Learning |
| `what is today's date` | Displays the current date |
| `what time is it` | Displays the current time |
| `calculate 25 * 4` | Calculates a mathematical expression |
| `open youtube` | Attempts to open YouTube |
| `search Python tutorials` | Searches the web |
| `help` | Shows available commands |

## 9. Testing

The application was tested using common questions, date and time requests, mathematical calculations, website-opening commands, and web searches.

The tested features worked as expected in the local environment.

## 10. Limitations

- Responses to general questions are predefined.
- The application does not use a large language model or an external AI API.
- Its ability to answer questions is limited to the implemented rules.
- Website-opening and search features depend on the local environment and internet connectivity.

## 11. Conclusion

The Smart AI Assistant demonstrates how Python can be used to build a simple task-oriented assistant with an interactive web interface. The project provides a foundation for future improvements, including AI-powered responses, speech recognition, and additional automation features.
