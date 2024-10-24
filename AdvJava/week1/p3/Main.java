import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CaesarCipher cipher = new CaesarCipher();

        // Input for Phone Number
        System.out.print("Enter Phone Number: ");
        String phoneNumber = scanner.nextLine();
        // Encrypt Phone Number
        String encryptedPhone = cipher.encrypt(2, 3, phoneNumber);
        System.out.println("Encrypted Phone Number: " + encryptedPhone);
        // Decrypt Phone Number
        String decryptedPhone = cipher.decrypt(2, 3, encryptedPhone);
        System.out.println("Decrypted Phone Number: " + decryptedPhone);

        // Input for Email ID
        System.out.print("Enter Email ID: ");
        String emailId = scanner.nextLine();
        // Encrypt Email ID
        String encryptedEmail = cipher.encrypt(1, 2, emailId);
        System.out.println("Encrypted Email ID: " + encryptedEmail);
        // Decrypt Email ID
        String decryptedEmail = cipher.decrypt(1, 2, encryptedEmail);
        System.out.println("Decrypted Email ID: " + decryptedEmail);

        scanner.close();
    }
}

