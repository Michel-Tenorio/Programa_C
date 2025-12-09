# Projetos em C

Repositório com exercícios e pequenos projetos desenvolvidos em linguagem C para praticar lógica de programação, manipulação de arrays, estruturas, funções e entrada/saída de dados no console.

## Tecnologias utilizadas

- Linguagem C
- Compilador GCC (ou compatível)
- Biblioteca padrão (`stdio.h`, `stdlib.h`, `string.h`, etc.)

## Arquivos do projeto

### `hospital.c`

Sistema simples de cadastro e consulta de pacientes em um hospital.

**Funcionalidades principais:**

- Cadastro de pacientes (nome, idade, profissão, altura, estado civil).
- Edição de dados de um paciente já cadastrado.
- Consulta de um paciente específico pelo nome.
- Listagem completa de todos os pacientes cadastrados.
- Ordenação alfabética dos pacientes pelo nome antes da listagem.
- Menu interativo no console para navegação entre as opções.

**Conceitos praticados:**

- `struct` para modelar o tipo `Paciente`.
- Vetores de structs e limite máximo de registros.
- Manipulação de strings (`fgets`, `strlen`, `strcmp`/`strcasecmp`, `strcpy`).
- Funções para organizar o código (cadastro, edição, consulta, listagem).
- Laços de repetição e controle de menu.
- Tratamento básico de entrada de dados do usuário.

### `atividade_C.c`

Arquivo com funções utilitárias para praticar manipulação de arrays numéricos e strings.

**Funcionalidades principais:**

- `contarPares(int numeros[], int tamanho)`  
  Conta e retorna a quantidade de números pares em um array de inteiros.
- `inverterArray(int numeros[], int tamanho)`  
  Inverte a ordem dos elementos de um array de inteiros “in-place”.
- `contarCaracteres(char str[])`  
  Conta a quantidade de caracteres de uma string até o caractere nulo `'\0'`.
- Função `main` que:
  - Lê 10 números inteiros do usuário.
  - Mostra a quantidade de números pares.
  - Inverte o array e exibe o resultado no console.

**Conceitos praticados:**

- Arrays unidimensionais.
- Passagem de arrays por parâmetro para funções.
- Laços `for` e `while`.
- Manipulação de strings em C.
- Separação de lógica em funções reutilizáveis.

