# Start Up message
import openai
import os
import platform

# Program Info
omniVersion = "0.0.1"
omniAuthors = "Eben Vranken"

# Signature
print(
    f"Project Omniscient\nVersion: {omniVersion}]\nAuthor(s): {omniAuthors}\n")

# Reading System Information
print(f"Reading OS Information")

osName = platform.system()
osRelease = platform.release()
osVersion = platform.version()
home_directory = os.path.expanduser('~')

# Declare API key environment variable
# os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI API key: ")
os.environ["OPENAI_API_KEY"] = input("Enter your API key: ")

# # API Key Authorization
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize user menu
isRunning = True
totaltoken = 0

# Command List
commandList = [
    "help",
    "info",
    "stop",
    "usage",
]

# Commands
# Help


def help():
    print(
        f"""List of all current commands:
-help: Get a list of all current commands
-stop: Stops the application
-info: Provides more information about Project Omniscient
-usage: Provides the total token usage for the current session\n"""
    )


# Stop
def stop():
    global isRunning
    isRunning = False


# Info
def info():
    print(
        f"""Project Omniscient is an Operating System Assistant powered by the GPT language model.
Authors: {omniAuthors}
Version: {omniVersion}\n"""
    )


def usage():
    print(f"""Total token usage: {totaltoken}
Price estimation: {0.002/1000*totaltoken}""")


# Introduction message
print("Welcome to Project Omniscient\nUse command /help for more information\n")

while isRunning:
    userInput = input(">Enter your command: ")
    # Input is a command
    if userInput[1:] in commandList:
        exec(f"{userInput[1:]}()")
    # Input is a Omniscient command
    elif userInput != "":
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                    "content": f"""Task: Provide terminal commands for various system-related tasks.

As a helpful assistant, I can provide you with the necessary terminal commands to perform system-related tasks on {osName} {osRelease} ({osVersion}), with your home directory located at {home_directory}. Please note that I will only respond with the necessary terminal command(s) to achieve the task you requested, without any additional explanations or instructions. Simply type your request, and I will respond with the appropriate command(s) to carry out the task."""},
                {"role": "user", "content": userInput},
            ],
        )

        print(f""">{userInput}\n""")
        omniscientOutput = completion.choices[0].message.content
        print(omniscientOutput)
        totaltoken += completion.usage.total_tokens
        print(
            f"— Used {completion.usage.total_tokens} tokens. (${0.002/1000*completion.usage.total_tokens})\n")

        # Run Omniscient Output
        os.system(omniscientOutput)
