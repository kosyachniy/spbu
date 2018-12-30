#include <iostream>
#include <string>

using namespace std;

int main() {
	int n, m;
	cin >> n;

	int i = 2;
	bool f = false;
	string s = "";

	m = n / 2;

	while (i <= m) {
		if (n%i == 0) {
			int o = 1;
			n /= i;

			while (true) {
				if (n % i) break;
				o++;
				n /= i;
			}

			if (f) {
				s += "*";
			} else {
				f = true;
			}

			s += to_string(i) + "^" + to_string(o);

			if (n == 1) {
				cout << s;
				return 0;
			}
		}

		i++;
	}

	cout << "";
	return 0;
}