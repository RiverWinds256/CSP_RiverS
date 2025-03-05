// River Stanley loops notes C


#include <stdio.h>

int main(void){
    

//1 What is a loop? 
    //a section of code repeated mulyiple times

//2 What are the two types of loops?
    //while
//
// int start=0:
// while (start<5){
//    printf("hello")
// }


 //for loop
//
// int q; {
// for(q=0;q<5;q++)
// printf("%d\n", q);
// }   

//3 What is iteration

    //repeat something wih minor chnages each time 

//4 What are (array)lists?
    //A array is a varible holfing multiple vaules 
    
//8 How do you make lists in C?
    //arrays must be same data type
 int grades[] = {88, 97, 100, 70, 72, 99, 61};
    // set data type, after naming it but [], list must be surrounded by {}, commans between each item
    //ptint a single item
    printf("Csp grades: %d\n", grades[2]);
    //size of lsists in bystes
    int length = sizeof(grades)/sizeof(grades[0]); 
    printf("%d/n", length);
    //changing a item
    grades[2] = 95;
    //arrays with strings
    //first [] set the lench of the list, second sets the length of each string
    char movies[][20] = {"cars", "treausure plant", "an american tale", "marley and me", "the av"};
    int mlength = sizeof(movies);
    printf("the movie is %s\n", movies[1]);

//9 How do you make for loops in C?
    //set iterator (x, I), keeps track of timed loop has looped
    int x;
    // in (starting point; ending point; what we count by)
    for(x=0; x<=10; x+2){
    printf("%d\n", x);
    }
    int m; 
    for(m=0;m<mlength;m++){
        printf("s\n", movies [movies[m]]);
    }
//10 How do you make while loops in C?
int w = 0;//start point
while(w,100){ //end point
    printf("%d\n",w);
    w += 10;//count by
}






return 0;
}

