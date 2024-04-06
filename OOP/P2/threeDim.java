package P2;
import P1.*;

public class threeDim extends twoDim {
    private int z;
    public threeDim() {
        super(0,0);
        z=0;
    }
    public threeDim(int a, int b, int c) {
        super(a,b);
        z=c;
    }
    public String toString() {
        return super.toString()+" z:"+z;
    }
}
