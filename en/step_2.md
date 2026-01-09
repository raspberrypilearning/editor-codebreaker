<h2 class="c-project-heading--task">Reverse the alphabet</h2>
--- task ---
Make a new list where the alphabet is backwards.
--- /task ---

Use `list()` together with `reversed()` to reverse the letters. 

Under the next comment that says `# Create the atbash code by reversing the alphabet` add the code below.

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 8
line_highlights: 9-13
---
# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))  # Reverse alphabet

    for i in range(len(alphabet)):  # Go through each letter
        code[alphabet[i]] = backwards[i]  # Match each letter to its secret letter
    
--- /code ---
