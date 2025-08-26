// Faça um Programa que converta metros para centímetros.
import java.util.Scanner;

public class Ex05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos metros? ");
        double m = sc.nextDouble();

        double c = m * 100;

        System.out.printf("%.0f metros são %.0f centimetros", m, c);

        sc.close();
    }
}
