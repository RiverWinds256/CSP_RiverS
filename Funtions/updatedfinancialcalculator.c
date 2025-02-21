// River Stanley financial calculator C updated

#include <stdio.h>
void info( float cost, float income, char* type){
    float percent = cost/income*100;
    printf("your %s is %.2f dollars which is %.2f percent of your income\n", type, cost, percent);
}

float spend(char* type){
    float vaule;
    printf("what is your %s cost? ",type);
    scanf("%f", &vaule);
    return vaule;
}

int main(void){
    printf("welcome to the financial calculator\n");

    float income, rent, utilities, groceries, transportaition;

    printf("what is your income? ");
    scanf("%f", &income);

    rent=spend("rent");
    utilities=spend("utilities");
    groceries=spend("groceries");
    transportaition=spend("transportation");
  
    float savings=income*0.1;
    float spending=income-rent-utilities-groceries-transportaition-savings;

    info(rent, income, "rent");
    info(utilities, income, "utilities");
    info(groceries, income, "groceries");
    info(transportaition, income, "transportation");

     printf("Your ideal savings would be %.2f which is 10 percent of your income\n\n", savings);

    printf("Your leftover spending money is %.2f dollars\n\n", spending);

return 0; }