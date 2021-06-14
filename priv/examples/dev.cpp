#include <iostream>
#include <string>
#include <limits>
#include <vector>
#include <regex>
#include <unordered_map>
using namespace std;

struct persona {
	string nombre, apellido, civstate, sexo;
	int edad;
};

struct civstate {
	vector<persona> soltero, casado, divorciado, viudo;
};

void clcin() {
	cin.clear();
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

bool sin_arr(vector<string> x, string y) {
	for (int i=0; i < x.size(); i++) {
		if (y == x[i]) {
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

void display_data(vector<persona> x) {
	for (int i=0; i<x.size(); i++) {
		cout << "\t" << x[i].nombre << endl;
		cout << "\t" << x[i].apellido << endl;
		cout << "\t" << x[i].edad << endl;
		cout << "\t" << x[i].sexo << endl;
		cout << "\n";
	}
}

int main() {
	vector<string> sexos = {"masculino", "femenino"};
	vector<string> civs  = {"soltero", "soltera", "casado", "casada", "divorciado", "divorciado", "viudo", "viuda"};
	persona ps[10];

	for (int i=0; i<10; i++) {
		cout << "Nombre: ";
		getline(cin, ps[i].nombre);
		cout << "Apellido: ";
		getline(cin, ps[i].apellido);
		while (true) {
			cout << "Edad: ";cin >> ps[i].edad;clcin();
			if (ps[i].edad == 0) {
				cout << "\tEdad inválida\n";
				continue;
			}
			break;
		}
		while (true) {
			cout << "Sexo: ";getline(cin, ps[i].sexo);
			ps[i].sexo = lower(ps[i].sexo);
			if (! sin_arr(sexos, ps[i].sexo)) {
				cout << "\tSexo inválido\n";
				continue;
			}
			break;
		}
		while (true) {
			cout << "\tLos posibles valores para estado civil son: soltero/a, casado/a, divorciado/a o viudo/a.\n";
			cout << "Estado civil: ";getline(cin, ps[i].civstate);
			if (! sin_arr(civs, ps[i].civstate)) {
				cout << "\tEstado civíl inválido\n";
				continue;
			}
			break;
		}
		cout << "\tSe ha registrado exitosamente a " << ps[i].nombre << "\n\n";
	}
	cout << "\n\tOrden por Estado Civil\n\n";
	civstate civsts;
	for (int i=0; i<10; i++) {
		if (regex_match(ps[i].civstate, regex("solter[oa]"))) {
			civsts.soltero.push_back(ps[i]);
		}
		else if (regex_match(ps[i].civstate, regex("casad[oa]"))) {
			civsts.casado.push_back(ps[i]);
		}
		else if (regex_match(ps[i].civstate, regex("divorciad[oa]"))) {
			civsts.divorciado.push_back(ps[i]);
		}
		else if (regex_match(ps[i].civstate, regex("viud[oa]"))) {
			civsts.viudo.push_back(ps[i]);
		}
	}
	cout << "Soltero/a:\n";
	display_data(civsts.soltero);
	cout << "\nCasado/a:\n";
	display_data(civsts.casado);
	cout << "\nDivorciado/a:\n";
	display_data(civsts.divorciado);
	cout << "\nViudo/a:\n";
	display_data(civsts.viudo);

	unordered_map<int, vector<persona>> edades;
	vector<persona> tmped;
	for (int i=0; i<10; i++) {
		if (edades.find(ps[i].edad) == edades.end()) {
			edades[ps[i].edad] = tmped;
		}
	}
	for (int i=0; i<10; i++) {
		edades[ps[i].edad].push_back(ps[i]);
	}
	cout << "\n\tOrden por Edad:\n\n";
	for (auto& it: edades) {
		cout << it.first << ":\n";
		for (int i=0;i<edades[it.first].size(); i++) {
			cout << "\t" << edades[it.first][i].nombre << endl;
			cout << "\t" << edades[it.first][i].apellido << endl;
			cout << "\t" << edades[it.first][i].edad << endl;
			cout << "\t" << edades[it.first][i].sexo << endl;
			cout << "\n";
		}
	}
	return 0;
}
