from pygal import Bar
from frequency import english

alphabet = ' abcdefghijklmnopqrstuvwxyz '
backwards = alphabet[::-1]

code = {alphabet[i]: backwards[i] for i in range(len(alphabet))} # Create a dictionary to map the letters

# atbash function creates the secret code
def atbash(text):
    text = text.lower() # make lower case
    output = '' # Store secret message

    for letter in text:
        if letter in code:
            output += code[letter] # Swap each letter

    return output

# get_text function
def get_text(filename):
    with open(filename) as f: # open the file
        text = f.read().replace('\n','')  # read file and replace newline

    return text # Return the text
    
# frequency analysis 
def frequency(text):
    text = text.lower()
    total = len(text) or 1
    freq = {ch: 0 for ch in alphabet} #Note to Becca - changed to a dictionary comprehension so it creates a dict with each letter mapped to 0
    for ch in text:
        if ch in freq:
            freq[ch] += 1
    return {ch: freq[ch] / total * 100 for ch in alphabet} #Note to Becca - this is another dict comprehension but does the percentage calculation.

# Create the chart 
def make_chart(text, language):
    chart = Bar(width=800, height=400, title='Frequency analysis', x_labels = list(text.keys())) # Make a bar chart
    chart.add('Target message', list(text.values()))  # Label the frequency data for the encoded message
    chart.add('Language', list(language.values()))  # Label the frequency data for the language
    chart.render() #Render the chart

# User input
choice = ''  # Start with a wrong answer for choice.

while choice != 'e' and choice != 'f':  # Asking for the right answer
    choice = input('Enter e to encode text, or f for frequency analysis: ')

    if choice == 'e':
        print('Running your message through the cypher…')
        message = get_text('longer.txt')  # Take input from a file
        cyphertext = atbash(message)
        print(cyphertext)
    
    elif choice == 'f':
        print('Analysing message…')
        message = get_text('input.txt')
        message_freq = frequency(message)
        lang_freq = english  # Import the English frequency dictionary
        make_chart(message_freq, lang_freq)  # Call the function to make a chart        