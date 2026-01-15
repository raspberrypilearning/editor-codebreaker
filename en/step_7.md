<h2 class="c-project-heading--task">Create a frequency analyser</h2>
--- task ---
Write a function that works out how often each letter appears in your text.
--- /task ---

<div class="c-project-callout c-project-callout--tip">

### Tip
**Frequency analysis** counts how often something appears, so you can spot patterns in that data.
</div>

Copy the function below into your code above the `# User input` comment. This code turns the letter counts into a percentage of the whole message.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 31
line_highlights: 34-45
---
print(get_text('input.txt')) # print to check that it works
print(atbash(get_text('input.txt'))) # print to check that it works

# frequency analysis 
def frequency(text):
    text = text.lower()
    total = len(text) or 1
    freq = {ch: 0 for ch in alphabet} 
    
    for ch in text:
        if ch in freq:
            freq[ch] += 1
    return {ch: freq[ch] / total * 100 for ch in alphabet} 

print(frequency(get_text('input.txt'))) # print to check that it works

# user input
choice = ''  # Start with a wrong answer for choice.
--- /code ---
--- task ---
**Test:** Run your code. You should see a list of numbers. These numbers are the percentage of the message made up by each letter.
Try editing the text in `input.txt` and run the code again to see the percentage change.
--- /task---
</div>

<div class="c-project-output">
<pre>{' ': 20.0, 'a': 5.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 10.0, 'f': 0.0, 'g': 0.0, 'h': 10.0, 'i': 10.0, 'j': 0.0, 'k': 0.0, 'l': 10.0, 'm': 0.0, 'n': 0.0, 'o': 5.0, 'p': 0.0, 'q': 0.0, 'r': 0.0, 's': 15.0, 't': 15.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0}</pre>
</div>
