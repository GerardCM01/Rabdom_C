#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Inicialitza la llavor per a la generació de nombres aleatoris
    srand(time(NULL));

    // Genera un nombre aleatori
    int numero_aleatori = rand();

    // Imprimeix el nombre aleatori
    printf("Nombre aleatori: %d\n", numero_aleatori);

    return 0;
}
