import java.util.Scanner;

public class CRC {
    public static String xor(String a, String b) {
        int len = Math.max(a.length(), b.length());
        int x = Integer.parseInt(a, 2);
        int y = Integer.parseInt(b, 2);
        String result = Integer.toBinaryString((x ^ y));
        result = String.format("%" + len + "s", result).replace(" ","0");
        return result;
    }

    public static String divide(String dividend, String divisor) {
        int dLen = divisor.length();
        int dndLen = dividend.length();
        while (dndLen >= dLen) {
            String temp;
            if (dividend.charAt(0) == '1') {
                temp = xor(divisor, dividend.substring(0, dLen));
            } else {
                temp = xor("0", dividend.substring(0, dLen));
            }
            dividend = temp.substring(1) + dividend.substring(dLen);
            dndLen -= 1;
        }
        return dividend;
    }

    public static String generate(String message, String generator) {
        int msgLen = message.length();
        int gtrLen = generator.length();

        String dividend = String.format("%-" + (msgLen + gtrLen - 1)
                + "s", message).replace(' ', '0');
        String rem = divide(dividend, generator);
        return message + rem;
    }

    public static boolean checkCodeWord(String cw, String gw) {
        String temp = divide(cw, gw);
        return (Integer.parseInt(temp) == 0);
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Using CRC-CCITT");
        String generator = "10001000000100001";
        while (true) {
            System.out.println("1. Generate codeword");
            System.out.println("2. Check data");
            int input = s.nextInt();
            switch (input) {
                case 1:
                    System.out.print("Enter dataword: ");
                    String dataword = s.next();
                    System.out.println("Codeword: " +
                            generate(dataword, generator));
                    break;
                case 2:
                    System.out.print("Enter codeword: ");
                    String codeword = s.next();
                    if (checkCodeWord(codeword, generator)) {
                        System.out.println("No Error");
                    } else {
                        System.out.println("Error");
                    }
            }
        }
    }
}