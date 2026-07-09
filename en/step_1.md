## Reverse text

Print the alphabet and then reverse it.

Add the Python code below to create `alphabet` and `backwards`.

The code uses `[::-1]` to reverse the text.

```python filename="main.py" line_numbers="true" line_number_start="1" line_highlights="4-6"
from pygal import Bar
from frequency import english

alphabet = ' abcdefghijklmnopqrstuvwxyz '
backwards = alphabet[::-1]
print(alphabet) # print to check that it works
```

## Now run your code

You should see the alphabet printed in the output.

Try printing **backwards** to see it in reverse.

```
abcdefghijklmnopqrstuvwxyz
```

> [!TIP]
>
> Two libraries are already imported into your project: `pygal` and `frequency`. You can see them at the top of your code.
