<h2 class="c-project-heading--task">Encode the message</h2>
--- task ---
Create a function that can turn text into a secret message using the atbash code.
--- /task ---
 
Before you start, **comment out** the print line you used for testing the code dictionary.

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 12
line_highlights: 15
---
    for i in range(len(alphabet)):  # Go through each letter
        code[alphabet[i]] = backwards[i]  # Match each letter to its secret letter
  
   # print(code)
   
--- /code ---

<h2 class="c-project-heading--explainer">Make your atbash function</div>

Find the comment that says `# Encode/decode a piece of text — atbash is symmetrical`. 

Under the comment, add a function called atbash.

Inside the function:
- change the text to lower case
- create an empty string called output to build the secret message

--- code ---
---
language: python
filename: main.py - atbash()
line_numbers: true
line_number_start: 23
line_highlights: 24-26
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text): 
    text = text.lower() # Converts text to lower case 
    output = '' # Stores the secret message

--- /code ---

<h2 class="c-project-heading--explainer">Encode your text</h2>

Add code below to go through the text one letter at a time.

Use the `code` dictionary to swap each letter for its secret letter. When all the letters are done, send the secret message back.

--- code ---
---
language: python
filename: main.py - atbash()
line_numbers: true
line_number_start: 23
line_highlights: 28-32
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text):
    text = text.lower() # Converts text to lower case 
    output = '' # Stores the secret message'

    for letter in text:
        if letter in code:
            output += code[letter] # Swap each letter using the code dictionary

    return output # Send back the secret message

--- /code ---

<h2 class="c-project-heading--explainer">Test and debug</div>

Add a line in `main()` to test your code using the word `Test`.

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 40
line_highlights: 43
---
# Start up
def main():
    create_code()
    print(atbash('Test'))

--- /code ---

**Test:** Run your code. You should see `gvhg`.

<div class="c-project-output">
<pre>gvhg</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging
If you see a message about an indentation error:
- Check that you have indented all of your code correctly
- Look back at the sample code on this page to help you check

</div>

**Comment out** your `print(atbash('Test'))` line of code now that you have finished testing. 

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 40
line_highlights: 43
---
# Start up
def main():
    create_code()
    # print(atbash('Test'))

--- /code ---
