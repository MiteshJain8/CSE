#include <stdio.h>

#define COMPARE_EXPONENT(a, b) ((a) > (b) ? 1 : ((a) < (b) ? -1 : 0))

typedef struct {
    float coef;
    int expo;
}Poly;

void addPolynomials(Poly p1[], int n1, Poly p2[], int n2, Poly p3[], int *n3) {
    int i = 0, j = 0, k = 0;
    
    while (i < n1 && j < n2) {
        switch (COMPARE_EXPONENT(p1[i].expo, p2[j].expo)) {
            case -1:
                p3[k].coef = p2[j].coef;
                p3[k].expo = p2[j].expo;
                j++;
                k++;
                break;
            case 0:
                p3[k].coef = p1[i].coef + p2[j].coef;
                p3[k].expo = p1[i].expo;
                i++;
                j++;
                k++;
                break;
            case 1:
                p3[k].coef = p1[i].coef;
                p3[k].expo = p1[i].expo;
                i++;
                k++;
        }
    }
    
    while (i < n1) {
        p3[k].coef = p1[i].coef;
        p3[k].expo = p1[i].expo;
        i++;
        k++;
    }
    
    while (j < n2) {
        p3[k].coef = p2[j].coef;
        p3[k].expo = p2[j].expo;
        j++;
        k++;
    }
    
    *n3 = k;
}

int main() {
    int n1, n2, n3;
    
    printf("Enter the number of terms in the first polynomial: ");
    scanf("%d", &n1);
    
    Poly p1[n1];
    
    printf("Enter the coefficients and exponents of the first polynomial:\n");
    for (int i = 0; i < n1; i++) {
        scanf("%f%d", &p1[i].coef, &p1[i].expo);
    }
    
    printf("Enter the number of terms in the second polynomial: ");
    scanf("%d", &n2);
    
    Poly p2[n2];
    
    printf("Enter the coefficients and exponents of the second polynomial:\n");
    for (int i = 0; i < n2; i++) {
        scanf("%f%d", &p2[i].coef, &p2[i].expo);
    }
    
    Poly p3[n1 + n2];
    
    addPolynomials(p1, n1, p2, n2, p3, &n3);
    
    printf("Resultant polynomial after addition:\n");
    for (int i = 0; i < n3-1; i++) {
        printf("%.2f x^%d + ", p3[i].coef, p3[i].expo);
    }
    printf("%.2f x^%d", p3[n3-1].coef, p3[n3-1].expo);
    return 0;
}
