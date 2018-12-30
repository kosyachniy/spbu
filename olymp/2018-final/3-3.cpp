#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	cin >> n;

	if (n > 1) {
		int i=2, k=0;
		bool f = false;
		string s = "";

		while (i <= n) {
			if (n%i == 0) {
				k += 1;
				n /= i;
			} else {
				if (k) {
					if (f) {
						s += "*";
					} else {
						f = true;
					}

					s += to_string(i) + "^" + to_string(k);
					k = 0;
				}

				i += 1;
			}
		}

		if (f) s += "*";
		s += to_string(i) + "^" + to_string(k);

		cout << s;
	} else {
		cout << "";
	}

	return 0;
}