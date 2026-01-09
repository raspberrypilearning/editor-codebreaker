<h2 class="c-project-heading--task">Encode a secret message</h2>
--- task ---
In this project you'll make an encoded message and use a graph to crack the code.
--- /task ---

## Encode the alphabet
To start, create a dictionary for your encoded letters. 

Find the `# Set up data structures` comment, then use the `list()` function to create a **list** of letters from the `alphabet`. 

**Initialise** the `code` **dictionary** so that you can populate it in a later step.  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 5 
line_highlights: 6-8
---
# Set up data structures
alphabet = list(' abcdefghijklmnopqrstuvwxyz ')  # List from a string
code = {}
print(alphabet)
--- /code ---

Tip
The `alphabet` list contains spaces at the beginning and end to preserve the spaces in the message. Strong encryption would not do this, as it makes the message easier to decode. The spaces have been kept in for this project to make the messages easier to read. 