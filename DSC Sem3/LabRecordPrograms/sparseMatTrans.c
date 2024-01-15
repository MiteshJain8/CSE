//Week 3 program 1
#include <stdio.h>

#define MAX_TERMS 100

typedef struct
{
    int row;
    int col;
    int value;
} Term;

void transpose(Term a[], Term b[])
/* b is set to the transpose of a */
{
    int i, j, currentb;
    int numTerms = a[0].value;
    int numCols = a[0].col;
    b[0].row = a[0].col; /* rows in b = columns in a */
    b[0].col = a[0].row; /*columns in b = rows in a */
    b[0].value = a[0].value;
    if (numTerms > 0)
    { /*non zero matrix */
        currentb = 1;
        for (i = 0; i < numCols; i++)
            /* transpose by columns in a */
            for (j = 1; j <= numTerms; j++)
                /*  find elements from the current column */
                if (a[j].col == i)
                {
                    /* element is in current column, add it to b */
                    b[currentb].row = a[j].col;
                    b[currentb].col = a[j].row;
                    b[currentb].value = a[j].value;
                    currentb++;
                }
    }
}

void displayMatrix(Term a[])
{
    int numTerms = a[0].value;

    for (int i = 0; i <= numTerms; i++)
    {
        printf("%d %d %d\n", a[i].row, a[i].col, a[i].value);
    }
}

int main()
{
    Term a[MAX_TERMS], b[MAX_TERMS];

    printf("Enter the number of rows in the matrix: ");
    scanf("%d", &a[0].row);

    printf("Enter the number of columns in the matrix: ");
    scanf("%d", &a[0].col);

    printf("Enter the number of non-zero elements in the matrix: ");
    scanf("%d", &a[0].value);

    printf("Enter the elements of the matrix (row, column, value):\n");
    for (int i = 1; i <= a[0].value; i++)
    {
        scanf("%d %d %d", &a[i].row, &a[i].col, &a[i].value);
    }

    printf("Original sparse Matrix:\n");
    displayMatrix(a);

    transpose(a, b);

    printf("Transposed sparse Matrix:\n");
    displayMatrix(b);

    return 0;
}
