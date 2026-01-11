import java.util.Scanner;

public class  FibonacciSeries{
    public static void generateFibonacci(int n){
        int first = 0, second = 1, next;
        System.out.print("Fibonacci Series :" +first+" "+second);
        for (int i = 2; i < n; i++) {
            next = first + second;
            System.out.print(" "+next);
            first = second;
            second = next;
        }
    System.out.println();
    }
    


    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no.of terms of fibonacci series : ");
        int n = sc.nextInt();
        generateFibonacci(n);
        sc.close();
    }
}