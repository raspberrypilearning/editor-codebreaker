<h2 class="c-project-heading--task">Extend the menu to include 'f'</h2>
--- task ---
Add the option for the user to press 'f' to analyse and print the letter frequency.
--- /task ---
 
In the `menu` function add the code below.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 57
line_highlights: 72-76
---
# Create a text-based menu system
def menu():
    choice = ''  # Start with a wrong answer for choice.
    
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

**Test:** Run your code. Choose 'f' at the prompt and you should see a readout of the letter frequency of your message in the Text output tab. 

<div class="c-project-output">
<pre>Enter c to encode/decode text, or f for frequency analysis: 
f
Analysing message…
{' ': 20.0, 'a': 5.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 10.0, 'f': 0.0, 'g': 0.0, 'h': 10.0, 'i': 10.0, 'j': 0.0, 'k': 0.0, 'l': 10.0, 'm': 0.0, 'n': 0.0, 'o': 5.0, 'p': 0.0, 'q': 0.0, 'r': 0.0, 's': 15.0, 't': 15.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0}<pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip
The values you see will depend on the text you added to the input.txt file.
</tip>