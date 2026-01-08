## Encode the alphabet

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
To start, you will create a dictionary for your encoded letters. 
</div>
<div>
![The output of the code dictionary that is created in this step.](images/code-dictionary.PNG){:width="600px"}
</div>
</div>

--- task ---

If you have a Raspberry Pi account, you can click **Save** to save a copy of the starter code to your library.


### Set up the alphabet list and the code dictionary

The codebreaker program starts with two data structures. The first data structure is a **list** of all the letters in the alphabet and the second is a `code` **dictionary**. To save typing time, you can create a list from a string by using the `list()` function.  

[[[list-function]]]

--- task ---

Find the `# Set up data structures` comment in the program, then use the `list()` function to create a **list** of letters from the `alphabet`. Next, **initialise** the `code` **dictionary** so that you can populate it in a later step.  

The `alphabet` list contains spaces at the beginning and end to preserve the spaces in the message. Strong encryption would not do this, as it makes the message easier to decode. The spaces have been kept in for this project to make the messages easier to read. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 5 
line_highlights: 6-7
---
# Set up data structures
alphabet = list(' abcdefghijklmnopqrstuvwxyz ')  # List from a string
code = {}

--- /code ---

--- /task ---

### Create a new list that reverses the alphabet

You need to create a new list that holds the alphabet, but backwards. You can use the `list()` function again to help with this. You can also use the `reversed()` function to reverse an existing list. 

--- task ---

Find the `# Create the atbash code by reversing the alphabet` comment then **define** a new function called `create_code`. Next, create a **list** that holds the **reverse** of the `alphabet` list. 

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 10 
line_highlights: 11-12
---
# Create the atbash code by reversing the alphabet
def create_code():
    backwards = list(reversed(alphabet))  # Reverses a list

--- /code ---

--- /task ---
