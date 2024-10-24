package NumberConversion;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Binary conversion
        bin binaryConverter = new bin();
        System.out.print("Enter a number to convert to binary: ");
        int number = sc.nextInt();
        String binary = binaryConverter.toBinary(number);
        System.out.println("Binary: " + binary);
        System.out.print("Enter a binary number to convert to decimal: ");
        String binaryInput = sc.next();
        int decimalFromBinary = binaryConverter.fromBinary(binaryInput);
        System.out.println("Decimal: " + decimalFromBinary);

        // Octal conversion
        oct octalConverter = new oct();
        System.out.print("Enter a number to convert to octal: ");
        number = sc.nextInt();
        String octal = octalConverter.toOctal(number);
        System.out.println("Octal: " + octal);
        System.out.print("Enter an octal number to convert to decimal: ");
        String octalInput = sc.next();
        int decimalFromOctal = octalConverter.fromOctal(octalInput);
        System.out.println("Decimal: " + decimalFromOctal);

        // Hexadecimal conversion
        hex hexConverter = new hex();
        System.out.print("Enter a number to convert to hexadecimal: ");
        number = sc.nextInt();
        String hex = hexConverter.toHexadecimal(number);
        System.out.println("Hexadecimal: " + hex);
        System.out.print("Enter a hexadecimal number to convert to decimal: ");
        String hexInput = sc.next();
        int decimalFromHex = hexConverter.fromHexadecimal(hexInput);
        System.out.println("Decimal: " + decimalFromHex);
        
        sc.close();
    }
}

