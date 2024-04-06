#include <stdio.h>
#include <stdlib.h>
#define COMPARE(x, y) (x > y ? 1 : (x < y ? -1 : 0))
struct node
{
    int coeff;
    int expo;
    struct node *link;
};
typedef struct node *polyptr;

void attach(int coefficient, int exponent, polyptr *ptr)
{
    polyptr temp;
    temp = (polyptr)malloc(sizeof(struct node));
    temp->coeff = coefficient;
    temp->expo = exponent;
    (*ptr)->link = temp;
    *ptr = temp;
}
polyptr cpadd(polyptr a, polyptr b)
{
    polyptr c, lastC, startA;
    int sum, done = 0;
    startA = a;
    a = a->link;
    b = b->link;
    c = (polyptr)malloc(sizeof(struct node));
    c->expo = -1;
    lastC = c;
    do
    {
        switch (COMPARE(a->expo, b->expo))
        {
        case -1:
            attach(b->coeff, b->expo, &lastC);
            b = b->link;
            break;
        case 0:
            if (startA == a)
                done = 1;
            sum = a->coeff + b->coeff;
            if (sum)
                attach(sum, a->expo, &lastC);
            a = a->link;
            b = b->link;
            break;
        case 1:
            attach(a->coeff, a->expo, &lastC);
            a = a->link;
            break;
        }
    } while (!done);
    lastC->link = c;
    return c;
}
void printPoly(polyptr a)
{
    a = a->link;
    while (((a->link)->expo) != -1)
    {
        printf("%d x ^ %d + ", a->coeff, a->expo);
        a = a->link;
    }
    printf("%d x ^ %d", a->coeff, a->expo);
    printf("\n");
}
void readPoly(polyptr *a)
{
    *a = (polyptr)malloc(sizeof(struct node));
    polyptr temp;
    (*a)->expo = -1;
    temp = *a;
    int expo;
    int n;
    int coeff;
    int i = 0;
    printf("Enter number of terms: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter coeff and exponent %d", i);
        scanf("%d%d", &coeff, &expo);
        attach(coeff, expo, &temp);
    }
    temp->link = *a;
}
int main(void)
{
    polyptr a, b, c;
    readPoly(&a);
    printPoly(a);
    readPoly(&b);
    printPoly(b);
    c = cpadd(a, b);
    printPoly(c);
}