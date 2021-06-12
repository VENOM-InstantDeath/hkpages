#include <iostream>
#include <sstream>
#include <algorithm>
#include <ctype.h>
#include <limits>
using namespace std;

struct ary {
	int len;
	string* arr;
};

struct persona {
	string nombre, apellido, civstate, sexo;
	int edad;
};

void clcin() {
	cin.clear();
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

bool sin_arr(ary x, string y) {
	for (int i=0; i < x.len; i++) {
		if (y == x.arr[i]) {
			return true;
		}
	}
	return false;
}


string lower(string x) {
	for (int i=0; i<x.size(); i++) {
		x[i] = tolower(x[i]);
	}
	return x;
}

int main() {
	//A ingresar los datos de 10 personas como el nombre,
	//apellido, la edad y sexo
	//
	//Presente la información en consulta general
	// 	Primera consulta ordenada por estado civil
	// 	Segunda consulta por edad

	string nombre, apellido, sexo;
	string A_sexos[] = {"masculino", "femenino"};
	ary sexos = {2, A_sexos};
	int edad;

	cout << "Nombre: ";
	getline(cin, nombre);
	cout << "Apellido: ";
	getline(cin, apellido);
	while (true) {
		cout << "Edad: ";
		cin >> edad;
		clcin();
		if (edad == 0) {
			cout << "Edad inválida\n\n";
			continue;
		}
		break;
	}
	while (true) {
		cout << "Sexo: ";
		getline(cin, sexo);
		sexo = lower(sexo);
		if (! sin_arr(sexos, sexo)) {
			cout << "Sexo inválido\n\n";
			continue;
		}
		break;
	}
	return 0;
}
