# What is this?

This is a done-in-a-day project i came up with for scoring the best starting word in Wordle (I know I'm late).
I won't say that this is a perfect way of doing this, but i thought it would be a fun exercise :) 

## What improvments can be done:
I could add a way to retract some score if a letter apear twice in the same word. I might update the script for this later.

## What does it do?
By running the `Script.py` file, you will iterate through the `wordlist.txt` file and give each word a score. \
This score is based on how many times X letter appear in Y spot.


## How does this work?
The `Script.py` file does 3 things.

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

3. Sort this list by Score, and Voila! You have the `Result.txt` file as provided!