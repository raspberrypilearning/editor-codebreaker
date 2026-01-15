<h2 class="c-project-heading--task">Create a frequency analyser</h2>
--- task ---
Code a frequency analyser function to work out how often each letter of the alphabet appears in your text
--- /task --- 


Beneath the `# Calculate the frequency of all letters in a piece of text` comment add the code below. 

This defines `frequency`, and converts your message to lower case and make it a list.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 18-19
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Make lower case and a list
--- /code ---
</div>