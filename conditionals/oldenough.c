// River Stanley old enough C


#include <stdio.h>

int main(void){
    int age;
    printf ("How old are you? ");
    scanf("%d", & age);

    if (age >=18)   
        printf("You are old enough to go to school, get a learner permit, drive and vote.");

    else if (age >=16) 
        printf("You are old enough to go to school, get a learner permit, drive, but not vote");    

    else if (age >=15)
        printf("You are old enough to go to school, get a learner permit, but not drive and vote.");

    else if (age >5)
        printf("you are old enough to go to school, but not old enough get a learners permit, drive, or vote.") ; 
    
    else
        printf("you are not old enough go to school, get a learners permit, drive, or vote");
    

return 0;
}