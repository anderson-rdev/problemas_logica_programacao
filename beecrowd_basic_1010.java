package calculosimples;
import java.util.Scanner;
import java.util.Locale;

class Peca {
    private int codigo;
    private int quantidade;
    private double valorUnitario;
    
    public Peca(int codigo, int quantidade, String valorStr){
        this.codigo = codigo;
        this.quantidade = quantidade;
        
        // Substituindo vírgula pelo e convertendo para double
        this.valorUnitario = Double.parseDouble(valorStr.replace(',','.'));
    }
    
    public double getSubtotal(){
        return quantidade * valorUnitario;
    }
}

public class CalculoSimples {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Leitura de dados peça 1
        int codigo1 = sc.nextInt();
        int quantidade1 = sc.nextInt();
        String valorStr1 = sc.next();

        // Leitura de dados peça 1
        int codigo2 = sc.nextInt();
        int quantidade2 = sc.nextInt();
        String valorStr2 = sc.next();
        valorStr2 = valorStr2.replace(',', '.');
        
        // Criando objetos para as peças 
        Peca peca1 = new Peca(codigo1,quantidade1,valorStr1);
        Peca peca2 = new Peca(codigo2,quantidade2,valorStr2);
        
        // Calculando o total 
        double total = peca1.getSubtotal() + peca2.getSubtotal();

        System.out.printf(Locale.US,"VALOR A PAGAR: R$ %.2f\n", total);

        sc.close();
    }
}
