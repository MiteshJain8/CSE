package My_Code.Week2;
// import java.util.*;

// public class Sales {
//  public static void main(String[] args)
//  {
//  final int SALESPEOPLE = 5;
//  int[] sales = new int[SALESPEOPLE];
// int sum;
//  Scanner sc = new Scanner(System.in);
//  for (int i=0; i<sales.length; i++)
//  {
//  System.out.print("Enter sales for salesperson "+i+": ");
//  sales[i] = sc.nextInt();
//  }
//  System.out.println("\nSalesperson Sales");
//  System.out.println("                     ");
//  sum = 0;
//  for (int i=0; i<sales.length; i++)
//  {
//  System.out.println(" " + i + " " + sales[i]);
//  sum += sales[i];
//  }
//  System.out.println("\nTotal sales: " + sum);
//  sc.close();
//  }
// }

import java.util.Scanner;

public class Sales {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of salespeople: ");
        int numSalespeople = scanner.nextInt();
        int[] sales = new int[numSalespeople];
        int totalSales = 0;
        int maxSale = Integer.MIN_VALUE;
        int minSale = Integer.MAX_VALUE;

        for (int i = 0; i < numSalespeople; i++) {
            System.out.print("Enter the sales for salesperson " + (i + 1) + ": ");
            sales[i] = scanner.nextInt();
            totalSales += sales[i];

            if (sales[i] > maxSale) {
                maxSale = sales[i];
            }

            if (sales[i] < minSale) {
                minSale = sales[i];
            }
        }

        double averageSale = (double) totalSales / numSalespeople;

        System.out.println("\nSales Report:");
        for (int i = 0; i < numSalespeople; i++) {
            System.out.println("Salesperson " + (i + 1) + " had sales of ₹" + sales[i]);
        }

        System.out.println("\nTotal sales: ₹" + totalSales);
        System.out.println("Average sale: ₹" + averageSale);
        System.out.println("Salesperson with the highest sale: Salesperson " + (findSalespersonId(sales, maxSale) + 1) + " with ₹" + maxSale);
        System.out.println("Salesperson with the lowest sale: Salesperson " + (findSalespersonId(sales, minSale) + 1) + " with ₹" + minSale);

        System.out.print("\nEnter a value: ");
        int value = scanner.nextInt();
        int numSalesExceeded = 0;

        System.out.println("\nSalespeople who exceeded ₹" + value + ":");
        for (int i = 0; i < numSalespeople; i++) {
            if (sales[i] > value) {
                System.out.println("Salesperson " + (i + 1) + " had sales of ₹" + sales[i]);
                numSalesExceeded++;
            }
        }

        System.out.println("Total number of salespeople whose sales exceeded ₹" + value + ": " + numSalesExceeded);
        scanner.close();
    }

    private static int findSalespersonId(int[] sales, int sale) {
        for (int i = 0; i < sales.length; i++) {
            if (sales[i] == sale) {
                return i;
            }
        }
        return -1;
    }
}
