// River Stanley financial calculator C updated

#include <stdio.h>

int main(void){
    printf("welcome to the financial calculator\n");

    float income, rent, utilities, groceries, transportaition;

    printf("what is your income? ");
    scanf("%f", &income);

    printf("what is your rent? ");
    scanf("%f", &rent);

    printf("what is your utilities cost? ");
    scanf("%f", &utilities);

    printf("what is your groceries cost? ");
    scanf("%f", &groceries);

    printf("what is your ransportaition cost? ");
    scanf("%f", &transportaition);
  

    float savings=income*0.1;
    float spending=income-rent-utilities-groceries-transportaition-savings;
    float rentpercent=rent/income*100;
    float utilitiespercent=utilities/income*100;
    float groceriespercent=groceries/income*100;
    float transportationpercent=transportaition/income*100;


     printf("Your rent is %.2f dollars which is %.2f percent of your income\n\n", rent, rentpercent);

     printf("Your utilities cost is %.2f dollars which is %.2f percent of your income\n\n", utilities, utilitiespercent);

     printf("Your groceries cost is %.2f dollars which is %.2f percent of your income\n\n", groceries, groceriespercent);

     printf("Your transportaition cost is %.2f dollars which is %.2f percent of your income\n\n", transportaition, transportationpercent);
     
     printf("Your ideal savings would be %.2f which is 10 percent of your income\n\n", savings);

    printf("Your leftover spending money is %.2f dollars\n\n", spending);

return 0;