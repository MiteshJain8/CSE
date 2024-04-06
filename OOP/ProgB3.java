// import java.lang.Math.*;

class MathSin extends Thread {
    double deg, result;

    MathSin(double degree) {
        deg = degree;
    }

    public void run() {
        result = Math.sin(deg);
    }
}

class MathCos extends Thread {
    double deg, result;

    MathCos(double degree) {
        deg = degree;
    }

    public void run() {
        result = Math.cos(deg);
    }
}

class MathTan extends Thread {
    double deg, result;

    MathTan(double degree) {
        deg = degree;
    }

    public void run() {
        result = Math.tan(deg);
    }
}

public class ProgB3 {
    public static void main(String[] args) {
        MathSin sin = new MathSin(45);
        MathCos cos = new MathCos(45);
        MathTan tan = new MathTan(45);
        sin.start();
        cos.start();
        tan.start();
        try {
            sin.join();
            cos.join();
            tan.join();
            double result = sin.result+cos.result+tan.result;
            System.out.println("sin(45)+cos(45)+tan(45) = "+result);
        } catch(InterruptedException e) {

        }
    }
}
