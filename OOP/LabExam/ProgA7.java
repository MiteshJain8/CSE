class Customer {
    int ID, discount;
    String name;
    Customer(int i, String n, int d) {
        ID=i;
        name=n;
        discount=d;
    }
    int getID() {
        return ID;
    }
    String getName() {
        return name;
    }
    int getDiscount() {
        return discount;
    }
    public String toString() {
        return name+"("+ID+")";
    }
}

class Invoice {
    int ID;
    Customer customer;
    double amount;
    Invoice(int i, Customer c, double amt) {
        ID=i;
        customer=c;
        amount=amt;
    }
    int getID() {
        return ID;
    } 
    Customer getCustomer() {
        return customer;
    } 
    void setCustomer(Customer c) {
        customer=c;
    } 
    String getAmount() {
        return Double.toString(amount);
    }
    void setAmount(double amt) {
        amount=amt;
    }
    String getCustomerName() {
        return customer.getName();
    }
    double getAmountAfterDiscount() {
        return amount-(amount*customer.getDiscount()/100);
    }
}

public class ProgA7 {
    public static void main(String[] args) {
        Customer c1 = new Customer(11, "Kiran", 5);
        System.out.println("Customer 1 is: "+c1);
        Customer c2 = new Customer(12, "Manu", 5);
        Invoice i = new Invoice(101, c1, 1000);
        System.out.println("Customer name: "+i.getCustomerName());
        i.setCustomer(c2);
        i.setAmount(2000);
        System.out.println("\n Invoice Details \n");
        System.out.println("Invoice ID: "+i.getID());
        System.out.println("Customer details: "+i.getCustomer());
        System.out.println("Amount: "+i.getAmount());
        System.out.println("Amount after discount: "+i.getAmountAfterDiscount());
    }
}
