// Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import java.util.Scanner;

public class Ex07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Informe o lado do quadrado: ");
        int l = sc.nextInt();

        int a = l * l;

        System.out.printf("A área do quadrado é %d e o dobro dessa área é %d", a, a*2);
        sc.close();
    }
}
