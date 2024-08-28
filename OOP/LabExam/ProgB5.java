import java.util.*;

class Triangle extends Exception {
    public String toString() {
        return "Invalid triangle";
    }
}

public class ProgB5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        try {
            if((a<b+c)&&(b<c+a)&&(c<a+b)) {
                double s = (a+b+c)/2;
                double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
                System.out.println("Area: "+area);
            } else {
                throw new Triangle();
            }
        } catch(Triangle e) {
            System.out.println(e);
        }
    }
}
