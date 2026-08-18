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

#include<stdio.h>
int main (){
    int age;
    printf("Enter your age : ");
    scanf("&d",age);

    if(age < 18){
        printf("notable to vote");
    }
    else {
        printf("able to vote \n");
    }
    printf("thankyou \n");
    return 0;
}
