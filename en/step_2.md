<h2 class="c-project-heading--task">Reverse text</h2>
--- task ---
Print the alphabet and then reverse it.
--- /task ---

--- task ---
Add the Python code below to create `alphabet` and `backwards`.

The code uses `[::-1]` to reverse the text.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4-6
---
from pygal import Bar
from frequency import english

alphabet = ' abcdefghijklmnopqrstuvwxyz '
backwards = alphabet[::-1]
print(alphabet) # print to check that it works
--- /code ---
--- task ---
**Test:** Run the code. You should see the alphabet printed.  
Try printing **backwards** to see it in reverse.
--- /task ---
</div>

<div class="c-project-output">
abcdefghijklmnopqrstuvwxyz
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip
Two libraries are already imported into your project: `pygal` and `frequency`. You can see them at the top of your code.
</div>










