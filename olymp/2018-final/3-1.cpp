#include <iostream>
#include <cmath>

using namespace std;

int s(int n, int i) {
	int k = 0;
	while (n%i == 0) {
		k++;
		n /= i;
	}
	return k;
}

int main() {
	int n;
	cin >> n;

	int i = 2;
	bool f = false;

	while (true) {
		if (n%i == 0) {
			int o = s(n, i);
			n /= pow(i, o);

			if (f) {
				cout << "*";
			}
			else {
				f = true;
			}

			cout << i << "^" << o;

			if (n == 1) {
				break;
			}
		}

		i++;
	}
	return 0;
}