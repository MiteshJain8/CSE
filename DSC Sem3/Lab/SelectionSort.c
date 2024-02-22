//Week 1 program 1
#include <stdio.h>

void swap(int *x, int *y) {
     int temp = *x;
     *x = *y;
     *y = temp;
}

void SelectionSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++)
    {
        int min = i;
        for (int j = i+1; j < n; j++)
        {
            if(arr[j]<arr[min]) {
                min = j;
            }      
        }
        swap(&arr[i], &arr[min]);
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    SelectionSort(arr, n);
    printf("Sorted array: ");
    for (int i=0; i<n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}