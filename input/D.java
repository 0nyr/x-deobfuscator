public class D {
    public static int i = 7;
    private int j;
    public D(int a, int b) {
      i = a;
      this.j = b;
    }
    public static int getI() {
      return i;
    }
    public int getIJ() {
      return i * this.j;
    }
  }