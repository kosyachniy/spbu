#include <iostream>
#include <string>

using namespace std;

#define CH ((int) '0') * 2

int main() {
	string a, b, c;
	cin >> a >> b;
	int n_a = a.length();
	int n_b = b.length();
	
	int d = n_b - n_a;
	if (d < 0) {
		c = a;
		a = b;
		b = c;
		d *= -1;
	}

	for (int i=0; i<d; i++) {
		cout << b[i];
	}

	for (int i=0; i<a.length(); i++) {
		cout << (int) a[i] + (int) b[d+i] - CH;
	}

	return 0; 
}