<h2 class="c-project-heading--task">Reverse text</h2>

Print the alphabet and then reverse it.

Add the Python code below to create `alphabet` and `backwards`.

The code uses `[::-1]` to reverse the text.

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
</div>

## Now run your code

You should see the alphabet printed in the output.

Try printing **backwards** to see it in reverse.


<div class="c-project-output">
abcdefghijklmnopqrstuvwxyz
</div>

### Tip
<div class="c-project-callout c-project-callout--tip">

Two libraries are already imported into your project: `pygal` and `frequency`. You can see them at the top of your code.
</div>

