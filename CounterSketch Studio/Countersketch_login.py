'''
######################################################################################################################################################
Title         Python automated for CounterSketch Studio
Creator:      Matthew, Bebsz 
Version:      1.0
######################################################################################################################################################

[SETUP_INSTRUCTIONS]
- Requirements
    python3 - https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tar.xz
    pip - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    py -m pip install pyautogui

'''

import pyautogui
import time

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
serial_code = "SERIAL_NUMBER"

# Locate the username input field on the screen
username_field_location = pyautogui.locateOnScreen(r'C:\temp\CounterSketch\src\img\password_field.png', confidence=0.8)
if username_field_location is None:
    print("Username field not found.")
else:
    # Get the center coordinates of the username field
    username_field_center = pyautogui.center(username_field_location)
    # Click on the username field
    pyautogui.click(username_field_center)

    # Move the cursor to a relative position to the username field (adjust as needed)
    pyautogui.moveRel(100, 0)

    # Locate the password input field on the screen
    password_field_location = pyautogui.locateOnScreen(r'C:\temp\CounterSketch\src\img\username_field.png', confidence=0.8)
    if password_field_location is None:
        print("Password field not found.")
    else:
        # Get the center coordinates of the password field
        password_field_center = pyautogui.center(password_field_location)
        # Click on the password field
        pyautogui.click(password_field_center)

        # Wait for a short time for the fields to be focused
        time.sleep(0.5)

        # Enter the username and password
        pyautogui.typewrite(username)  # USERNAME
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(password)  # PASSWORD
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(serial_code)  # SERIAL CODE

        # Move the cursor away from the input fields
        pyautogui.moveRel(100, 0)

        # Locate the serial code input field on the screen
        serial_code_field_location = pyautogui.locateOnScreen(r'C:\temp\CounterSketch\src\img\serial_code_field.png', confidence=0.10)
        if serial_code_field_location is None:
            print("Serial code field not found.")
        else:
            # Get the center coordinates of the serial code field
            serial_code_field_center = pyautogui.center(serial_code_field_location)
            # Click on the serial code field
            pyautogui.click(serial_code_field_center)

        # Locate and click the login button
        login_button_location = pyautogui.locateOnScreen(r'C:\temp\CounterSketch\src\img\login_button.png', confidence=0.8)
        if login_button_location is None:
            print("Login button not found.")
        else:
            # Get the center coordinates of the login button
            login_button_center = pyautogui.center(login_button_location)
            # Click on the login button
            pyautogui.click(login_button_center)

        # Wait for the application to complete the login process
        time.sleep(5)
