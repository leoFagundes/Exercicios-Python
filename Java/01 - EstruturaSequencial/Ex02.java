// Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número: ");
        int numero = sc.nextInt();

        System.out.printf("O número digitado foi %d", numero );

        sc.close();
    }
}
