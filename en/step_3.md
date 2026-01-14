<h2 class="c-project-heading--task">Create a dictionary</h2>
--- task ---
Create a dictionary that maps each letter in `alphabet` to the matching letter in `backwards`.
--- /task ---.
--- /task ---

Add the code below and check that it works in the **Text output** tab.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8-9
---
from pygal import Bar
from frequency import english

alphabet = ' abcdefghijklmnopqrstuvwxyz '
backwards = alphabet[::-1]
print(alphabet) # print to check that it works

code = {alphabet[i]: backwards[i] for i in range(len(alphabet))} # Create a dictionary to map the letters
print(code) # print to check that it works
--- /code ---
--- task ---
**Test:** Run your code. You should see that the alphabet is reversed.  
For example, **a** matches **z**, and **b** matches **y**.
--- /task ---
</div>

<div class="c-project-output">
<pre>{' ': ' ', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}</pre>
</div>