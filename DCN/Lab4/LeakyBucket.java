import java.util.*;

public class LeakyBucket {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter bucket size and rate: ");
        int bucket_cap = sc.nextInt();
        int rate = sc.nextInt();

        System.out.print("\nEnter no. of packets: ");
        int n = sc.nextInt();
        int[] packets = new int[n];
        System.out.println("Enter size of :");
        for(int i=0;i<n;++i){
            System.out.print("\tpacket["+(i+1)+"]: ");
            packets[i] = sc.nextInt();
        }
        int bucket_rem=0, recieved, sent;
        for(int i=0;i<n;++i){
            if(packets[i]>0){
                if(packets[i]+bucket_rem > bucket_cap)
                    recieved = -1;
                else{
                    recieved = packets[i];
                    bucket_rem += packets[i];
                }
            }
            else
                recieved=0;
            if(bucket_rem > rate){
                sent = rate;
                bucket_rem -= rate;
            }
            else{
                sent = bucket_rem;
                bucket_rem = 0;
            }
            System.out.println("\nPacket["+(i+1)+"]: "+packets[i]);
            if(recieved==-1)
                System.out.println("Packet dropped!!");
            else{
                System.out.println("Recieved: "+recieved);
                System.out.println("Sent : "+sent);
                System.out.println("Remaining: "+bucket_rem);
            }
        }
        sc.close();
    }
}