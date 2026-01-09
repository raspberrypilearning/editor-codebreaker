<h2 class="c-project-heading--task">Start the program</h2>
--- task ---
Set up your program so it runs your code when it starts.
--- /task ---

Create a `main()` function. This runs the other parts of your program when it starts.

Under the the `# Start up` comment, add the code below. 

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 30
line_highlights: 31-34
---
# Start up
def main():
    create_code()

main()
--- /code ---

Now add `print` so you can check that your code works.

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 8
line_highlights: 15
---
# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))

    for i in range(len(alphabet)):  #  Gets length of a list
        code[alphabet[i]] = backwards[i]  #  Populates the code dictionary with a letter of the alphabet and its encoded letter

    print(code)
--- /code ---


**Test:** Run your code. You should see a pattern where:
- a matches with z
- b matches with y

<div class="c-project-output">
<pre>{' ': ' ', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}</pre>
</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging
If nothing appears on the screen:
- Check that print(code) is indented inside the create_code function
- Check that both create_code() and main() are written exactly as shown

If you see a message saying code is not defined make sure you created the code dictionary earlier in the program

If you see an indentation error:
- Check that all lines are indented correctly
- Compare your code with the example above

