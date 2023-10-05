When doing competitive programming, one can sometimes fall
    into an almost trance-like state. Minutes becomes hours, hours
    becomes days, and suddenly you don’t even know for how many
    days you have been programming! Of course, this just became
    another problem for you to solve by writing programs. By
    looking at the current time with intervals of less than an
    entire day, you can always compute the current date, relative
    to some starting date.
Task
Your task is to write a program in C++ that supports two
    operations:


void lookAtClock(int hours, int
        minutes) – take a report on the current time in
        24-hour format (i.e. **0 \le
        hours < 24** and **0
        \le minutes < 60**).


int getDay() – return the
        number of days that you have been programming.


Before the first call to any function, it is 00:00 on day
    **1**. When getDay is called, assume that it is called
    immediately after the last invocation to lookAtClock, so that the number of days is the
    same on the two calls.
It is guaranteed that the function lookAtClock is called at least once every
    **23** hours and
    **59** minutes. Thus, the
    first call will always be a time on day **1**. At least 1 minute will have
    elapsed between calls too. The two functions will together be
    called at most **1\, 000**
    times.
Template
You can use the template in countingdays.cpp from the Attachments menu when
    implementing your program. When submitting your code, send in
    only this file.
Testing
First, download the file countingdays.h from the Attachments menu and
    save it in the same place as your solution. That file calls
    your program with a fixed test case and reports whether it was
    correct.