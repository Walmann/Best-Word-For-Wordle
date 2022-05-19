# What is this?

This is a done-in-a-day-that-became-a-week-or-more project i came up with for scoring the best starting word in Wordle (I know I'm late).
I won't say that this is a perfect way of doing this, but i thought it would be a fun exercise :)

## What does it do?

By running the `GetBestWord.py` file, you will iterate through the word list file and give each word a score. \
This score is based on how many times X letter appear in Y spot.

## How does this work?

### **GetBestWord.py**

The `GetBestWord.py` file does 3 things.

1. First it will run through the word list file that is set in the script, and give each letter in X spot a score. <br />
   This score is based on how many times this letter appear in that column (Index, starts at 0).
   > The score is set from 0 to 25

</br>

### **Example:**

| Word           | Index 0       | Index 1                 | Index 2                 | Index 3      | Index 4       |
| -------------- | ------------- | ----------------------- | ----------------------- | ------------ | ------------- |
| arose          | A 1           | R 1                     | O 1                     | S 1          | E 1           |
| adder          | A 1           | D 1                     | D 1                     | E 1          | R 1           |
| seder          | S 1           | E 1                     | D 1                     | E 1          | R 1           |
| Total</>Points | A 2 </br> S 1 | R 1 </br> D 1 </br> E 1 | 0 1 </br> D 1 </br> E 1 | S 1 </br>E 2 | E 1 </br> R 2 |

2. It will then go through all the words and give them a score based on which letters the word consists of.
   - If the letter contains two or more of the same letter, that letter will only count once.

<!-- | --- | --- | --- | --- | --- |
| A | R | O | S | E |
| 19 | 23 | 23 | 22|24| -->

| Letters          | A   | R   | O   | S   | E   |
| ---------------- | --- | --- | --- | --- | --- |
| Letter</br>Score | 19  | 23  | 23  | 22  | 24  |

Total Score for Arose: 111

| Letters          | C   | A   | D   | D      | Y   |
| ---------------- | --- | --- | --- | ------ | --- |
| Letter</br>Score | 23  | 25  | 15  | ~~15~~ | 2   |

Total Score for Caddy: 065

> Notice how the second D did not count

3. Sort this list by Score, and Voila! You have the `Result.csv` file as provided!

### **GuessTheWord.py**

This script goes through these instructions in a loop:

1.  Find the word that fits the current attributes. An example of this would be; Has to contain a "H" in index 1 (Green Letters), and the letters "E" and "L" somewhere (Yellow letters).
    - On first run, this is the first entry in `Result.txt`.
2.  After you enter that word into Wordle, it will ask which letters became green, and which became yellow, and add them to separate lists. The rest of the letters in the current word, get automatically added to it's own list.
3.  Updates the green and yellow lists, to make sure that there are no yellow entries in the green list.
4.  For every word it guesses, it will add these to another list, so that we don't get repeated guesses.
5.  And repeat the loop.

# Which word list too choose?

If you are going to use this tool on the NYTimes site, use the `wordlistNYTimes.txt` \
For all my testing i have used [Infinite Wordle by Greg Cameron](https://gregcameron.com/infinite-wordle/) with the `wordlistInfiniteWordle.txt` file.

# In the future

Some ideas that can be created at a later date:

1. [x] A solver that gives advice about which word you should guess next. <br />
       This could be done like this:

   [x] Give the top scoring word as suggestion \
   [x] Ask which letters became green, yellow, and black (in a for loop or something.) \
   [x] Give next suggestion based on this information. \

2. [ ] Webapp?
   1. infinite Wordle, to see exactly how accurate this method is?
   2. Might be a good way to start learning reactJS?
3. [ ] Make this more user friendly:
   1. Select desired word list at beginning
      - Default selection
   2. Make suggested words easier to notice inside terminal (Different colors etc.)
