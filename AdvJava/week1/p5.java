public class p5 {    
    public synchronized void displayPrime(int n) {
        if (isPrime(n)) {
            System.out.println(n);
        }
    }
    
    private boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public void findPrimesInRange1() {
        for (int i = 1; i <= 100; i++) {

            synchronized (this) {
                displayPrime(i);
            }
        }
    }

    public void findPrimesInRange2() {
        for (int i = 101; i <= 200; i++) {

            synchronized (this) {
                displayPrime(i);
            }
        }
    }

    public static void main(String[] args) {
        p5 primeDisplay = new p5();

        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                primeDisplay.findPrimesInRange1();
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                primeDisplay.findPrimesInRange2();
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        System.out.println("Prime number display completed.");
    }
}

