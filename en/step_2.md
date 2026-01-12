<h2 class="c-project-heading--task">Set up code</h2>
--- task ---
Set up the list and code functions.
--- /task ---

<h2 class="c-project-heading--explainer">Encode the alphabet</h2>
To start, find the comment that says `# Set things up`.

Add the Python code below to turn `alphabet` into a list of letters. You will add to `code = {}` later.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4 
line_highlights: 5-6
---
# Set things up
alphabet = list(' abcdefghijklmnopqrstuvwxyz ')  # Make a list with the letters of the alphabet
code = {} 
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip
The `alphabet` list has spaces at the beginning and end so the spaces in the message stay the same.
Very strong secret codes would not do this, because it makes messages easier to figure out.
The spaces are kept here to make the messages easier to read.
</div>