#include <math.h>
#include<stdio.h>

float test(float x, float y){
    return (hypot(x, y));
}


void main(){
    float result;
    result = test(1,1);
    printf("%f\n", result);
}






