Image by 
        Victoria M. Gardner (Shutterstock), Used under license
      

Hangman is a (somewhat macabre) word-guessing game that can
    be played by two people. Player�**1** thinks of a word consisting of
    **n** letters, and draws a
    row of **n** dashes on a
    piece of paper. These dashes correspond to the letters of the
    word, in the same order. Player�**2** then attempts to discover the word
    by making a sequence of letter guesses. For each letter guessed
    by Player�**2**:


If the letter occurs one or more times in the word,
        Player�**1** writes
        the letter above each corresponding dash.


If the letter does not occur in the word,
        Player�**1** adds
        one component to a drawing of a stick-figure man hanging on
        a gallows. The drawing (initially empty) has **10** possible components: base,
        vertical beam, horizontal beam, rope, head, torso, right
        leg, left leg, right arm, left arm.


If Player�**2**
    guesses all the letters in the word before the drawing of the
    hanging man is complete, then Player�**2** wins (and Player�**1** loses). Otherwise,
    Player�**2** loses (and
    Player�**1** wins).
Ned loves playing hangman, especially as
    Player�**2**, but he
    finds that he is not a very good letter guesser. To improve his
    chances, he decides to adopt a new strategy. For each word
    selected by Player�**1**, Ned chooses a random permutation
    of the letters of the alphabet, and then simply guesses letters
    in that order until he either wins or loses. Given the word and
    Ned�s permutation of the alphabet, determine the outcome of the
    game.
Input
The input consists of two lines representing a single game
    of Hangman. The first line contains the word to be guessed, a
    non-empty string of uppercase English alphabet letters
    (A�Z) of
    maximum length **16**. The
    second line contains a permutation of the **26** letters of the English alphabet,
    also uppercase.
Output
If Ned wins the game by guessing letters in the order given
    by the permutation (proceeding from left to right), output
    �WIN�. Otherwise, output �LOSE�.


Sample Input 1
Sample Output 1



HANGMAN
ABCDEFGHIJKLMNOPQRSTUVWXYZ



WIN






Sample Input 2
Sample Output 2



BANANA
ABCDEFGHIJKLMNOPQRSTUVWXYZ



LOSE






Sample Input 3
Sample Output 3



RAINBOWS
USIANBVLOJRKWXZCTQGHPFMYDE



WIN