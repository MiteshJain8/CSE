package NumberConversion;

public class hex {
	 public String toHexadecimal(int number) {
        	return Integer.toHexString(number).toUpperCase();
    	}

    	public int fromHexadecimal(String hex) {
        	return Integer.parseInt(hex, 16);
    	}
}
