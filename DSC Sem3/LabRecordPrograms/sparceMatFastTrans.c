//Week 3 program 2
#include <stdio.h>

#define MAX_TERMS 100

typedef struct {
    int row;
    int col;
    int value;
} Term;

void fastTranspose(Term a[], Term b[]) {
    int numTerms = a[0].value;
    int numCols = a[0].col;
    int colTerm[numCols];
    int startingPos[numCols];

    b[0].row = a[0].col;
    b[0].col = a[0].row;
    b[0].value = a[0].value;

    if (numTerms > 0) {
        for (int i = 0; i < numCols; i++) {
            colTerm[i] = 0;
        }

        for (int i = 1; i <= numTerms; i++) {
            colTerm[a[i].col]++;
        }

        startingPos[0] = 1;

        for (int i = 1; i < numCols; i++) {
            startingPos[i] = startingPos[i - 1] + colTerm[i - 1];
        }

        for (int i = 1; i <= numTerms; i++) {
            int j = startingPos[a[i].col]++;
            b[j].row = a[i].col;
            b[j].col = a[i].row;
            b[j].value = a[i].value;
        }
    }
}

void displayMatrix(Term a[]) {
    int numTerms = a[0].value;

    for (int i = 0; i <= numTerms; i++) {
        printf("%d %d %d\n", a[i].row, a[i].col, a[i].value);
    }
}

int main() {
    Term a[MAX_TERMS], b[MAX_TERMS];

    printf("Enter the number of rows in the matrix: ");
    scanf("%d", &a[0].row);

    printf("Enter the number of columns in the matrix: ");
    scanf("%d", &a[0].col);

    printf("Enter the number of non-zero elements in the matrix: ");
    scanf("%d", &a[0].value);

    printf("Enter the elements of the matrix (row, column, value):\n");
    for (int i = 1; i <= a[0].value; i++) {
        scanf("%d %d %d", &a[i].row, &a[i].col, &a[i].value);
    }

    printf("Original sparse Matrix:\n");
    displayMatrix(a);

    fastTranspose(a, b);

    printf("Transposed sparse Matrix:\n");
    displayMatrix(b);

    return 0;
}
