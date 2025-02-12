// River Stanley Name Decorator 


#include <stdio.h>
#include <strings.h>

int main(void){
    printf("welcome to name decorator\n");
     char name[50]; 
     char decor1[] = "<<<<<<";
     char decor2 []= ">>>>>>";
     printf("Please enter your name :");
    scanf("%s", name);
    strcat(decor1,name);
    strcat(decor1, decor2);

    printf("%s",decor1);

    


return 0;
}

