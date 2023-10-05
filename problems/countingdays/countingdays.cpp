#include "countingdays.h"

int prevHour = 0;
int prevMin = 0;
int days = 1;

void lookAtClock(int hours, int minutes) {
    if (hours < prevHour) {
        days++;
    }
    if (hours == prevHour && minutes < prevMin) {
        days++;
    }
    prevHour = hours;
    prevMin = minutes;
}

int getDay() {
    return days;
}