import java.util.*;

abstract class Vehicle {
    boolean hasHelmet;
    int yom;
    abstract void putData();
    abstract void getData();
    Vehicle(boolean h, int y) {
        hasHelmet=h;
        yom=y;
    }
}

class twoWheeler extends Vehicle {
    twoWheeler(int y) {
        super(true, y);
    }
    private String brand;
    protected int cost;
    String EngineType;
    public String color;
    void getData() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter brand name, cost, engine type and color of two wheeler:");
        brand=sc.nextLine();
        cost=sc.nextInt();
        EngineType=sc.nextLine();
        color=sc.nextLine();
    }
    void putData() {
        System.out.println("\n Two Wheeler details");
        System.out.println("Brand: "+brand+"\nCost: "+cost+"\nEngine type: "+EngineType+"\nColor: "+color+"\nYear of manufacture: "+yom+"\nHas helmet: "+hasHelmet);
    }
}

final class fourWheeler extends Vehicle {
    fourWheeler(int y) {
        super(false, y);
    }
    void getData(){}
    void putData() {
        System.out.println("\n Four Wheeler details");
        System.out.println("Year of manufacture: "+yom+"\nHas helmet: "+hasHelmet);
    }
} 

public class ProgA2 {
    public static void main(String[] args) {
        twoWheeler t1 = new twoWheeler(2012);
        fourWheeler f1 = new fourWheeler(2016);
        f1.putData();
        t1.getData();
        t1.putData();
    }
}
