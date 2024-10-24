import java.util.Scanner;


class AgeOutOfRangeException extends Exception {
    public AgeOutOfRangeException(String message) {
        super(message);
    }
}

class LowCGpaException extends Exception {
    public LowCGpaException(String message) {
        super(message);
    }
}

public class p6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Enter your age and CGPA");
			int age = sc.nextInt();
			int cgpa = sc.nextInt();
			sc.close();
			if (age > 25) {
				throw new AgeOutOfRangeException("Must be younger than 25");
			}
			else if (cgpa < 8) {
				throw new LowCGpaException("CGPA must be greater than 8");
			}
			else {
				System.out.println("Your application is accepted and is under study");
			}
		}
		catch (AgeOutOfRangeException e) {
			System.out.println(e);
		}
		catch (LowCGpaException e) {
		       System.out.println(e);
	    }
 	}		
}
