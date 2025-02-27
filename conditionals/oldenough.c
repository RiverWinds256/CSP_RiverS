// River Stanley old enough C


#include <stdio.h>

int main(void){
    int age;
    printf ("How old are you? ");
    scanf("%d", & age);

    if (age >=18){  
        printf("You are old enough to vote.");
    

    }else if (age >=16){
        printf("You are old enough to drive.");    

    }else if (age >=15){
        printf("You are old enough to get a learner permit.");

    }else if (age >5){
        printf("you are old enough to go to school.") ; 
    
    }else{
        printf("you are not old enough go to school");
    }
    

return 0;
}