// River Stanley FIZZBUZZ C


#include <stdio.h>
#include <math.h>

int main(void){
   
    int x;
    for(x=0; x<51; x++){
        if (x%5 ==0 && x%3 ==0){
            printf("fizzbuzz\n");
        }else if (x%5 ==0){
            printf("buzz\n");
        }else if (x%3 ==0){
            printf("fizz\n");
        }else{
            printf("%d\n",x);
        }
    }
return 0;
}