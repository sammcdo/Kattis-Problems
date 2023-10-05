Ordinarily, when you got to an amusement park, you pay for
    your ticket, you ride as many rides as you like and then you
    leave at the end of the day. If you leave early or get there
    late you don’t get a discount. Bob’s Pretty Safe Playland is
    ramping up a new plan to help attract more customers; you pay
    in proportion to the amount of time you spend in the park.
    Although Bob expects to lose some money on customers who just
    stop by for a couple of rides, he expects to make it back on
    the people who end up staying for a long time.
Under Bob’s new pricing scheme, customers pay **\** 0.10** for each minute they spend
    in the park. Bob will send a bill after a few days, and
    customers can can pay at their convenience. Bob will use a
    computer system to manage billing. It will notice when each
    customer enters and leaves. For each day, it will generate a
    report of how much each customer owes. Your job is to write
    that program.
Input
Input consists of logs for up to **20** days. The log for a given day
    starts with the word “OPEN” and ends
    with the word “CLOSE”. Between these
    entries are lines describing when various customers enter and
    leave the park. When a customer enters the park, it is recorded
    with a line like “ENTER Timmy 25”.
    This indicates that Timmy entered the park **25** minutes after it opened. When a
    customer leaves the park, it is recorded like: “EXIT Timmy 130”. This indicates that Timmy left
    the park **130** minutes
    after it opened. In this case, Timmy spent **105** minutes in the park.
All distinct customers have different names consisting of
    **1** to **20** lower or uppercase (a-z)
    characters. At most **20**
    different customers visit the park during a day. Entry and exit
    times are all in the range **[0,800]**. Log entries for each day
    are sorted by minute. The logging system is foolproof in that
    each enter has a matching exit some time later the same day.
    There are no ENTER reports for a
    customer who is already in the park, and there are no
    EXIT reports for a customer who was
    not previously in the park. At the start and the end of each
    day, the park is empty of customers.
Output
For each day, print out a report like the following. Give
    the total bill for each customer. Sort your report
    alphabetically by customer name and leave a blank line between
    reports for consecutive days.


Sample Input 1
Sample Output 1




OPEN
ENTER Sam 0
ENTER Alice 15
EXIT Sam 20
EXIT Alice 700
CLOSE
OPEN
ENTER Sam 5
ENTER Alice 10
EXIT Sam 20
EXIT Alice 35
ENTER Sam 700
EXIT Sam 710
CLOSE




Day 1
Alice **68.50
Sam **2.00

Day 2
Alice **2.50
Sam **2.50