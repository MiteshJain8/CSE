#include <stdio.h>

int binary(int arr[], int low, int high, int mid, int key) {
    if(low>high) {
        return -1;
    } else if(key==arr[mid]) {
        return mid;
    } else if(key<arr[mid]) {
        return binary(arr,low, mid-1, (low+mid-1)/2, key);
    } else {
        return binary(arr,mid+1, high, (mid+1+high)/2, key);
    }
}

int main() {
    int n, key;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter the key: \n");
    scanf("%d", &key);
    int low = 0;
    int high = sizeof(arr)/sizeof(int);
    int mid = (low+high)/2;
    int result = binary(arr, low, high, mid, key);
    if(result==-1) {
        printf("Element not found");
    } else {
        printf("Element found at index %d", result);
    }
    return 0;
}