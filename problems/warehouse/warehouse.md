Photo by 
        Random Retail


Elvira is processing shipments for the Christmas season!
    There are various shipments of toys coming into her warehouse
    throughout the day, and her boss wants a summary report at the
    end. Each shipment consists of some number of a single kind of
    toy.
The summary report is an aggregated list of all the toys
    that arrived at the warehouse over the day. The boss is most
    interested in the biggest sellers, so toys should be sorted in
    decreasing order of count. If the warehouse received the same
    number of two kinds of toys, sort them in alphabetical
    order1.
Input
The first line of input contains the number of test cases,
    **T** (**1 \le T \le 100**).
Each test case begins with a line containing an integer,
    **N** (**1 \le N \le 100**). This indicates
    that **N** shipments are
    coming in for processing. Each of the next **N** lines describes a single shipment.
    The line contains a string and an integer, the name of the toy
    and how many of that toy are in the given shipment. The name of
    a toy is a string of at most **10** lowercase letters (a–z) and between
    **1** and **10** toys arrive in a given
    shipment.
Output
For each test case, output **K**, the number of unique toys that
    have arrived in the warehouse.
Then output **K** lines,
    each containing the name of a toy and how many of that toy that
    have arrived, summed up over all the shipments. Output toys in
    decreasing order of count, breaking ties alphabetically.


Sample Input 1
Sample Output 1



2
4
furby 4
elmo 5
furby 1
kirby 10
2
funfungame 1
funfun 1



3
kirby 10
elmo 5
furby 5
2
funfun 1
funfungame 1