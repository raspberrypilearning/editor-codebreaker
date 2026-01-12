<h2 class="c-project-heading--task">Analyse more text</h2>
--- task ---
Change your code so that it analyses the message in `longer.txt`. 
--- /task ---

Codebreakers can use the frequency of letters to work out the type of encoding that has been used on the message. They can use trial and error to **predict** what a letter might represent using the chart as a guide. 

Your secret message is quite small, which makes it tricky to analyse using a frequency chart. 

Change `input.txt` to `longer.txt`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 75
line_highlights: 77
---
    elif choice == 'f':
        print('Analysing message…')
        message = get_text('longer.txt') 
        message_freq = frequency(message)  # Get the frequency of the letters in the message, as %
--- /code ---
</div>

**Test:** Run the code and notice how the highest bar for **Language** is **e** and the highest bar for **Target message** is **v**. This is because with the **Atbash** cypher, the letter **e** is encoded with the letter **v**. 

<div class="c-project-output">
![A bar chart showing the frequency of letters in the English language compared to the frequency of letters used in the encoded message in longer.txt.](images/longer-analysis.PNG)
</div>