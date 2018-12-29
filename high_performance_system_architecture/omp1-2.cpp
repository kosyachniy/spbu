#include "omp.h"
#include <chrono>
#include <iostream>

using namespace std;

double func(double x) {
    return 4.0 / (1 + x * x);
}

double proc(double func(double), int mode) {
    double bottom = 0, top = 1;

    double sum = 0;
    size_t n = (top - bottom) / 1e-5;

    if (mode == 1) {
    	#pragma omp parallel for 
    } else {
    	if (mode == 2) {
	    	#pragma omp parallel for shared(func, bottom, top, n) reduction(+: sum)
	    }
	}

    for (int i = 0; i <= n; i++) {
        sum += func(bottom + 1e-5 * i);
    }

    sum *= 1e-5;

    return sum;
}

int main() {
    cout << "Parallel for" << endl;

    auto start = std::chrono::system_clock::now();
    double res = proc(func, 1);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;

    cout << "∫=" << res << " (time: " << elapsed_seconds.count() << ")" << endl;


    cout << "Reduction" << endl;

    start = std::chrono::system_clock::now();
    res = proc(func, 2);
    end = std::chrono::system_clock::now();
    elapsed_seconds = end - start;

    cout << "∫=" << res << " (time: " << elapsed_seconds.count() << ")" << endl;


    cout << "Consistently" << endl;

    start = std::chrono::system_clock::now();
    res = proc(func, 0);
    end = std::chrono::system_clock::now();
    elapsed_seconds = end - start;

    cout << "∫=" << res << " (time: " << elapsed_seconds.count() << ")" << endl;
}