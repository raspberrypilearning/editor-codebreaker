<h2 class="c-project-heading--task">Add frequency dictionary</h2>
--- task ---
Add the code below to create a dictionary called `freq`.
--- /task ---

Make sure you **keep the indentation**.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 21-23
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert the message to lower case and make it a list

    freq = {}  # Create a dictionary
    for letter in alphabet:
        freq[letter] = 0
--- /code ---
</div>