# What is this?

This is a done-in-a-day project i came up with for scoring the best starting word in Wordle (I know I'm late).
I won't say that this is a perfect way of doing this, but i thought it would be a fun exercise :) 


## What does it do?
By running the `GetBestWord.py` file, you will iterate through the `wordlist.txt` file and give each word a score. \
This score is based on how many times X letter appear in Y spot.


## How does this work?
The `GetBestWord.py` file does 3 things.

1. First it will run through the `wordlist.txt` file and give each letter in X spot a score. <br /> This score is based on how many times this letter appear in X spot. 
> The score is set from 0 to 25

### Example:
```
Short wordlist:
acers
adder
seder

In this example "a" in row 1 will get 2 points, as there are 3 ocurences. and "s" will get 1 point.
The letters "c", "d", and "e" in row 2 all get 1 point.
The letter "e" will get 2 points etc.
```

2. It will then go through the word list again and rate each word like this:

```
acers

a = 02 points,
c = 16 points,
e = 15 points,
r = 22 points,
s = 10 points,

Combine these and you get 83 points.

```
> EDIT: If the same letter appear twice in a word, the second letter wont account towards the Word Score.

3. Sort this list by Score, and Voila! You have the `Result.csv` file as provided!

# Wich wordlist too choose?
The original list i used was the `wordlistAllowedGuesses.txt`, but this was changed to `wordlistNYTimes.txt` later. <br />
But you can use whichever you want.

# In the future
Some ideas that can be created at a later date:
1. ~~A solver that gives advice about wich word you should guess next. <br />
   This could be done like this:~~
   - ~~Give the top scorring word as suggestion~~
   - ~~Ask wich letters became green, yellow, and black (in a for loop or something.)~~
   - ~~Give next suggestion based on this information.~~
  

Nothing right now. </br>
If i get the inspiration, mabye turn it into a webapp?