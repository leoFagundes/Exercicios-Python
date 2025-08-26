// Faça um Programa que peça as 4 notas bimestrais e mostre a média.
import java.util.Scanner;

public class Ex04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite as 4 notas bimestrais: ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int n4 = sc.nextInt();

        System.out.printf("A média das notas é: %d", (n1 + n2 + n3 + n4) / 4);

        sc.close();
    }
}
