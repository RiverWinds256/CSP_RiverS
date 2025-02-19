// River Stanley, silly sentences C


#include <stdio.h>

char word1[20];
char word2[20];
char word3[20];

int main(void){
printf(" Welcome to silly sentences!\n All answers must be one word. \n ");

printf("What is one negative word that people may use describe you?\n ");
scanf("%s", word1);

printf(" In ONE word what is something you do everyday?\n ");
scanf("%s", word2);

printf(" What is one chore you do everyday?\n ");
scanf("%s", word3);

printf("\nThe tyrannosaurus rex would always wear a toupee beacuase he felt %s because he didnt have hair like the other dinosaurs.\n So whenever he went to %s he would wear his toupee to hid his bald head.\n The only time he doesnt wear histoupee is when he %s because being bald in helpful in that chore.", word1, word2, word3);

return 0;
}

