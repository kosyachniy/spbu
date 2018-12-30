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

	int a[n][n];
	int a_j[n];
	int a_i = 1;
	a_j[0] = 1;
	a[0][0] = 0;
	for (int i=1; i<n; i++) {
		if (m[i] <= m[a[a_i-1][0]]) {
			a[a_i][0] = i;
			a_j[a_i] = 1;
			a_i++;
		}

		for (int j=0; j<a_i; j++) {
			if (m[i] > m[a[j][a_j[j]-1]]) {
				a[j][a_j[j]] = i;
				a_j[j]++;
			}
		}
	}

	int m_i = 0;
	int m_l = a_j[0];
	for (int i=0; i<a_i; i++) {
		if (a_j[i] > m_l) {
			m_i = i;
			m_l = a_j[i];
		}
	}

	cout << m_l << endl;
	for (int i=0; i<m_l; i++) {
		cout << a[m_i][i]+1 << " ";
	}

	return 0;
}