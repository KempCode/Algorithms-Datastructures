// YOOBEEPRACTICE.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <cmath>
#include <ctime>
#include <cctype>
#include <fstream>
#include <exception>
using namespace std;

int main()
{
    int A[2][5] = {
    {2, 0, 0, 0, 0},
    {0, 0, 0, 0, 0}
    };

    int B[5][4] = {
        {2, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0}
    };

    int C[2][4] = { 0 }; // Initialize the result matrix with zeros

    // Perform matrix multiplication
    for (int i = 0; i < 2; ++i) { /// iterate C's rows
        for (int j = 0; j < 4; ++j) { // iterate C's columns


            for (int k = 0; k < 5; ++k) { // K is shared between A and B
                C[i][j] += A[i][k] * B[k][j]; // multipily and add
                //C[1][1] += A[1][1] * B[1][1]; 
                //C[1][1] += A[1][2] * B[2][1];
                //C[1][1] += A[1][3] * B[3][1]; until 5 then next on C makes sense
            }
        }
    }


}

