class Person {
    private String name, address;
    Person(String n, String a) {
        name=n;
        address=a;
    }
    String getName() {
        return name;
    }
    String getAddress() {
        return address;
    }
    void setAddress(String a) {
        address=a;
    }
    public String toString() {
        return name+"("+address+")";
    }
}

class Students extends Person {
    int numCourses=0;
    String courses[] = new String[30];
    int grades[] = new int[30];
    Students(String n, String a) {
        super(n, a);
    }
    void addCourseGrade(String course, int grade) {
        if(numCourses<=29) {
            courses[numCourses]=course;
            grades[numCourses]=grade;
            numCourses++;
        } else {
            System.out.println("Max courses taken");
        }
    }
    void printGrades() {
        for(int i=0; i<numCourses;i++) {
            System.out.println("Course: "+courses[i]+" grade: "+grades[i]);
        }
    }
    double getAvg() {
        double d=0;
        for(int i=0;i<numCourses;i++) {
            d+=grades[i];
        }
        return d/numCourses;
    }
    public String toString() {
        return super.toString();
    }
}

class Teachers extends Person {
    int numCourses;
    String courses[] = new String[5];
    Teachers(String n, String a) {
        super(n, a);
    }
    void addCourse(String course) {
        if(numCourses<=4) {
            courses[numCourses]=course;
            numCourses++;
            System.out.println(course+" added");
        } else {
            System.out.println("max courses limit reached");
        }
    }
    void removeCourse(String course) {
        if(numCourses!=0) {
            for(int i=0;i<numCourses;i++) {
                if(courses[i]==course) {
                    courses[i]=" ";
                    System.out.println(course+" removed");
                    break;
                } else if(i==numCourses-1) {
                    System.out.println("Course does not exist");
                }
            }
        } else {
            System.out.println("Zero courses");
        }
    }
    public String toString() {
        return super.toString();
    }
}

public class ProgA8 {
    public static void main(String[] args) {
        Students s1 = new Students("Raju", "Bangalore"); 
        System.out.println (s1); 
        s1.addCourseGrade ("Maths", 85);
        s1.addCourseGrade ("OOPS", 80); 
        s1.addCourseGrade ("DS",75);  
        s1.addCourseGrade ("DMS", 70); 
        s1.printGrades(); 
        System.out.println(s1.getAvg()); 

        Teachers t1 = new Teachers("CC","Delhi");
        System.out.println(t1);
        t1.removeCourse("Maths");
        t1.addCourse("Maths");
        t1.addCourse("OOP");
        t1.addCourse("DS");
        t1.addCourse("DMS");
        t1.addCourse("Maths");
        t1.addCourse("UNIX");
        t1.removeCourse("Maths");
        t1.removeCourse("Maths");
        t1.removeCourse("Maths");
    }
}
