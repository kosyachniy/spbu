#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	float m[n];
	for (int i=0; i<n; i++) {
		float a, b;
		cin >> a >> b;

		if (a) {
			m[i] = b / a;
		} else {
			m[i] = 1000000001.0;
		}
	}

	int a[n];
	int o = 1;
	a[0] = 0;
	for (int i=1; i<n; i++) {
		if (m[i] > m[a[o-1]]) {
			a[o] = i;
			o++;
		}
	}

	for (int i=1; i<n-o; i++) {
		if (m[i] <= m[a[0]]) {
			int b[n];
			int l = 1;
			b[0] = i;
			for (int j=i+1; j<n; j++) {
				if (m[j] > m[b[l-1]]) {
					b[l] = j;
					l++;
				}
			}

			if (l > o) {
				o = l;
				for (int u=0; u<l; u++) {
					a[u] = b[u];
				}
			}
		}
	}

	cout << o << endl;
	for (int i=0; i<o; i++) {
		cout << a[i]+1 << " ";
	}

	return 0;
}