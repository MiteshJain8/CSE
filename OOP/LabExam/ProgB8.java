import java.util.*;

public class ProgB8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string: ");
        String s = sc.nextLine();
        String S = s.toUpperCase();
        int count=0;
        for (int i=1;i<S.length();i++) {
            if(S.charAt(i-1)==S.charAt(i)) {
                count++;
            }
        }
        System.out.println(count);
    }
}