<h2 class="c-project-heading--task">Analyse more text</h2>

The chart that has been produced shows the frequency of letters in the English language, labelled as **Language**. You can see that the letter **e** is the most frequently used letter in the English language because it has the highest bar for all of the **language** values. 

The frequency chart also lists the frequency of letters in your **encoded** message, labelled as **Target message**. This includes the spaces in your message, which can be seen in the last bar on the right. To work out what **encoding** has been used for this message, you can compare the bars showing the English language with the bars on the encoded message. The highest bar (ignoring the spaces) in the encoded message text will most likely be an **e**. The second highest letter will most likely be a **t** as this is the next most popular letter. 

Codebreakers can use the frequency of letters to work out the type of encoding that has been used on the message. They can use trial and error to **predict** what a letter might represent using the chart as a guide. 

Your secret message is quite small, which makes it tricky to analyse using a frequency chart. Change your code so that it analyses the message in `longer.txt` instead. 

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

**Analyse** the frequency chart by looking at the **Language** values and the **Target message** values. Notice how the highest bar for **Language** is **e** and the highest bar for **Target message** is **v**. This is because with the **Atbash** cypher, the letter **e** is encoded with the letter **v**. 

<div class="c-project-output">
![A bar chart showing the frequency of letters in the English language compared to the frequency of letters used in the encoded message in longer.txt.](images/longer-analysis.PNG)
</div>