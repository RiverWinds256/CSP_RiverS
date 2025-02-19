//River Stanley hello world update

#include <stdio.h>
void hello (char name [20]){
     printf("hello %s\n", name);
}
int main(void){
    char name[30];
    printf("Please enter your name:");
    scanf("%s", name);
    hello(name);
    hello("mary");
    hello("larry");
    hello("bob");
    hello("sue");

return 0;


}