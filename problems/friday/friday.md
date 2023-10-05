On the planet Htrae Friday the 13th is a lucky day. You
    are going there on the next space ship and want to calculate
    how many times it happens during a given year. Unfortunately
    they change their calendar every year. Every year starts on a
    Sunday, but other than that, they change everything. They have
    released a list of calendar specifications for the next few
    years. A calendar specification consists of the total number of
    days in the year, the number of months in the year, and the
    number of days in each of the months.
Your task is to figure out how many times there will be
    Friday the 13th based on the calendar specifications.
Input
The first line of the input consists of a single integer,
    **T**, the number of test
    cases.
    The first line of each of the **T** test cases is a line with two
    space separated integers, **D** and **M**, the total number of days in the
    year and the number of months in the year respectively. The
    second line of each test case consists of **M** space separated integers,
    **d_ i**, the number of days
    in each month.


**1 \leq T \leq
        20**


**1 \leq M \leq D \leq
        1000**


**1 \leq d_ i \leq
        100**


**\sum (d_ i) =
        D**


Output
For each test case, output the number of Friday the 13ths in
    the specified year.


Sample Input 1
Sample Output 1




3
20 1
20
40 2
21 19
365 12
31 28 31 30 31 30 31 31 30 31 30 31




1
2
2