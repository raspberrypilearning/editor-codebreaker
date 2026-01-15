<h2 class="c-project-heading--task">Count letters</h2>
--- task ---
Count the letters in the text to determine how often they appear.
--- /task ---

Add the code below to the `frequency` function

Create a `for` loop to count every time each letter appears in the text. Leave a blank line at the end of your script.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 25-29
---
# Calculate the frequency of all letters in a piece of text
def frequency(text):
    text = list(text.lower())  # Convert to lower case and make a list

    freq = {} 
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)  # Count the letters 

    for letter in text:
        if letter in freq:
            freq[letter] += 1
--- /code ---
</div>

