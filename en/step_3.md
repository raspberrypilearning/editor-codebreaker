## Make a secret code

Use a function to turn text into a secret message.

Under the `print(code)` line, add the code below.

```python filename="main.py" line_numbers="true" line_number_start="8" line_highlights="11-22"
code = {alphabet[i]: backwards[i] for i in range(len(alphabet))} # Create a dictionary to map the letters
print(code) # print to check that it works

# create the atbash function
def atbash(text):
    text = text.lower() # make lower case
    output = '' # Store secret message

    for letter in text:
        if letter in code:
            output += code[letter] # Swap each letter

    return output

print(atbash('hello world'))
```

## Now run your code

Check that `hello world` is encoded as `svool dliow`.

```
svool dliow
```

Try changing `'hello world'` to a different message. Make sure you use `'` around the text.

> [!INFO]
>
> ### What is Atbash?
>
> - Atbash makes the secret code
> - It uses the swapped letters from the dictionary to create new words
