<h2 class="c-project-heading--task">Get user input</h2>
--- task ---
Asks your user to make choices about what they would like to do. If the user enters `e`, the message is encoded.
--- /task ---
 
--- task ---
Paste the code below into your project.
--- /task ---

<div class="c-project-callout c-project-callout--tip">

### Code explainer

- This uses `choice` in a loop. The loop runs until the user enters `e` or `f`.  
- If the user enters `e`, the message is encoded. 
- `f` is used later.

</div>

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 32
line_highlights: 34-50
---
print(atbash(get_text('input.txt'))) # print to check that it works

# user input
choice = ''  # Start with a wrong answer for choice.

while choice != 'e' and choice != 'f':  # Asking for the right answer
    choice = input('Enter e to encode text, or f for frequency analysis: ')

    if choice == 'e':
        print('Running your message through the cypher…')
        message = get_text('longer.txt')  # Take input from a file
        cyphertext = atbash(message)
        print(cyphertext)

    elif choice == 'f':
        print('Analysing message…')
        message = get_text('input.txt')
        message_freq = frequency(message)
        lang_freq = english  # Import the English frequency dictionary

--- /code ---
--- task ---
**Test:** Run your code. You should see a message asking for your choice.
--- /task---
</div>

<div class="c-project-output">
<pre>Enter e to encode/decode text, or f for frequency analysis: </pre>
</div>

--- task ---
Type `e` and press enter to encode your message.
--- /task---

<div class="c-project-output">
<pre>Running your message through the cypher…
gsrh rh olmtvi gvcg</pre>
</div>