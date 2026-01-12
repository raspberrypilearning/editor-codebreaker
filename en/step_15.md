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
line_number_start: 63
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

**Test:** Run your code. Choose 'f' at the prompt and you should see a readout of the letter frequency of your message in the console. The values you see from your message will depend on the text you added to the input.txt file.

<div class="c-project-output">
![Image showing the output of a frequency analysis function as percentages.](images/freq-analysis-text-output.PNG)
</div>