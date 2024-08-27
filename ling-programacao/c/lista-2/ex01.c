#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Produto {
    char nome[30];
    int codigo;
    double preco;
};

typedef struct node {
    struct Produto produto;
    struct node* next;
} Node;

Node* criarProduto() {
    Node* novo = (Node*)malloc(sizeof(Node));
    if (novo == NULL) {
        printf("Erro ao alocar memória.\n");
        return NULL;
    }
    
    printf("Digite o nome do produto: ");
    scanf(" %29[^\n]", novo->produto.nome);
    printf("Digite o código do produto: ");
    scanf("%d", &novo->produto.codigo);
    printf("Digite o preço do produto: ");
    scanf("%lf", &novo->produto.preco);
    
    novo->next = NULL;
    return novo;
}

void adicionarProduto(Node** lista) {
    Node* novo = criarProduto();
    if (novo == NULL)
        return;
    
    if (*lista == NULL) {
        *lista = novo;
    } else {
        Node* temp = *lista;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = novo;
    }
}

void exibirLista(Node* lista) {
    if (lista == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    
    Node* temp = lista;
    while (temp != NULL) {
        printf("Nome: %s, Código: %d, Preço: %.2lf\n", temp->produto.nome, temp->produto.codigo, temp->produto.preco);
        temp = temp->next;
    }
}

void buscarPorNome(Node* lista) {
    if (lista == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    
    char nomeBusca[30];
    printf("Digite o nome do produto que deseja buscar: ");
    scanf(" %29[^\n]", nomeBusca);
    
    Node* temp = lista;
    int encontrou = 0;
    while (temp != NULL) {
        if (strcmp(temp->produto.nome, nomeBusca) == 0) {
            printf("Produto encontrado:\n");
            printf("Nome: %s, Código: %d, Preço: %.2lf\n", temp->produto.nome, temp->produto.codigo, temp->produto.preco);
            encontrou = 1;
            break;
        }
        temp = temp->next;
    }
    
    if (!encontrou) {
        printf("Produto não encontrado.\n");
    }
}

void liberarLista(Node* lista) {
    Node* temp;
    while (lista != NULL) {
        temp = lista;
        lista = lista->next;
        free(temp);
    }
}

int main() {
    Node* lista = NULL;
    int opcao;

    do {
        printf("\nMenu:\n");
        printf("1. Adicionar Produto\n");
        printf("2. Exibir Lista de Produtos\n");
        printf("3. Buscar Produto por Nome\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                adicionarProduto(&lista);
                break;
            case 2:
                exibirLista(lista);
                break;
            case 3:
                buscarPorNome(lista);
                break;
            case 4:
                liberarLista(lista);
                printf("Programa encerrado.\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (opcao != 4);

    return 0;
}
