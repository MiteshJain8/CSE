#include <stdio.h>
#include <stdlib.h>

int main() {
  int *arr = (int*)malloc(5 * sizeof(int)); // allocate memory for 5 integers
  for (int i = 0; i < 5; i++) {
    arr[i] = i + 1; // assign values to the array
  }
  printf("The original array is:\n");
  for (int i = 0; i < 5; i++) {
    printf("%d ", arr[i]); // print the original array
  }
  printf("\n");

  arr = (int*)realloc(arr, 10 * sizeof(int)); // resize the memory block to 10 integers
  for (int i = 5; i < 10; i++) {
    arr[i] = i + 1; // assign values to the new elements
  }
  printf("The resized array is:\n");
  for (int i = 0; i < 10; i++) {
    printf("%d ", arr[i]); // print the resized array
  }
  printf("\n");

  free(arr); // free the memory
  return 0;
}
