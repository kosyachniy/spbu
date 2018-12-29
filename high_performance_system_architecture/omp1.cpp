#include "omp.h"
#include <chrono>
#include <iostream>

// #define PARALLEL_FOR
// #define REDUCTION

using namespace std;

double func(double x) {
    return 4.0 / (1 + x * x);
}

double proc(double func(double)) {
    double bottom = 0, top = 1;

    double sum = 0;
    size_t n = (top - bottom) / 1e-5;

    #ifdef PARALLEL_FOR
        #pragma omp parallel for 
    #endif

    #ifdef REDUCTION
        #pragma omp parallel for shared(func, bottom, top, n) reduction(+: sum)
    #endif

    for (int i = 0; i <= n; i++) {
        sum += func(bottom + 1e-5 * i);
    }

    sum *= 1e-5;

    return sum;
}

int main() {
    auto start = std::chrono::system_clock::now();
    double res = proc(func);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;

    #ifdef PARALLEL_FOR
        cout << "Parallel for" << endl;
    #endif

    #ifdef REDUCTION
        cout << "Reduction" << endl;
    #endif

    #ifndef PARALLEL_FOR
        #ifndef REDUCTION
            cout << "Consistently" << endl;
        #endif
    #endif

    cout << "∫=" << res << " (time: " << elapsed_seconds.count() << ")" << endl;
}