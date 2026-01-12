<h2 class="c-project-heading--task">Create a menu</h2>
--- task ---
Create a menu that asks your user to make choices about what they would like to do.
--- /task ---

Before you start **comment out** `print(atbash('Test'))` in `main()`. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 40
line_highlights: 43
---
# Start up
def main():
    create_code()
    # print(atbash('Test'))

main()
--- /code ---
</div>

**Find** the `# Create a text-based menu system` comment. Under this define a function called `menu()` and create a new variable called `choice`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 37
line_highlights: 38-39
---
# Create a text-based menu system  
def menu():
    choice = '' # Wrong answer

--- /code ---
</div>

Create a **while loop** that runs as long as your answer **DOES NOT** match one you have defined. As long as the user **does not** choose `c` or `f`, the loop will continue to run. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 37
line_highlights: 41-42
---
# Create a text-based menu system  
def menu():
    choice = ''  # Wrong answer

    while choice != 'c' and choice != 'f':  # Asking for the right answer
        choice = input('Enter c to encode/decode text, or f for frequency analysis: ')
--- /code ---
</div>