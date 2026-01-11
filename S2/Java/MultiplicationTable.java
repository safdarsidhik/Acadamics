import java.util.Scanner;

class MultiplicationTable {
    public static void plintTable(int num) {
        System .out.println("Multiplication Table of " + num);
        for (int i = 1; i <= 10; i++) {
            System.out.println(num + " x " + i + " = " + num * i);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        plintTable(num);
        sc.close();
    }
}