class Mul extends Thread {
    int n;

    Mul(int num) {
        n = num;
    }

    synchronized void Table() {
        try {
            for (int i = 1; i <= 10; i++) {
                System.out.println(i * n);
                Thread.sleep(1000);
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public void run() {
        Table();
    }
}

public class ProgB6 {
    public static void main(String[] args) {
        Mul m1 = new Mul(8);
        m1.start();
        Mul m2 = new Mul(9);
        m2.start();
    }
}
