<h2 class="c-project-heading--task">Make a secret code</h2>
--- task ---
Use a function to turn text into a secret message.
--- /task ---

Under the the `print(code)` line, add the code below. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11-22
---
code = {alphabet[i]: backwards[i] for i in range(len(alphabet))} # Create a dictionary to map the letters
print(code) # print to check that it works

# create the atbash function
def atbash(text):
    text = text.lower() # make lower case
    output = '' # Store secret message

    for letter in text:
        if letter in code:
            output += code[letter] # Swap each letter

    return output

print(atbash('hello world'))
--- /code ---
--- task ---
**Test:** Run your code. You should see that `'hello world'` has been encoded.
--- /task---
</div>

<div class="c-project-output">
<pre>svool dliow</pre>
</div>

--- task ---
Try changing `'hello world'` to a different message. Make sure you use `'` around the text.
--- /task ---

<div class="c-project-callout c-project-callout--tip">

### What is Atbash?
- Atbash makes the secret code.
- It uese the swapped letters from the dictionary to create new words
</div>
