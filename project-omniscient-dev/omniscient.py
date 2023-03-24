
import webbrowser
import time
import pyautogui
import platform
import pygetwindow as gw

# Start Up message
print("Project Omniscient\nVersion: 0.0.1\nAuthor: Eben Vranken")

# Browser manipulation
chatGPTLink = "https://chat.openai.com/chat"

print("Launching GPT.")
webbrowser.open(chatGPTLink)
time.sleep(3)
browserApplication = gw.getActiveWindow()
print("GPT launched.")

# Reading system/OS information
osName = platform.system()
osVersion = platform.version()

# Enter template prompt
protocolPrompt = f"Hello ChatGPT! I am using {osName} and {osVersion}. From now on, we will be following a protocol to ensure our conversations go smoothly. Whenever I ask you a question, please respond with a command and a command only. No apologies, no explanations, just the command. This is to ensure that we stay on track and get things done efficiently. Let's get started!"
pyautogui.write(protocolPrompt)
pyautogui.press('enter')

# User Access Given
print("User Access Given")

# Command List
cmd = [
    "help", "info", "stop",
]

# User States
isStopped = False

# Command List


def help():
    print("List of all current commands:\n-help: Get a list of all current commands\n-stop: Stops the application\n-info: Provides more information about Project Omniscient")


def stop():
    global isStopped
    isStopped = True


print("\nWelcome to Project Omniscient\nUse command /help for more information\n")
while isStopped != True:
    userInput = input(">enter command: ")
    # Input was Omniscient command
    if (userInput in cmd):
        exec(userInput + "()")
    else:
        # Input was GPT command
        browserApplication.activate()
        pyautogui.write(userInput)
        pyautogui.press('enter')
