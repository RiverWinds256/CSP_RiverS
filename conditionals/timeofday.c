// River Stanley, getting the time


#include <stdio.h>
#include <time.h>

int main(void){
    printf("Welcome, ");
    time_t seconds;
    seconds = time(NULL);
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    time_t now = time (NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;

if (hour<12){
    printf("good morning\n");
    
}else if (12<=hour<18){
    printf("good afternoon\n");
}else {
    printf("good evening\n");
}


return 0;
}
