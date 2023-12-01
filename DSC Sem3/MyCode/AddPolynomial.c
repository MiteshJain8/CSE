#include <stdio.h>

struct polynomial
{
    int coef;
    int exp;
};

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int n1, n2;
    printf("Enter the no of terms in ist polynomial: ");
    scanf("%d", &n1);
    printf("Enter the no of terms in 2nd polynomial: ");
    scanf("%d", &n2);
    int n3 = n1 + n2;
    struct polynomial p1[n1];
    struct polynomial p2[n2];
    struct polynomial p3[n3];
    printf("Enter the coefficients and exponents of terms in 1st polynomial: ");
    for (int i = 0; i < n1; i++)
    {
        scanf("%d %d", &p1[i].coef, &p1[i].exp);
    }
    printf("Enter the coefficients and exponents of terms in 2nd polynomial: ");
    for (int i = 0; i < n2; i++)
    {
        scanf("%d %d", &p2[i].coef, &p2[i].exp);
    }
    for (int i = 0; i < n1 - 1; i++)
    {
        int max = i;
        for (int j = i + 1; j < n1; j++)
        {
            if (p1[j].exp > p1[max].exp)
            {
                max = j;
            }
        }
        swap(&p1[i].exp, &p1[max].exp);
        swap(&p1[i].coef, &p1[max].coef);
    }
    for (int i = 0; i < n2 - 1; i++)
    {
        int max = i;
        for (int j = i + 1; j < n2; j++)
        {
            if (p2[j].exp > p2[max].exp)
            {
                max = j;
            }
        }
        swap(&p2[i].exp, &p2[max].exp);
        swap(&p2[i].coef, &p2[max].coef);
    }
    printf("The 1st polynomial is: ");
    for (int i = 0; i < n1; i++)
    {
        printf("%dx^%d + ", p1[i].coef, p1[i].exp);
    }
    printf("\nThe 2nd polynomial is: ");
    for (int i = 0; i < n2; i++)
    {
        printf("%dx^%d + ", p2[i].coef, p2[i].exp);
    }
    int i = 0, j = 0, k = 0;
    while (i < n1 || j < n2)
    {
        if (p1[i].exp == p2[j].exp)
        {
            p3[k].coef = p1[i].coef + p2[j].coef;
            p3[k].exp = p1[i].exp;
            i += 1, j += 1, k += 1;
        }
        else if (p1[i].exp > p2[j].exp)
        {
            p3[k].coef = p1[i].coef;
            p3[k].exp = p1[i].exp;
            i += 1, k += 1;
        }
        else
        {
            p3[k].coef = p2[j].coef;
            p3[k].exp = p2[j].exp;
            j += 1, k += 1;
        }
    }
    printf("\nThe sum of the polynomials is: ");
    for (int x = 0; x < k - 1; x++)
    {
        printf("%dx^%d + ", p3[x].coef, p3[x].exp);
    }
    printf("%dx^%d", p3[k - 1].coef, p3[k - 1].exp);
    return 0;
}