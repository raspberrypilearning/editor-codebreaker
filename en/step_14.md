<h2 class="c-project-heading--task">Turn counts into percentage</h2>
--- task ---
Now you know how long the message is, you can begin counting the letters in it to determine how often they appear.
--- /task ---

Create a `loop` that converts the number of times the letters appear into a percentage of the whole message.

**Return** the frequency dictionary so it can be used elsewhere in your code. 
 
 <div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 31-34
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


