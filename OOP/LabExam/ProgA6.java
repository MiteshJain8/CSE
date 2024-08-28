class SavingsAcc {
    static int annualInterestRate;
    double savingsBalance;
    SavingsAcc(double s) {
        savingsBalance=s;
    }
    static void modifyInterestRate(int i) {
        annualInterestRate=i;
    }
    void monthlyInterest() {
        double d = savingsBalance*annualInterestRate/12;
        savingsBalance = savingsBalance + d;
    }
    void display() {
        System.out.println(savingsBalance);
    }
}

public class ProgA6 {
    public static void main(String[] args) {
        SavingsAcc s1 = new SavingsAcc(2000);
        SavingsAcc s2 = new SavingsAcc(3000);
        SavingsAcc.modifyInterestRate(4);
        s1.monthlyInterest();
        s2.monthlyInterest();
        s1.display();
        s2.display();

        SavingsAcc.modifyInterestRate(5);
        s1.monthlyInterest();
        s2.monthlyInterest();
        s1.display();
        s2.display();
    }
}
