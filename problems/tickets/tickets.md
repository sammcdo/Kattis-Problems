The concert promoters of the Bon Jovi Tour 2013 have decided
    to sell tickets for the concerts in lotteries. The rules are
    quite simple. For every concert, fans can apply online for
    tickets. In response they receive unique reservation numbers.
    It is important that for each concert the numbers distributed
    online are consecutive nonnegative integers starting with 0.
    Unfortunately, as the organizers tried to draw reservation
    numbers randomly, they discovered that the pseudo random
    generator they used is extremely slow. To minimize the number
    of calls to the generator, they invented a peculiar but fair
    enough way to distribute tickets.
As soon as the reservation for a concert is finished, the
    organizers ascertain the number of submissions **M** and draw one random integer
    **Z** from **\{ 0, \ldots , M-1\} ** (remember,
    fans get integers from **0**
    to **M-1**). Integer
    **Z** is the only object the
    organizers have to draw randomly! Finally, to complete the
    selection rules the organizers determine an integer
    **r>0** which has a
    direct impact on the number of selected tickets.
Now, using **Z** and
    **r**, tickets are selected
    deterministically as follows. For the reservation numbers
    **0, \ldots , M-1** and the
    number **Z**, their decimal
    representations of length **n** are considered, where **n** is the length of the
    representation of **M-1**
    without leading zeros. Thus, the decimal representations of the
    remaining numbers are padded on the left with leading zeros, if
    needed. If **z_{1}\ldots
    z_{n}** denotes such a representation for **Z**, then the holder of a number
    **a_{1}\ldots a_ n** gets
    the ticket if and only if the strings **z_{1}\ldots z_{n}** and **a_{1}\ldots a_ n** have a common
    contiguous substring of length **r** or more which starts at the same
    position. Speaking formally, he or she gets the ticket if there
    exists an index **i**, with
    **1\le i\le n-r+1**, such
    that **z_ i\ldots z_{i+r-1} = a_ i
    \ldots a_{i+r-1}**. For example, if **Z = 56743** and **r=3** then a fan with a reservation
    number **06740** gets a
    ticket, but a fan having **56143** does not.
Your task is to help the organizers to estimate, for given
    numbers **M**, **Z** and **r**, the exact number of tickets
    selected in such a way.
Input
The first line contains the number of concerts **C**, with **1\le C \le 5000**. Then follow
    **C** lines, each containing
    three integers **M, Z,** and
    **r**, with **0<M\le 10^{18}**, **0\le Z \le M-1** and **r\ge 1**. You may safely assume that
    **r** is smaller or equal to
    the length of the decimal representation of **M-1**.
Output
For each concert, print one line containing the number of
    tickets selected during the ticket draw.


Sample Input 1
Sample Output 1




8
89 32 1
67 49 1
67 45 2
1000 23 1
1000 401 2
1000 54 2
3571 2 3
3571 976 3




18
15
1
271
19
19
13
12