// Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import java.util.Scanner;

public class Ex06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Qual é o raio do círculo? ");
        double r = sc.nextDouble();

        double a = a = r*r*3.14;
        System.out.printf("A área do círculo de raio %.0f é %.1f", r, a);

        sc.close();
    }
}
