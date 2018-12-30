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
		cout << "Какое устройство?" << endl;
		cin >> type;
		cout << "Имя: ";
		cin >> name;
		cout << "Стоимость ремонта = " << rand() << endl << "Дата: " << tdata << endl;
	}

	void took() {
		remont = 2;
	}

	void broke() {
		remont = 3;
	}
};