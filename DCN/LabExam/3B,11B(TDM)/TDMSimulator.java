import java.util.Scanner;

public class TDMSimulator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of stations (maximum 10): ");
        int n = sc.nextInt();
        int[] bt = new int[n]; // processing times for each station
        int[] rem_bt = new int[n]; // remaining times for each station
        int[] tat = new int[n]; // completion times for each station
        int[] wt = new int[n]; // waiting times for each station
        float awt = 0, atat = 0; // average waiting and turnaround times

        System.out.println("Enter the processing time for each channel");
        for (int i = 0; i < n; i++) {
            System.out.print("S" + (i+1) + " = ");
            bt[i] = sc.nextInt();
            rem_bt[i] = bt[i];
        }

        System.out.print("Enter the frame size: ");
        int qt = sc.nextInt();

        int count = 0, sq = 0;
        while (true) {
            for (int i = 0; i < n; i++) {
                if (rem_bt[i] == 0) {
                    count++;
                    continue;
                }

                int temp = qt;
                if (rem_bt[i] > qt) {
                    rem_bt[i] -= qt;
                } else {
                    temp = rem_bt[i];
                    rem_bt[i] = 0;
                }

                sq += temp;
                tat[i] = sq;
            }

            if (count == n) {
                break;
            }
            count = 0;
        }

        System.out.println("--------------------------------------------------------");
        System.out.println("Station   Processing Time   Completion Time   Waiting Time");
        System.out.println("--------------------------------------------------------");
        for (int i = 0; i < n; i++) {
            wt[i] = tat[i] - bt[i];
            awt += wt[i];
            atat += tat[i];
            System.out.println("S" + (i+1) + "\t\t" + bt[i] + "\t\t" + tat[i] + "\t\t" + wt[i]);
        }

        awt /= n;
        atat /= n;
        System.out.println("Average Waiting Time: " + awt);
        System.out.println("Average Turnaround Time: " + atat);
    }
}
