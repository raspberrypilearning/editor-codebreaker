<h2 class="c-project-heading--task">Reverse the alphabet</h2>
--- task ---
Make a new list where the alphabet is reversed.
--- /task ---

Under the next comment that says `# Create the atbash code by reversing the alphabet` add the code below.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 9-13
---
# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))  # Reverse alphabet

    for i in range(len(alphabet)):
        code[alphabet[i]] = backwards[i]  # Match letters
--- /code ---
</div>
