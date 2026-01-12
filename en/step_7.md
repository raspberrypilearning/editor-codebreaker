<h2 class="c-project-heading--task">Add message</h2>
--- task ---
Add a message to encode `if` the user enters `c`.
--- /task ---

Add the code below.

You can change the text that says `'my secret message'` to anything you like. This text will be encoded and decoded.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 37
line_highlights: 44-48
---
def menu():
    choice = ''  # Wrong answer

    while choice != 'c' and choice != 'f':  # asking for the right answer
        choice = input('Enter c to encode/decode text, or f for frequency analysis: ')

    if choice == 'c':
        print('Running your message through the cypher…')
        message = 'my secret message' # text to encode
        code = atbash(message)
        print(code)

--- /code ---
</div>

Under `# Start up` comment, add `menu()` to call when the program runs. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 50
line_highlights: 54
---
# Start up
def main():
    create_code()
    # print(atbash('Test'))
    menu()

main()

--- /code ---
</div>

**Test:** Run your code to see the user prompt. 

<div class="c-project-output">
<pre>Enter c to encode/decode text, or f for frequency analysis: </pre>
</div>

Type `c` and press **Enter** to encode your message! 

<div class="c-project-output">
<pre>Running your message through the cypher…
nb hvxivg nvhhztv</pre>
</div>

To see different encoded messages change the `'my secret message'` text and run your code again.

<div class="c-project-callout c-project-callout--debug">
### Debugging
If you see a message about an indentation error:
- Check that you have indented all of your code correctly
- Look back at the sample code on this page to help you check

If you see the error message `c is not defined` when you run your code, check that you have used apostrophes ('') around your c in the condition `choice != 'c'`.

If nothing happens when you press `c`, check that you have correctly spelled `message`.
</div>