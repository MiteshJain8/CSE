#include <stdio.h>

struct polynomial {
    int coeff;
    int exp;
};

void swap(struct polynomial *a, struct polynomial *b) {
    struct polynomial temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(struct polynomial arr[], int n) {
    int i, j, max_idx;

    for (i = 0; i < n - 1; i++) {
        max_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j].exp > arr[max_idx].exp)
                max_idx = j;

        swap(&arr[max_idx], &arr[i]);
    }
}

int main() {
    int n1, n2;

    scanf("%d", &n1);
    scanf("%d", &n2);

    struct polynomial p1[n1];
    struct polynomial p2[n2];
    struct polynomial p3[n1 + n2];

    for (int i = 0; i < n1; i++) {
        scanf("%d %d", &p1[i].coeff, &p1[i].exp);
    }

    for (int i = 0; i < n2; i++) {
        scanf("%d %d", &p2[i].coeff, &p2[i].exp);
    }

    selectionSort(p1, n1);
    selectionSort(p2, n2);

    int i = 0, j = 0, k = 0;

    while (i < n1 && j < n2) {
        if (p1[i].exp == p2[j].exp) {
            p3[k].coeff = p1[i].coeff + p2[j].coeff;
            p3[k].exp = p1[i].exp;
            i++;
            j++;
        } else if (p1[i].exp > p2[j].exp) {
            p3[k].coeff = p1[i].coeff;
            p3[k].exp = p1[i].exp;
            i++;
        } else {
            p3[k].coeff = p2[j].coeff;
            p3[k].exp = p2[j].exp;
            j++;
        }
        k++;
    }

    while (i < n1) {
        p3[k].coeff = p1[i].coeff;
        p3[k].exp = p1[i].exp;
        i++;
        k++;
    }

    while (j < n2) {
        p3[k].coeff = p2[j].coeff;
        p3[k].exp = p2[j].exp;
        j++;
        k++;
    }

    for (int i = 0; i < k; i++) {
        printf("%dx^%d", p3[i].coeff, p3[i].exp);

        if (i < k - 1 && p3[i + 1].coeff != 0) {
            printf(" + ");
        }
    }
    return 0;
}