// River Stanley, getting the time


#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds; //time since jan 1 1970
    seconds = time(NULL);
    //printf("seconds jan 1st 1970 = %d", seconds);

    //current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //printf("Current time and date is %s\n", asctime(timeinfo));

    //current hour 
    time_t now = time (NULL);

    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;

    printf("%d\n", hour);


return 0;
}
