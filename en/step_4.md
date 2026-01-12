<h2 class="c-project-heading--task">Start the program</h2>
--- task ---
Create a `main()` function to run the other parts of your program when it starts.
--- /task ---

Under the the `# Start up` comment, add the code below. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 30
line_highlights: 31-34
---
# Start up
def main():
    create_code()

main()
--- /code ---
</div>

Now add `print` so you can check that your code works.

In the `# Create the atbash code by reversing the alphabet` code add the following line:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 15
---
# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))  # Reverse alphabet

    for i in range(len(alphabet)):  # Go through each letter
        code[alphabet[i]] = backwards[i]  # Match each letter to its secret letter

    print(code)
--- /code ---
</div>

**Test:** Run your code. You should see a pattern where the alphabet is revered - a matches with z, and b matches with y.

<div class="c-project-output">
<pre>{' ': ' ', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging
If nothing appears on the screen:
- Check that print(code) is indented inside the create_code function
- Check that both create_code() and main() are written exactly as shown

If you see a message saying code is not defined make sure you created the code dictionary in earlier steps.

If you see an indentation error:
- Check that all lines are indented correctly
- Compare your code with the example above
</div>
