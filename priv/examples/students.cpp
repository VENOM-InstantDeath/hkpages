#include <iostream>
#include <stdlib.h>
using namespace std;

struct materia {
	string nombremateria;
	float nota1, nota2, notafinal;
};

struct estudiante {
	string nombre;
	materia mismaterias[2];
};

int main() {
	estudiante P;
	P.nombre = "Tomás";
	P.mismaterias[0].nombremateria = "Matemática";
	P.mismaterias[0].nota1 = 80.0;
	P.mismaterias[0].nota2 = 95.5;
	P.mismaterias[0].notafinal = 100.0;
	P.mismaterias[1].nombremateria = "Literatura";
	P.mismaterias[1].nota1 = 40.5;
	P.mismaterias[1].nota2 = 60.0;
	P.mismaterias[1].notafinal = 100.0;

	estudiante O;
	O.nombre = "Pedro";
	O.mismaterias[0].nombremateria = "Matemática";
	O.mismaterias[0].nota1 = 30.5;
	O.mismaterias[0].nota2 = 50.0;
	O.mismaterias[0].notafinal = 44.0;
	O.mismaterias[1].nombremateria = "Literatura";
	O.mismaterias[1].nota1 = 10.0;
	O.mismaterias[1].nota2 = 20.0;
	O.mismaterias[1].notafinal = 10.0;
	
	cout << "Estudiante: " << P.nombre << endl;
	for (int i=0;i < 2; i++) {
		cout << "\t" <<P.mismaterias[i].nombremateria << endl;
		cout << "\t\t" << P.mismaterias[i].nota1 << endl;
		cout << "\t\t" << P.mismaterias[i].nota2 << endl;
		cout << "\t\t" << P.mismaterias[i].notafinal << endl;
	}
	cout << "\nEstudiante: " << O.nombre << endl;
	for (int i=0; i < 2; i++) {
		cout << "\t" << O.mismaterias[i].nombremateria << endl;
		cout << "\t\t" << O.mismaterias[i].nota1 << endl;
		cout << "\t\t" << O.mismaterias[i].nota2 << endl;
		cout << "\t\t" << O.mismaterias[i].notafinal << endl;
	}
	return 0;
}
