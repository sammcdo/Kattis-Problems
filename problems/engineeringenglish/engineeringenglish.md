Engineers have taken over the university�s English
    department! As part of their plan to dominate the university,
    they have employed you to write their nefarious software. Their
    goal is to eliminate all duplicated words from all texts in the
    English department, because, as they say, �duplicated words are
    duplicated work� and �duplicated work wastes money.� Actually,
    what they would really say is �duplicated words are . work� and
    �. . wastes money�. This is what your program should do �
    remove all duplicate words and replace them with a period.
Input
Input is a textbook with at most **2\, 000** lines. Each line contains up
    to **100** characters.
    Punctuation does not appear (it has already been removed by
    another programmer); words are made up of up to **20** lower and uppercase characters
    (a�z). There are at most **20\,
    000** total words in the input. Each pair of adjacent
    words is separated by a single space. Case does not matter when
    comparing words for duplicates (i.e. �Book� and �book� and
    �bOoK� should be considered the same word). Input ends at end
    of file.
Output
Print each word the first time it appears, but thereafter if
    that word appears again print a period.


Sample Input 1
Sample Output 1




Engineering will save the world from inefficiency
Inefficiency is a blight on the world and its
humanity




Engineering will save the world from inefficiency
. is a blight on . . and its
humanity






Sample Input 2
Sample Output 2




he said that that that that that man used
was wrong




he said that . . . . man used
was wrong