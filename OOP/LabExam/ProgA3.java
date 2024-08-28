abstract class Shape {
    String color;
    boolean filled;
    abstract double getArea();
    Shape() {
        color="green";
        filled=true;
    } 
    Shape(String c, boolean f) {
        color=c;
        filled=f;
    }
    boolean isFilled() {
        return filled;
    }
    void setFilled(boolean f) {
        filled=f;
    }
    String getColor() {
        return color;
    }
    void setColor(String c) {
        color=c;
    }
    public String toString() {
        return "A Shape with color of "+color+" and filled: "+filled;
    }
}

class Circle extends Shape {
    int r;
    Circle(int d) {
        super();
        r=d;
    }
    Circle(int d, String c, boolean f) {
        super(c, f);
        r=d;
    }
    double getArea() {
        return 3.14*r*r;
    }
}

final class Rect extends Shape {
    int l,b;
    Rect(int x, int y) {
        super();
        l=x;
        b=y;
    }
    Rect(int x, int y, String c, boolean f) {
        super(c, f);
        l=x;
        b=y;
    }
    double getArea() {
        return l*b;
    }
}

public class ProgA3 {
    public static void main(String[] args) {
        Circle c1 = new Circle(5);
        Rect r1 = new Rect(3, 4);
        System.out.println(c1);
        System.out.println(r1);
        c1.setColor("brown");
        c1.setFilled(false);
        r1.setColor("blue");
        System.out.println(c1);
        System.out.println(r1);
        System.out.println("area of rectangle: "+r1.getArea());
        System.out.println("area of circle: "+c1.getArea());
    }
}
