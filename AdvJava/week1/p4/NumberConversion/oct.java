package NumberConversion;

public class oct {
	public String toOctal(int number) {
		return Integer.toOctalString(number);
	}

	public int fromOctal(String octal) {
		return Integer.parseInt(octal, 8);
	}
}
