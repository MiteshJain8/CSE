#include <stdio.h>
#define COMPARE(x,y) (((x)<(y))? -1 : ((x)==(y))? 0:1)

int binary(int arr[], int low, int high, int key) {
    int mid = (low + high) / 2;
    if (low > high) {
        return -1;
    } else {
        switch (COMPARE(arr[mid], key)) {
            case 0: {
                return mid;
            }
            case 1: { //arr[mid]>key
                return binary(arr, low, mid - 1, key);
            }
            case -1: { //arr[mid]<key
                return binary(arr, mid + 1, high, key);
            }
        }
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
    int key, low = 0, high = sizeof(arr)/sizeof(int);
    printf("Enter the key: ");
    scanf("%d", &key);
    int result = binary(arr, low, high, key);
    if(result==-1) {
        printf("Element not found");
    } else {
        printf("Element found at index %d", result);
    }
    return 0;
}