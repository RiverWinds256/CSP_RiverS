// River Stanley conditional notes


#include <stdio.h>
#include <string.h>
char name[]="Vienna";
int num[];
int main(void){
//#10 How do you write an if statement in C?
if (strcmp(name,"vienna") == 0){ //strcmp means string coparsion, when the outcome is 0, the strings are the same
    printf("hello mrs Larose");
}




//11 How do you write else statements in C?


    printf("hello %s");


printf("how many siblings do you have");
scanf("%d", &num );
//12 How do you write elif/ else if statements in C?
if(num==0){
    printf("you are a only child");
}else if (num<=2){ 
    printf("you have a couple of siblings");
}else if (num<=5){
    printf("word");

}else {
    printf("print");
}




//13 How do you write the 3 logical operators in C?
// && = and
// || = or
//!=not

if (num==7 || num== 13){
    
    printf("%d is a unlucky number", num);



}else if(num <10 && num > 5){
    if(num == 12){ 
    printf("that a dozen");

}
    

else
printf("you must ")

else if (!num= <10 )

return 0;
}

