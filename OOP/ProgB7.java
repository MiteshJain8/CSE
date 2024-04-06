interface Calc {
    public int res(int x,  int y);
}

public class ProgB7 {
    public static void main(String[] args) {
        Calc a = (x,y) -> (x+y);
        System.out.println(a.res(2,3));
        Calc m = (x,y) -> (x*y);
        System.out.println(m.res(4,5));
    }
}
