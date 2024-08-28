import java.util.*;

class Name extends Exception {
    String name;

    Name(String n) {
        name = n;
    }

    public String toString() {
        return name + " is not a valid name";
    }
}

class Age extends Exception {
    int age;

    Age(int n) {
        age = n;
    }

    public String toString() {
        return age + " is above 50";
    }
}

class Emp {
    int age;
    String name;

    Emp(int a, String n) {
        age = a;
        name = n;
    }

    void display() {
        System.out.println("Employee name: " + name + ", age: " + age);
    }
}

public class ProgB4 {
    public static void main(String[] args) throws Name, Age {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();
        String name = sc.next();
        boolean b = true;
        try {
            int h = Integer.parseInt(name);
            b = false;
            throw new Name(name);
        } catch (Name e) {
            System.out.println(e);
        } catch (Exception e) {
            System.out.println(e);
        }

        try {
            if(age>50) {
                b=false;
                throw new Age(age);
            } 
        } catch (Age e) {
            System.out.println(e);
        }

        if(b) {
            Emp e1 = new Emp(age, name);
            e1.display();
        }
    }
}
