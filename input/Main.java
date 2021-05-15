public class Main {

    //START (Methods and functions)

    //END
    public static void main(String []args) {

        //START (main code)
        int[][] t = new int[][] { { 4, 7 }, { 6, 3 }, { 2, 1, 8 }, { 5 } };
        t[3] = t[1];
        t[1][0] = 3;
        t[3][1] = 8;
        System.out.println(t[3][0] + " " + t[1][1]);
        //END
    }
}
