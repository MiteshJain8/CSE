abstract class Shape {
    abstract double area();
    abstract void display();
}
class Rectangle extends Shape {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    double area() {
        return length * width;
    }

    @Override
    void display() {
        System.out.println("Shape: Rectangle");
        System.out.println("Length: " + length);
        System.out.println("Width: " + width);
        System.out.println("Area: " + area());
    }
}
class Triangle extends Shape {
    private double base;
    private double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    @Override
    double area() {
        return 0.5 * base * height;
    }

    @Override
    void display() {
        System.out.println("Shape: Triangle");
        System.out.println("Base: " + base);
        System.out.println("Height: " + height);
        System.out.println("Area: " + area());
    }
}
class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }

    @Override
    void display() {
        System.out.println("Shape: Circle");
        System.out.println("Radius: " + radius);
        System.out.println("Area: " + area());
    }
}
public class p2 {
    public static void main(String[] args) {
        // Creating an array of Shape references
        Shape[] shapes = new Shape[3];

        // Assigning different shapes to the array
        shapes[0] = new Rectangle(5.0, 4.0);
        shapes[1] = new Triangle(3.0, 6.0);
        shapes[2] = new Circle(2.5);

        // Dynamic method dispatch
        for (Shape shape : shapes) {
            shape.display();
            System.out.println();
        }
    }
}
