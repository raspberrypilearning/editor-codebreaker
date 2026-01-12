<h2 class="c-project-heading--task">Analyse the frequency</h2>
--- task ---
Code a frequency analyser function to work out how often each letter of the alphabet appears in your text
--- /task --- 

First add a `#` to the beginning of the `print(message_freq)` line so that Python ignores it when the code is run. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 72
line_highlights: 76
---
    elif choice == 'f':
        print('Analysing message…')
        message = get_text('input.txt')  # Take input from the same file. We have a 'longer.txt' or similar containing cyphertext we know to perform reasonably well for frequency analysis
        message_freq = frequency(message)  # Get the frequency of the letters in the message, as %
        # print(message_freq)
--- /code ---
</div>

<h2 class="c-project-heading--explainer">Make the frequency chart function</h2>

--- task ---

Find the `# Make frequency chart` comment and create a new function called `make_chart()`. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 36
line_highlights: 37-38
---
# Make frequency chart
def make_chart(text, language): 
    chart = Bar(width=800, height=400, title='Frequency analysis', x_labels = list(text.keys())) # Make a bar chart
--- /code ---
</div>

Label the chart with the **frequency** of letters in the encoded message and the known letter frequency of the **language** the message is in. This data has been **passed into** the **function** via the `text` and `language` parameters. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py - make_chart()
line_numbers: true
line_number_start: 36
line_highlights: 39-40
---
# Make frequency chart
def make_chart(text, language):
    chart = Bar(width=800, height=400, title='Frequency analysis', x_labels = list(text.keys()))
    chart.add('Target message', list(text.values()))  # Label the frequency data for the encoded message
    chart.add('Language', list(language.values()))  # Label the frequency data for the language

    chart.render() #Render the chart 
--- /code ---
</div>

### Call the frequency chart function

Find your `elif` in the `menu()` function. Add a line of code that will **import** the `english` frequency dictionary from the `frequency.py` file. Add another line of code that will **call** the `make_chart` function to draw the chart. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 75
line_highlights: 80-81
---
    elif choice == 'f':
        print('Analysing message…')
        message = get_text('input.txt')  # Take input from the same file. We have a 'longer.txt' or similar containing cyphertext we know to perform reasonably well for frequency analysis
        message_freq = frequency(message)  # Get the frequency of the letters in the message, as %
        # print(message_freq)
        lang_freq = english  # Import the English frequency dictionary
        make_chart(message_freq, lang_freq)  # Call the function to make a chart
--- /code ---
</div>

**Test:** Run your code to display the frequency analysis bar chart. 

<div class="c-project-output">
![A bar chart showing the frequency of letters in the English language compared to the frequency of letters used in the encoded message.](images/frequency-analysis.PNG)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

In all languages, each letter in its alphabet has a 'personality' or set of traits when used in that language. One of the most obvious traits a letter has in any language is how often it appears. **Frequency analysis** is the method of breaking codes by looking at how often letters are used in the language of the code, and comparing that to how often encoded letters show up in a message. In English, the letter **e** is the most commonly used letter (it shows up 12.8% of the time), followed by **t** (at 9.1%). The least often used letter is **z**.
</div>

<div class="c-project-callout c-project-callout--debug">
Your chart doesn't look exactly the same as the one displayed in the image above:
- This is normal. Your chart will display the frequency data for the secret message that you have entered in `input.txt`.

You see the following error message `NameError: name 'lang_freq' is not defined`:
- Check that you added the line of code `lang_freq = english` **before** the `make_chart()` function call.

You see an `Indentation error` message:
- Check that you have correctly indented all of your new code. Revisit the tasks above to check.
</div>