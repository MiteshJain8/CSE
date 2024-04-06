class Car {
    int speed;
    double regularPrice;
    String color;
    Car(int s, double p, String c) {
        speed=s;
        regularPrice=p;
        color=c;
    }
    double getSalePrice() {
        return regularPrice;
    } 
}

class Truck extends Car {
    int weight;
    Truck(int s, double p, String c, int w) {
        super(s, p, c);
        weight=w;
    }
    double getSalePrice(){
        if(weight>2000) {
            return regularPrice*0.9;
        } else {
            return regularPrice*0.8;
        }
    }
}

class Ford extends Car {
    int year;
    int manufacturerDiscount;
    Ford(int s, double p, String c, int y, int d) {
        super(s, p, c);
        year=y;
        manufacturerDiscount=d;
    }
    double getSalePrice(){
        return regularPrice-manufacturerDiscount;
    }
}

class Sedan extends Car {
    int length;
    Sedan(int s, double p, String c, int l) {
        super(s, p, c);
        length=l;
    }
    double getSalePrice(){
        if(length>20)
            return regularPrice*0.95;
        else
            return regularPrice*0.9;
    }
}

public class ProgA5 {
    public static void main(String[] args) {
        Truck t=new Truck(65,2500000,"Red",3000); 
        System.out.println("Price of truck is "+t.getSalePrice()); 
        Car c = new Car(100,800000,"Black"); 
        System.out.println("Price of Car is "+c.getSalePrice()); 
        Ford f= new Ford(120,2200000,"Yellow",2016,120000); 
        System.out.println("Price of ford is "+f.getSalePrice()); 
        Sedan s= new Sedan(100,3500000,"Blue",22); 
        System.out.println("Price of Sedan is "+s.getSalePrice()); 
    }
}
