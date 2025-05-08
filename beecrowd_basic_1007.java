import java.util.Scanner;

public class DiferencaProduto {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  

        // Leitura de Valores 
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
       
        // Cálculo da diferença 
        int DIFERENCA = (a * b - c * d);

        // Resultado final 
        System.out.println("DIFERENCA = " + DIFERENCA);

        sc.close();
    }
}