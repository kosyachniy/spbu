#include <iostream>
#include <String>
#include <cstdlib>
#include <ctime>

using namespace std;

struct device {
	string type, name;
	int data, remont, price;

	void reception(int tdata) {
		srand(time(NULL));
		remont = 1;
		cout << "����� ����������?" << endl;
		cin >> type;
		cout << "���: ";
		cin >> name;
		cout << "��������� ������� = " << rand() << endl << "����: " << tdata << endl;
	}

	void took() {
		remont = 2;
	}

	void broke() {
		remont = 3;
	}
};