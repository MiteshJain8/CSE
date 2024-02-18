#include <stdio.h>
#include <stdlib.h>

#define MALLOC(p, s)                            \
    if (!((p) = malloc(s)))                     \
    {                                           \
        fprintf(stderr, "Insufficient memory"); \
        exit(EXIT_FAILURE);                     \
    }

#define COMPARE_EXPONENT(a, b) ((a) > (b) ? 1 : ((a) < (b) ? -1 : 0))

typedef struct polyNode *polyPointer;
typedef struct polyNode
{
    float coef;
    int expon;
    polyPointer link;
} polyNode;

void attach(float coefficient, int exponent, polyPointer *ptr)
{
    polyPointer temp;
    MALLOC(temp, sizeof(*temp));
    temp->coef = coefficient;
    temp->expon = exponent;
    (*ptr)->link = temp;
    *ptr = temp;
    temp->link = NULL;
}

polyPointer padd(polyPointer a, polyPointer b)
{
    polyPointer c, rear;
    float sum;
    MALLOC(c, sizeof(*c));
    rear = c;
    while (a && b)
        switch (COMPARE_EXPONENT(a->expon, b->expon))
        {
        case -1: /* a->expon < b->expon */
            attach(b->coef, b->expon, &rear);
            b = b->link;
            break;

        case 0: /* a->expon = b->expon */
            sum = a->coef + b->coef;
            if (sum)
                attach(sum, a->expon, &rear);
            a = a->link;
            b = b->link;
            break;

        case 1: /* a->expon > b->expon */
            attach(a->coef, a->expon, &rear);
            a = a->link;
        }
    for (; a; a = a->link)
        attach(a->coef, a->expon, &rear);
    for (; b; b = b->link)
        attach(b->coef, b->expon, &rear);
    rear->link = NULL;
    rear = c;
    c = c->link;
    free(rear);
    return c;
}

int main()
{
    polyPointer a = NULL, b = NULL, c = NULL;
    polyPointer rear = NULL;

    // first polynomial: 3x^3 + 2x + 1
    MALLOC(a, sizeof(*a));
    a->coef = 3;
    a->expon = 3;
    rear = a;
    attach(2, 1, &rear);
    attach(1, 0, &rear);
    rear->link = NULL;

    // second polynomial: 5x^2 + 4x + 3
    MALLOC(b, sizeof(*b));
    b->coef = 5;
    b->expon = 2;
    rear = b;
    attach(4, 1, &rear);
    attach(3, 0, &rear);
    rear->link = NULL;

    c = padd(a, b);
    for (rear = c; rear; rear = rear->link)
    {
        printf("%.2fx^%d ", rear->coef, rear->expon);
        if (rear->link && rear->link->coef >= 0)
            printf(" + ");
    }
    free(a);
    free(b);
    free(c);
    return 0;
}