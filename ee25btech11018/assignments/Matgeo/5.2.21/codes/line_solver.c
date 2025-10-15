#include <stdio.h>

void rref_solver(double aug[2][3], double solution[2]) {
    // Step 1: Normalize first row (pivot = aug[0][0])
    double pivot = aug[0][0];
    for (int j = 0; j < 3; j++) {
        aug[0][j] /= pivot;
    }

    // Step 2: Eliminate below pivot
    double factor = aug[1][0];
    for (int j = 0; j < 3; j++) {
        aug[1][j] -= factor * aug[0][j];
    }

    // Step 3: Normalize second row (pivot = aug[1][1])
    pivot = aug[1][1];
    for (int j = 0; j < 3; j++) {
        aug[1][j] /= pivot;
    }

    // Step 4: Eliminate above pivot
    factor = aug[0][1];
    for (int j = 0; j < 3; j++) {
        aug[0][j] -= factor * aug[1][j];
    }

    // Step 5: Extract solution
    solution[0] = aug[0][2]; // x
    solution[1] = aug[1][2]; // y
}



