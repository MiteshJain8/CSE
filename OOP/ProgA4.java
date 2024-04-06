import java.util.*;

abstract class Student {
    String name;
    int ID;
    int age;
    double grade;
    abstract boolean isPassed(double g);
}

class Undergrad extends Student {
    void getData() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name,ID,age: ");
        name=sc.next();
        ID=sc.nextInt();
        age=sc.nextInt();
    }
    boolean isPassed(double g) {
        grade=g;
        if(g>70)
            return true;
        else
            return false;
    }
    void display() {
        System.out.println("Name: "+name+" ID: "+ID+" age: "+age);
    }
}
class Grad extends Student {
    void getData() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name,ID,age: ");
        name=sc.next();
        ID=sc.nextInt();
        age=sc.nextInt();
    }
    boolean isPassed(double g) {
        grade=g;
        if(g>80)
            return true;
        else
            return false;
    }
    void display() {
        System.out.println("Name: "+name+" ID: "+ID+" age: "+age);
    }
}

public class ProgA4 {
    public static void main(String[] args) {
        Undergrad u1 = new Undergrad();
        u1.getData();
        u1.display();
        if(u1.isPassed(65)) {
            System.out.println("Student passed");
        } else {
            System.out.println("fail");
        }
        Grad g1 = new Grad();
        g1.getData();
        g1.display();
        if(g1.isPassed(85))
            System.out.println("Pass");
        else
            System.out.println("Fail");
    }
}
