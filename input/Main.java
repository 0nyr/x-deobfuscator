public class Main {
    public static void main(String []args) {

        //Etart
        int[‍] t = new int[‍] { 4, 7, 6, 3, 2, 1, 8, 5 };
        t[7] = 8;
        int[‍] u = t;
        u[0] = 5;
        System.out.println(t[0] + " " + u[7]);
        int[‍][‍] t = new int[‍][‍] { { 4, 7 }, { 6, 3 }, { 2, 1, 8 }, { 5 } };
        t[3] = t[1];
        t[1][0] = 3;
        t[3][1] = 8;
        System.out.println(t[3][0] + " " + t[1][1]);
        // end
    }
}
