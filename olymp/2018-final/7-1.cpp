#include <iostream>
#include <string>
#include <cmath>

void t(int n, std::string i) {
	if (n>1) {
		t(n-1, i+" 0");
		t(n-1, i+" 1");
	} else {
		std::cout << i << std::endl;
	}
}

int main() {
	int k;
	std::cin >> k;
	unsigned int p = pow(2, k);
	std::cout << p << std::endl;

	t(k, "0");
	t(k, "1");

	return 0;
}