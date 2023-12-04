package My_Code.Week2;

import java.util.Scanner;

public class Sales {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter the number of salespeople: ");
        int SALESPEOPLE = scan.nextInt();
        int[] sales = new int[SALESPEOPLE];
        int totalSales = 0;
        int maxSale = Integer.MIN_VALUE;
        int minSale = Integer.MAX_VALUE;
        int maxSalesperson = 0, minSalesperson = 0;

        for (int i = 0; i < SALESPEOPLE; i++) {
            System.out.print("Enter the sales for salesperson " + (i + 1) + ": ");
            sales[i] = scan.nextInt();
            totalSales += sales[i];

            if (sales[i] > maxSale) {
                maxSale = sales[i];
                maxSalesperson = i + 1;
            }

            if (sales[i] < minSale) {
                minSale = sales[i];
                minSalesperson = i + 1;
            }
        }

        double averageSale = (double) totalSales / SALESPEOPLE;

        System.out.println("\nSales Report:");
        for (int i = 0; i < SALESPEOPLE; i++) {
            System.out.println("Salesperson " + (i + 1) + " had sales of $" + sales[i]);
        }

        System.out.println("\nTotal sales: $" + totalSales);
        System.out.println("Average sale: $" + averageSale);
        System.out.println("Salesperson " + maxSalesperson + " had the highest sale with $" + maxSale);
        System.out.println("Salesperson " + minSalesperson + " had the lowest sale with $" + minSale);

        System.out.print("\nEnter a value: ");
        int value = scan.nextInt();
        int numSalesExceeded = 0;

        System.out.println("\nSalespeople who exceeded $" + value + ":");
        for (int i = 0; i < SALESPEOPLE; i++) {
            if (sales[i] > value) {
                System.out.println("Salesperson " + (i + 1) + " had sales of $" + sales[i]);
                numSalesExceeded++;
            }
        }

        System.out.println("Total number of salespeople whose sales exceeded $" + value + ": " + numSalesExceeded);
        scan.close();
    }

}
