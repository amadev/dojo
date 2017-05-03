#include <stdlib.h>
#include <stddef.h>

typedef struct {
    int *arr;
    size_t used; // size_t unsigned type
    size_t total;
} Array;


void init(Array *arr, size_t initial_size) {
    arr->arr = (int *) malloc(initial_size * sizeof(int));
    arr->used = 0;
    arr->total = initial_size;
}

void insert(Array *arr, int value) {
    if (arr->used >= arr->total) {
        arr->total *= 2;
        arr->arr = (int *) realloc(arr->arr, arr->total * sizeof(int));
    }
    arr->arr[arr->used++] = value;
}

void free_arr(Array *arr) {
    free(arr->arr);
    arr->arr = NULL;
    arr->used = arr->total = 0;
}

int main() {
    Array arr;
    int i;
    init(&arr, 5);
    for (i = 1; i < 10; i ++) {
        insert(&arr, i);
    }
    free_arr(&arr);
}
