You are given an array of of **n** integers **a_1, a_2, \ldots , a_ n**. An array is
    almost sorted if it is possible to reverse a continuous
    subarray to obtain an ascending sorted array. In other words,
    an array is almost sorted if there exists **1\leq i\leq j\leq n** such that
    **a_1\leq a_2\leq \ldots \leq
    a_{i-1} \leq a_ j \leq a_{j-1}\leq \ldots \leq a_{i+1} \leq a_
    i \leq a_{j+1} \leq a_{j+2}\leq \ldots \leq a_ n**
If **a** is almost
    sorted, output “Yes”, otherwise output “No” (both without
    quotes).
Input
The first line of each test case contains one integer n
    **(2\leq n\leq 300\, 000)**
    — the length of the array.
The second line of each test case contains n integers
    **a_1,a_2,\ldots ,a_ n**
**(1\leq a_ i\leq 10^9)** —
    the array given in the problem.
Output
Output “Yes” if **a** is
    almost sorted, “No” otherwise.


Sample Input 1
Sample Output 1



4
1 3 2 4



Yes






Sample Input 2
Sample Output 2



4
1 4 2 3



No