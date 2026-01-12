<h2 class="c-project-heading--task">Add text to the file</h2>
--- task ---
Add your own secret message to the `input.txt` file. 
--- /task ---

Find `input.txt` in the file tab. Delete the `replace with your message` text and enter your own text. 

![screenshot of the project file tab with the input file open for editing](images/input-file.png)

**Test:** Run your code to see if it displays your encoded message after entering the letter 'c' when prompted. 

Add image **

<div class="c-project-output">
<pre>Enter c to encode/decode text, or f for frequency analysis: 
c
Running your message through the cypher…
svool gsrh rh z gvhg</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging
**Debug:** Your encoded message doesn't look exactly like the message in the screenshot:
- This is normal. This is the encoded message for the text `replace with your message`. Your message will be different.

**Debug:** You see an error message that says `TypeError: get_text() takes exactly 1 arguments`:
- Check that you have entered `input.txt` inside the round brackets on line 57

**Debug:** You see an `Indentation error` message:
- Check that you have correctly indented all of your new code. Revisit the tasks above to check. 

</div>
