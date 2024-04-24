#include <stdio.h>

void transpose(int *matrix, int n) {
    int temp;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            temp = *(matrix + i * n + j);
            *(matrix + i * n + j) = *(matrix + j * n + i);
            *(matrix + j * n + i) = temp;
        }
    }
}

void displayMatrix(int *matrix, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", *(matrix + i * n + j));
        }
        printf("\n");
    }
}

int main() {
    int n;

    printf("Enter the number of rows and columns in the square matrix: ");
    scanf("%d", &n);

    int matrix[n][n];

    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    printf("Original Matrix:\n");
    displayMatrix(&matrix[0][0], n);

    transpose(&matrix[0][0], n);

    printf("Transposed Matrix:\n");
    displayMatrix(&matrix[0][0], n);

    return 0;
}
