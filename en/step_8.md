<h2 class="c-project-heading--task">Encode text from a file</h2>
--- task ---
 **Replace** your secret message with a `.txt` file to encode more text.
--- /task ---

Find the `# Fetch and return text from a file` comment and add the code below. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 34
line_highlights: 35-39
---
# Fetch and return text from a file
def get_text(filename): 
    with open(filename) as f: # open the file
        text = f.read().replace('\n','')  # read file and replace newline

    return text # Return the text
--- /code ---
</div>

In `menu()` **replace** your secret `message` with `get_text()`. This is where the name of the `.txt` file goes.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 41
line_highlights: 50
---
# Create a text-based menu system
def menu():
    choice = ''  # Start with a wrong answer for choice.

    while choice != 'c' and choice != 'f':  # Asking for the right answer
        choice = input('Enter c to encode/decode text, or f for frequency analysis: ')

    if choice == 'c':
        print('Running your message through the cypher…')
        message = get_text('input.txt')  # Take input from a file
        code = atbash(message)
        print(code)
--- /code ---
</div>
