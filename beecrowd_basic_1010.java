import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int peca1 = sc.nextInt();
        int numero1 = sc.nextInt();
        String valorStr1 = sc.next();
        valorStr1 = valorStr1.replace(',', '.');
        double valorunitario1 = Double.parseDouble(valorStr1);

        int peca2 = sc.nextInt();
        int numero2 = sc.nextInt();
        String valorStr2 = sc.next();
        valorStr2 = valorStr2.replace(',', '.');
        double valorunitario2 = Double.parseDouble(valorStr2);

        double total = (numero1 * valorunitario1) + (numero2 * valorunitario2);

        System.out.printf(Locale.US,"VALOR A PAGAR: R$ %.2f\n", total);

        sc.close();
    }
}
