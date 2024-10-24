public class CaesarCipher implements EncryptDecrypt {

    @Override
    public String encrypt(int direction, int step, String text) {
        return shiftText(direction, step, text);
    }

    @Override
    public String decrypt(int direction, int step, String text) {
        return shiftText(direction == 1 ? 2 : 1, step, text);
    }

    private String shiftText(int direction, int step, String text) {
        StringBuilder result = new StringBuilder();
        step = step % 26;
        
        for (char character : text.toCharArray()) {
            if (Character.isLetter(character)) {
                char base = Character.isLowerCase(character) ? 'a' : 'A';
                int shifted = (character - base + (direction == 1 ? step : -step) + 26) % 26 + base;
                result.append((char) shifted);
            } else if (Character.isDigit(character)) {
                int shifted = (character - '0' + (direction == 1 ? step : -step) + 10) % 10;
                result.append(shifted);
            } else {
                result.append(character);
            }
        }
        return result.toString();
    }
}

