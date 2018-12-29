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

double proc(double* mat, size_t n, size_t m) {
	double max;

	#ifdef  PARALLEL
		#pragma omp parallel for shared(mat, n, m)
	#endif

	for (int i = 0; i < m; i++) {
		double min = mat[n*i];

		for (size_t j = 1; j < n; j++) {
			size_t ind = n * i + j;

			if (mat[ind] < min) {
				min = mat[ind];
			}
		}

		#pragma omp critical

		if (min > max) {
			max = min;
		}
	}

	return max;
}

int main() {
	#ifdef PARALLEL
	    cout << "Parallel" << endl;
	#endif

	#ifndef PARALLEL
	    cout << "Consistently" << endl;
	#endif

    size_t n = 750, m = 229;
    size_t size = n * m;
	double* mat = new double[size];

	fill(mat, size, 0, 22);

	auto start = std::chrono::system_clock::now();
	double result = proc(mat, n, m);
	auto end = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = end - start;

	// for (size_t i = 0; i < m; i++) {
	// 	for (size_t j = 0; j < n; j++) {
	// 		cout << mat[i * n + j] << "	";
	// 	}
	// 	cout << endl;
	// }

	cout << result << " (time: " << elapsed_seconds.count() << ")" << endl;
}