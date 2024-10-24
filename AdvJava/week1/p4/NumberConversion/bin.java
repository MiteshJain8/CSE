package NumberConversion;

public class bin {
    public String toBinary(int number) {
        return Integer.toBinaryString(number);
    }

    public int fromBinary(String binary) {
        return Integer.parseInt(binary, 2);
    }
}

