# ============================================================
# Project: Smart AI Assistant
# Language: Python
# Description: A simple assistant that answers questions
#              and performs basic tasks using Python rules.
# ============================================================

import datetime
import ast
import operator
import webbrowser
from urllib.parse import quote_plus


# ------------------------------------------------------------
# 1. Define predefined responses
# ------------------------------------------------------------

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! I am your Smart AI Assistant.",
    "hey": "Hey! What would you like me to do?",

    "what is ai": (
        "Artificial Intelligence (AI) is a field of computer "
        "science focused on creating systems that can perform "
        "tasks requiring human-like intelligence."
    ),

    "what is python": (
        "Python is a popular programming language known for "
        "its readable syntax and wide range of applications."
    ),

    "what is machine learning": (
        "Machine Learning is a branch of AI that enables "
        "computers to learn patterns from data."
    ),

    "who are you": (
        "I am a Smart AI Assistant built using Python. "
        "I can answer predefined questions and perform basic tasks."
    )
}


# ------------------------------------------------------------
# 2. Safely evaluate basic mathematical expressions
# ------------------------------------------------------------

# Only these mathematical operators are allowed.
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def calculate(expression):
    """Calculate a basic arithmetic expression safely."""

    def evaluate(node):
        # Handle numeric values.
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        # Handle arithmetic operations such as +, -, *, and /.
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            left = evaluate(node.left)
            right = evaluate(node.right)

            # Prevent excessively large exponent calculations.
            if isinstance(node.op, ast.Pow):
                if abs(right) > 10_000:
                    raise ValueError("Exponent is too large.")

                if isinstance(left, (int, float)) and abs(left) > 1_000_000:
                    raise ValueError("Base is too large.")

            result = allowed_operators[type(node.op)](left, right)

            # Keep results within reasonable limits.
            if isinstance(result, int) and result.bit_length() > 4096:
                raise ValueError("The result is too large.")

            if isinstance(result, float):
                if not __import__("math").isfinite(result):
                    raise ValueError("The result is too large.")

            return result

        # Handle expressions such as -5.
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_operators:
            return allowed_operators[type(node.op)](evaluate(node.operand))

        # Reject all unsupported expressions.
        raise ValueError("Unsupported mathematical expression.")

    try:
        tree = ast.parse(expression, mode="eval")
        return evaluate(tree.body)

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except (ValueError, TypeError, SyntaxError, OverflowError):
        return "Sorry, I could not calculate that expression."


# ------------------------------------------------------------
# 3. Main assistant function
# ------------------------------------------------------------

def assistant_response(user_input):
    """Process the user's request and return a response."""

    # Normalize the input.
    message = user_input.lower().strip()

    # Return a default message for empty input.
    if not message:
        return "Please enter a message so I can help you."

    # A. Handle greetings and predefined questions.
    if message in responses:
        return responses[message]

    # B. Return the current date.
    if message in [
        "date",
        "today's date",
        "what is today's date",
        "what is the date"
    ]:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {today}."

    # C. Return the current time.
    if message in [
        "time",
        "current time",
        "what time is it",
        "tell me the time"
    ]:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"The current time is {current_time}."

    # D. Perform calculations.
    calculation_prefixes = [
        "calculate ",
        "what is ",
        "compute "
    ]

    expression = None

    for prefix in calculation_prefixes:
        if message.startswith(prefix):
            possible_expression = message[len(prefix):].strip()

            # Only attempt calculation when the expression contains
            # digits and arithmetic operators.
            if (
                any(char.isdigit() for char in possible_expression)
                and any(char in "+-*/%" for char in possible_expression)
            ):
                expression = possible_expression
                break

    # Also accept direct expressions such as 25 * 4.
    if expression is None:
        if (
            any(char.isdigit() for char in message)
            and any(char in "+-*/%" for char in message)
        ):
            expression = message

    if expression is not None:
        result = calculate(expression)
        return f"The answer is: {result}"

    # E. Open supported websites.
    website_commands = {
        "open google": "https://www.google.com",
        "open youtube": "https://www.youtube.com",
        "open github": "https://github.com",
        "open wikipedia": "https://www.wikipedia.org"
    }

    if message in website_commands:
        website_url = website_commands[message]

        try:
            opened = webbrowser.open(website_url)

            if opened:
                return f"Opening {message.replace('open ', '').title()}."

            return (
                "I could not confirm that the website opened. "
                "You can visit: " + website_url
            )

        except webbrowser.Error:
            return "Sorry, I could not open the website."

    # F. Search the web.
    search_prefixes = [
        "search for ",
        "search "
    ]

    for prefix in search_prefixes:
        if message.startswith(prefix):
            query = message[len(prefix):].strip()

            if not query:
                return "Please tell me what you want to search for."

            search_url = (
                "https://www.google.com/search?q="
                + quote_plus(query)
            )

            try:
                opened = webbrowser.open(search_url)

                if opened:
                    return f"Searching the web for: {query}"

                return (
                    "I could not confirm that the search opened. "
                    "You can use this search address: " + search_url
                )

            except webbrowser.Error:
                return "Sorry, I could not open the web search."

    # G. Provide a list of available commands.
    if message in ["help", "what can you do", "show commands"]:
        return (
            "Here is what I can do:\n"
            "1. Greet you.\n"
            "2. Answer predefined questions about AI and Python.\n"
            "3. Tell you the current date and time.\n"
            "4. Calculate arithmetic expressions.\n"
            "5. Open Google, YouTube, GitHub, or Wikipedia.\n"
            "6. Search the web.\n"
            "7. Respond to unknown inputs with a default message."
        )

    # H. Handle unknown requests.
    return (
        "Sorry, I don't understand that request yet. "
        "Type 'help' to see the commands I support."
    )


# ------------------------------------------------------------
# 4. Run the assistant in the terminal
# ------------------------------------------------------------

def start_assistant():
    """Start an interactive terminal conversation."""

    print("=" * 50)
    print("       SMART AI ASSISTANT")
    print("=" * 50)

    print("Type 'help' to see available commands.")
    print("Type 'exit' or 'quit' to stop the assistant.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit", "goodbye"]:
            print("Assistant: Goodbye! Have a great day!")
            break

        reply = assistant_response(user_input)
        print("Assistant:", reply)


# Run the terminal assistant only when this file is executed directly.
if __name__ == "__main__":
    start_assistant()