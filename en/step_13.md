<h2 class="c-project-heading--task">Count letters</h2>
--- task ---
Create a variable called `total_letters` and assign the length of the text to that variable. 
--- /task ---

Add the code below to the `frequency` function

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 26
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert the message to lower case and make it a list

    freq = {}  # Create a dictionary of every letter, with a count of 0
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)  # Count the letters in the message
--- /code ---
</div>

Once you know how long the message is, you can begin counting the letters in it to determine how often they appear.

Create a `for` loop to count every time each letter appears in the text. Leave a blank line at the end of your script, make sure you keep the indentation, and add:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 28-30
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert the message to lower case and make it a list

    freq = {}  # Create a dictionary of every letter, with a count of 0
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)  # Count the letters in the message

    for letter in text:
        if letter in freq:
            freq[letter] += 1
--- /code ---
</div>


Create a `loop` that converts the number of times the letters appear into a percentage of the whole message.
 
 <div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 32-33
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert the message to lower case and make it a list

    freq = {}  # Create a dictionary of every letter, with a count of 0
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)  # Count the letters in the message

    for letter in text:
        if letter in freq: 
            freq[letter] += 1

    for letter in freq:
        freq[letter] = freq[letter] / total_letters * 100  # Convert from counts to percentages
--- /code ---
</div>


**Return** the frequency dictionary so it can be used elsewhere in your code. Leave a blank line and type:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 35
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert the message to lower case and make it a list

    freq = {}  # Create a dictionary of every letter, with a count of 0
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)  # Count the letters in the message

    for letter in text:
        if letter in freq: 
            freq[letter] += 1

    for letter in freq:
        freq[letter] = freq[letter] / total_letters * 100  # Convert from counts to percentages

    return freq
--- /code ---
</div>

### Extend the menu to include 'f'

Now that you have a function that can calculate the frequency of letters in your message, you need to link it to your user menu. Right now, the user can only choose the letter 'c' to encode or decode a message. If they type the letter 'f', nothing happens. You are now going to add the option 'f' to analyse the letter frequency of your message by calling your new function. 

Underneath your first `if` statement asking the user to select 'c', you need to add an `elif` statement so the user can choose the option to analyse and print the letter frequency by pressing 'f'.

Leave a blank line after the `if` statement and, on line 72, type:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 63
line_highlights: 72-76
---
    while choice != 'c' and choice != 'f':  # Keep asking the user for the right answer
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')

    if choice == 'c':
        print('Running your message through the cypher…')
        message = get_text('input.txt')  # Take input from a file 
        code = atbash(message)
        print(code)

    elif choice == 'f':
        print('Analysing message…')
        message = get_text('input.txt')
        message_freq = frequency(message)
        print(message_freq)
--- /code ---
</div>


**Test:** Run your code. Choose 'f' at the prompt and you should see a readout of the letter frequency of your message in the console. The values you see from your message will be different from the values shown here:

<div class="c-project-output">
![Image showing the output of a frequency analysis function as percentages.](images/freq-analysis-text-output.PNG)
</div>