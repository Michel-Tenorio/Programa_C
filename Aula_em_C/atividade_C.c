#include <stdio.h>
#include <string.h>
//contarPares
int contarPares(int numeros[], int tamanho) {
    int pares = 0;
    for (int i = 0; i < tamanho; i++) {
        if (numeros[i] % 2 == 0) {
            pares++;
        }
    }
    return pares;
}
//funçao 
void inverterArray(int numeros[], int tamanho) {
    int temp;
    for (int i = 0; i < tamanho / 2; i++) {
        temp = numeros[i];
        numeros[i] = numeros[tamanho - 1 - i];
        numeros[tamanho - 1 - i] = temp;
    }
}
//coontar caracteres
int contarCaracteres(char str[]) {
    int i = 0;
    while (str[i] != '\0') {
        i++;
    }
    return i;
}
// inincio 
int main() {
    int numeros[10];
    char texto[100];
//Leitura dos numeros 
    printf("Digite 10 numeros:\n");
    for (int i = 0; i < 10; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &numeros[i]);
    }
//contagem
    int pares = contarPares(numeros, 10);
    printf("\nQuantidade de numeros pares: %d\n", pares);
//inverte e mostra o resultados 
    inverterArray(numeros, 10);
    printf("Array invertido: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");
//conta os caracteres 
    printf("\nDigite uma string: ");
    getchar(); // limpa o buffer do teclado
    fgets(texto, 100, stdin);

    texto[strcspn(texto, "\n")] = '\0'; // remove o \n do final
//mostra 
    int qtd = contarCaracteres(texto);
    printf("A string possui %d caracteres.\n", qtd);

    return 0;
}

