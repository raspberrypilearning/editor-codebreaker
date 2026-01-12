<h2 class="c-project-heading--task">Encode the message</h2>
--- task ---
Create a function that can turn text into a secret message using the **atbash** code.
--- /task ---
 
Before you start, **comment out** the print line you used for testing the code dictionary.
<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 15
---
    for i in range(len(alphabet)):  # Go through each letter
        code[alphabet[i]] = backwards[i]  # Match each letter to its secret letter
  
   # print(code)

--- /code ---
</div>

<h2 class="c-project-heading--explainer">Make an atbash function</h2>

Find the comment that says `# Encode/decode a piece of text — atbash is symmetrical`. 

Under the comment, add the code below to define `atbash`, change the text to lower case, and create an output.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 23
line_highlights: 24-26
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text): 
    text = text.lower() # make lower case 
    output = '' # Store secret message

--- /code ---
</div>

<h2 class="c-project-heading--explainer">Encode your text</h2>

Add `loop` below to swap each letter for its secret letter. Check that your indentation is correct.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 23
line_highlights: 28-32
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text): 
    text = text.lower() # make lower case 
    output = '' # Store secret message

    for letter in text:
        if letter in code:
            output += code[letter] # Swap each letter

    return output
--- /code ---
</div>

<h2 class="c-project-heading--explainer">Test and debug</h2>

Add `print()` in `main()` to test your code.

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
    print(atbash('Test'))

--- /code ---
</div>

**Test:** Run your code. You should see `gvhg`. To change the output, replace `'Test'` with another word.

<div class="c-project-output">
<pre>gvhg</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging
If you see a message about an indentation error:
- Check that you have indented all of your code correctly
- Look back at the sample code on this page to help you check
</div>
