interface Stackop {
    void push(int i);
    int pop();
}

class FixStack implements Stackop {
    private int stk[];
    private int tos=-1;
    FixStack(int size) {
        stk = new int[size];
    }
    public void push(int i) {
        if(tos==stk.length-1) {
            System.out.println("Stack overflow");
            return;
        }
        stk[++tos]=i;
    }
    public int pop() {
        if(tos==-1) {
            System.out.println("Stack underflow");
            return -1;
        }
        return stk[tos--];
    }
}

class DynStack implements Stackop {
    private int stk[];
    private int tos=-1;
    DynStack(int size) {
        stk = new int[size];
    }
    public void push(int i) {
        if(tos==stk.length-1) {
            System.out.println("Stack overflow doubling size..");
            int t[] = new int[2*stk.length];
            for(int j=0;j<stk.length;j++) {
                t[j]=stk[j];
            }
            stk = t;
        }
        stk[++tos]=i;
    }
    public int pop() {
        if(tos==-1) {
            System.out.println("Stack underflow");
            return -1;
        }
        return stk[tos--];
    }
}

public class ProgB1 {
    public static void main(String[] args) {
        int i;
        FixStack fs = new FixStack(3);
        for(i=0;i<3;i++) {
            fs.push(i);
        }
        System.out.println("Fixed stack contents are:");
        for(i=0;i<3;i++) {
            System.out.println(fs.pop());
        }

        DynStack ds = new DynStack(3);
        for(i=0;i<5;i++) {
            ds.push(i);
        }
        System.out.println("Dynamic stack contents are:");
        for(i=0;i<5;i++) {
            System.out.println(ds.pop());
        }

        Stackop mystk;

        mystk = fs;
        for(i=0;i<3;i++) {
            mystk.push(i);
        }
        System.out.println("Fixed stack contents using interface reference are:");
        for(i=0;i<3;i++) {
            System.out.println(mystk.pop());
        }

        mystk = ds;
        for(i=0;i<5;i++) {
            mystk.push(i);
        }
        System.out.println("Dynamic stack contents  using interface reference are:");
        for(i=0;i<5;i++) {
            System.out.println(mystk.pop());
        }
    }
}
