#include <stdio.h>

void trisec(double x1, double y1, double x2, double y2, double* x, double* y){
    *x= (x1+2*x2)/3;
    *y= (y1+2*y2)/3;

}