package My_Code.Week2;
import java.util.*;

public class Sales {
 public static void main(String[] args)
 {
 final int SALESPEOPLE = 5;
 int[] sales = new int[SALESPEOPLE];
int sum;
 Scanner sc = new Scanner(System.in);
 for (int i=0; i<sales.length; i++)
 {
 System.out.print("Enter sales for salesperson"+i+":");
 sales[i] = sc.nextInt();
 }
 System.out.println("\nSalesperson Sales");
 System.out.println("                     ");
 sum = 0;
 for (int i=0; i<sales.length; i++)
 {
 System.out.println(" " + i + " " + sales[i]);
 sum += sales[i];
 }
 System.out.println("\nTotal sales: " + sum);
 sc.close();
 }
}