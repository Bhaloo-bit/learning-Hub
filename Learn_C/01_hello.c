/*#include<stdio.h>
int main(){
    int x;
    int y;
    
    printf("Enter the value of x:");
    scanf("%d",&x);
    printf("Enter the value of y:");
    scanf("%d",&y);
    
    int result = x * y;
    printf("result %d", result);

    return 0;
}*/

// if else in C

/*#include<stdio.h>
int main (){
    int age;
    printf("Enter your age : ");
    scanf("&d",age);

    /*if(age < 18){
        printf("notable to vote");
    }
    else {
        printf("able to vote \n");
    }
    printf("thankyou \n");
    
    // Ternary Operator
    // $ condition ? dosomething if True: dosomething if False;
    age >= 18 ? printf("adult \n") : printf("not adult");
    return 0;
}
*/



/* switch 
    switch(number(number/char)){
        case 1://do something
            break;
        case 2://do something
            break;
        case 3://do something
            break;
    }
*/
/*
#include<stdio.h>
int main(){
    int day;
    printf("Enter day num (1-7): ");
    scanf("%d", &day);

    switch (day)
    {
        case 1:
            printf("Sunday");
            break;
        case 2:
            printf("Monday");
            break;
        case 3:
            printf("Tuesday");   
            break;
        case 4:
            printf("Wednesday");   
            break;
        case 5:
            printf("Thrusday");   
            break;
        case 6:
            printf("Friday");   
            break;
        case 7:
            printf("Saturday");   
            break;
        default : printf("not a valid day");
            break;
    };
    
    return 0;
    
}
*/
// program to check uppercase and lower case

/*#include<stdio.h>
int main(){
    char ch;
    printf("Enter between a-z or A_Z : ");
    scanf("%c", &ch);

    if(ch >= "A" && ch <= "Z"){
        printf("Alpha Uppercase");
    }
    else if (ch >= "a" && ch <="z") {
        printf("alpha is lower case");
    }
    else {
        printf("! Invalid Character");
    }

}
*/
// for loop syntax 
#include<stdio.h>
int main(){
    for (int i=0; i<=5; i++){
    printf("hello world \n");
    };
    for (char ch ='a'; ch <='z'; ch++){
        printf("%c\n", ch);
    };
    // $ while loop syntax
    
    int i = 0;
    while (i < 10){
        printf("learning C for cllg");
        i = i+1;
    }

    // do while loop syntax $
    /*int i_J = 0;
    do {
        printf("%d \n", i_J);

    }while(i_J >=5);*/

    int n;
    printf("enter any num: ");
    scanf("%d", &n);

    int sum = 0;
    for (int k= 0, j=n; k <=n, j>=1; k++, j--){
        sum = sum +k;
        printf("%d", j);
    }

    printf("%d", sum );

    
    return 0;
}







