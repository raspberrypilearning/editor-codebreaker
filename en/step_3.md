
### Encode the alphabet

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Encoding is when you convert data from one form to another. In an atbash cypher for example, the letter 'e' would be **encoded** as a 'v'. 
</p>

You now have two lists. One contains the alphabet written forwards, the other with the alphabet backwards. You are now going to use these two lists to populate a dictionary. The **key** will store the alphabet written forwards and the **paired value** will store the alphabet backwards. 

The code dictionary is really important because you can use it to match each letter from your message using the **key**, with its encoded **paired value**. 

--- task ---

Within your `create_code` function, **populate** the `code` dictionary with data from the two **lists**. Use a `for` loop to get the length of the `alphabet` list and populate the **dictionary** with the data. 

`len()` is a function that you can use to find out the length of an **object**, such as a list. It is used here to iterate a `for` loop, as many times as there are characters in the `alphabet` list — its length. 

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 11
line_highlights: 14-15
---
def create_code():
    backwards = list(reversed(alphabet))  # Reverses a list

    for i in range(len(alphabet)):  # Gets the length of a list
        code[alphabet[i]] = backwards[i]  # Populate the code dictionary with a letter of the alphabet and its encoded letter
--- /code ---

--- /task ---

Creating a `main()` function is useful to **call** all of the required functions when your program first starts. 

--- task ---

Find the `# Start up` comment and **define** a `main()` function to call your `code()` function. Next, call the `main()` function in the main body of your code. 

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 37
line_highlights: 38-41
---
# Start up
def main():
    create_code()

main()
--- /code ---

--- /task ---

### Test and debug

--- task ---

To test that your `code` dictionary has populated correctly, you can `print` the dictionary in full. Under your `for` loop in the `create_code` function, add a `print` function to display the contents. 

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 11
line_highlights: 17
---
def create_code():
    backwards = list(reversed(alphabet))

    for i in range(len(alphabet)):  #  Gets length of a list
        code[alphabet[i]] = backwards[i]  #  Populates the code dictionary with a letter of the alphabet and its encoded letter

    print(code)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see if the `code` dictionary displays correctly. You should see a pattern starting with the letter `a` paired with `z` and the letter `b` being paired with `y`.


![The output of the code dictionary that is created in this step.](images/code-dictionary.PNG){:width="600px"}

**Debug:** There are no error messages but your code dictionary is not displaying on the screen:
- Make sure that `print(code)` is indented correctly within the `create_code` function
- Check that you have **called** the `create_code()` and the `main()` function correctly

**Debug:** If you see a message about `code` not being defined, make sure that you have initialised the `code` dictionary. 

**Debug:** If you see a message about an indentation error:
- Check that you have indented all of your code correctly
- Look back at the sample code on this page to help you check

--- /task ---

In the next step, you will **encode** a message with the help of your `code` dictionary. 

--- save ---
