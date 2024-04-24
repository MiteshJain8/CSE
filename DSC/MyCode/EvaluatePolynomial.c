#include <stdio.h>
#include <math.h>
int main() {
    int degree;
    printf("Enter the degree of the polynomial: ");
    scanf("%d", &degree);

    int coefficients[degree + 1];
    printf("Enter the coefficients of the polynomial (starting from the highest degree): ");
    for (int i = degree; i >= 0; i--) {
        scanf("%d", &coefficients[i]);
    }

    int x;
    printf("Enter the value of x: ");
    scanf("%d", &x);

    int result = 0;
    for (int i = degree; i >= 0; i--) {
        result += coefficients[i] * pow(x, i);
    }

    printf("The value of the polynomial at x = %d is %d\n", x, result);

    return 0;
}
