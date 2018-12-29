#include "omp.h"
#include <chrono>
#include <iostream>

// #define PARALLEL

using namespace std;

void fill(double* a, size_t n, int min, int max) {
    for (size_t i = 0; i < n; i++) {
        a[i] = (rand() % (max - min + 1) + min) + rand() / RAND_MAX;
    }
}

bool check(double* a, double* b, size_t n,  double res) {
    double new_res = 0;

    for (size_t i = 0; i < n; i++) {
        new_res += a[i] * b[i];
    }

    return abs(res - new_res) < 1e-4;
}

double proc(double* a, double* b,  size_t n) {
    double res = 0;

    #ifdef PARALLEL
        #pragma omp parallel for shared(a, b, n)
    #endif

    for (int i = 0; i < n; i++) {
        #pragma omp atomic
        res += a[i] * b[i];
    }

    return res;
}

int main() {
    #ifdef PARALLEL
        cout << "Parallel" << endl;
    #endif

    #ifndef PARALLEL
        cout << "Consistently" << endl;
    #endif

    size_t n = 1000000;
    int min = 0, max = 100; 
    double* a = new double[n];
    double* b = new double[n];

    fill(a, n, min, max);
    fill(b, n, min, max);

    auto start = std::chrono::system_clock::now();
    double result = proc(a, b, n);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;

    cout << "<x,y>=" << check(a, b, n, result) << " (time: " << elapsed_seconds.count() << ")" << endl;
}