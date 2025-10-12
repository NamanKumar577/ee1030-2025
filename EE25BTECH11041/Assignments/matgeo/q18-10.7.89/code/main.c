#include <stdio.h>
#include <math.h>

struct Circle {
    double h, k, r;
};


struct Circle find_C1() {
    struct Circle c1;

    c1.h = 5.0;
    c1.k = 2.0;
    c1.r = 3.0;
    return c1;
}


struct Circle find_C2(struct Circle c1, double L) {
    struct Circle c2;
    c2.h = c1.h;
    c2.k = c1.k;
  
    double d = 3.0;
    c2.r = sqrt(pow(L/2, 2) + pow(d, 2));
    return c2;
}


void get_circles(double *h1, double *k1, double *r1, double *h2, double *k2, double *r2) {
    struct Circle c1 = find_C1();
    struct Circle c2 = find_C2(c1, 8.0);

    *h1 = c1.h; *k1 = c1.k; *r1 = c1.r;
    *h2 = c2.h; *k2 = c2.k; *r2 = c2.r;
}

