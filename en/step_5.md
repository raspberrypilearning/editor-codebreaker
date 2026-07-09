## Get user input

Ask your user to make choices about what they would like to do.

If the user enters `e`, the message is encoded.

Paste the code below into your project.

```python filename="main.py" line_numbers="true" line_number_start="32" line_highlights="34-50"
print(atbash(get_text('input.txt'))) # print to check that it works

# user input
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

```

## Now run your code

You should see a message asking for your choice.

```
Enter e to encode/decode text, or f for frequency analysis: 
```

Type `e` and press Enter to encode your message.

```
Running your message through the cypher…
gsrh rh olmtvi gvcg
```

> [!INFO]
>
> ## Code explainer
>
> - This uses `choice` in a loop. The loop runs until the user enters `e` or `f`.
> - If the user enters `e`, the message is encoded.
> - `f` is used later.
