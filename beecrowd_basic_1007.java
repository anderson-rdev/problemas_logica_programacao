import java.util.Scanner;  // Importa a classe Scanner para leitura de entrada do usuário

public class DiferencaProduto {
    public static void main(String[] args) {
        // Cria uma instância de Scanner para ler os valores inseridos pelo usuário
        Scanner sc = new Scanner(System.in);  

        // Leitura dos quatro valores inteiros (A, B, C e D) um por um
        int a = sc.nextInt();  // Lê o primeiro valor inteiro (A)
        int b = sc.nextInt();  // Lê o segundo valor inteiro (B)
        int c = sc.nextInt();  // Lê o terceiro valor inteiro (C)
        int d = sc.nextInt();  // Lê o quarto valor inteiro (D)
       
        // Cálculo da diferença entre os produtos de A*B e C*D
        int DIFERENCA = (a * b - c * d);  // A multiplicação de A e B, subtraída pela multiplicação de C e D

        // Exibe o resultado da diferença com a mensagem formatada
        System.out.println("DIFERENCA = " + DIFERENCA);  // A palavra DIFERENCA seguida pelo valor calculado

        // Fecha o Scanner após o uso para liberar recursos
        sc.close();
    }
}
