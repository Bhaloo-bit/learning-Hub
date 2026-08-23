// Function && Recursion

#include<stdio.h>
// delcaration / prototype
void printhello();
void printgoodbye();

int main(){
    printhello();  // function call
    printgoodbye();
    return 0;
}

// function defenations 
void printhello(){
    printf("! Hello \n");
}

void printgoodbye(){
    printf("goodbye \n");
}
    


# include<stdio.h>

void welcome_user();

int main(){
    welcome_user();
    return 0;
}

void welcome_user(){
    char user;
    printf("Enter your country origin: ");
    scanf("%c", &user);

    if (user == "indian"){
        printf("Namaste", user);
    }
    else if ("user"== "french"){
        printf("Bonjour", user);
    }
    else
    {
       printf("citizens of the planet Earth");
    }
    
}



#include<stdio.h>

int sum();

int main(){
    int a, b;
    printf("enter first number: ", a);
    scanf("%d", &a);
    printf("enter second number: ", b);
    scanf("%d", &b);

    int s = sum(a,b);
    printf("sum of entered value: %d  \n ", s);
    return 0;

}


int sum(int x,  int y){
    return x + y;
} 

// Writing table 

#include<stdio.h>

void printTable();

int main(){
    int n;
    printf("enter number for table: ");
    scanf("%d", &n);

    printTable(n);

    return 0;
}

void printTable(int n){
    for (int i=1; i<11; i++){
        printf( " \n %d",i*n);
    }
    
}


#include <stdio.h>
#include <math.h>

void area_square();
void area_circle();
void area_rectangle();

int main(){
    int choice;
    printf("Enter your choice for area 1.circle 2.rectangle 3.square: ");
    scanf("%d", &choice);
    if (choice == 1){
         area_circle();
    }
    else if(choice ==2){
        area_rectangle();
    }
    else if (choice ==3) {
        area_square();
    }
    else {
        printf("thank for using");
    }
    
    return 0;
}

void area_square(){
    int side;
    printf("Enter the side of sq:");
    scanf("%d", &side);
    printf("area of square: %d", side*side);
    }

void area_circle(){
    float circle_area;
    int radius;
    printf("Enter the radius of cirlce:");
    scanf("%d", &radius);
    circle_area = 3.14 * radius* radius;
    printf("area of circle %f",circle_area);
}

void area_rectangle(){
    int length, breadth;
    printf("Enter the length of rec:");
    scanf("%d", length);
    printf("Enter the breadth of rec:");
    scanf("%d", breadth);
    printf("Area of recatangel %d", length*breadth);
}


///////////////// Recursion  ////////////////


#include<stdio.h>
void printHW(int count);
int main(){
    printHW(5);
    return 0;
}

void printHW(int count){
    if (count == 0){
        return;
    }
    printf("hello world \n");
    printHW(count-1);
}

// sum of first n  natural numbers

# include <stdio.h>
int sum_n(int num);

int main(){
    printf("sum is: %d", sum_n(5));
    return 0;
}

int sum_n(int num){
    if (num ==1){
        return 1;
    }
    int sumNm1= sum_n(num-1);
    int sumN = sumNm1 +num;
    return sumN;
}