import java.util.*;
import java.io.*;
 
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException{
        int n = readInt();
        int[] numlist = new int[1001];
        for (int i = 0; i < n; i ++) {
            int a = readInt();
            numlist[a] ++;
        }
        int numatmax = 1;
        int max = 0;
        int firstmaxpos = 0;
        int lastmaxpos = 0;
        for (int i = 1; i < 1001; i ++) {
            if (numlist[i] > max) {
                max = numlist[i];
                numatmax = 1;
                firstmaxpos = i;
            }
            else if (numlist[i] == max) {
                numatmax += 1;
                lastmaxpos = i;
            }
        }
        if (numatmax > 1) {
            System.out.println(lastmaxpos - firstmaxpos);
        }
        else {
            int maax = 0;
            int firstpos = 0;
            int lastpos = 0;
            for (int i = 1; i < 1001; i ++) {
                if (numlist[i] > maax && numlist[i] < max) {
                    maax = numlist[i];
                    firstpos = i;
                    lastpos = i;
                }
                else if (numlist[i] == maax) {
                    lastpos = i;
                }
            }
            int a = firstpos - firstmaxpos;
            int b = lastpos - firstmaxpos;
            if (a < 0) {
                a = -a;
            }
            if (b < 0) {
                b = -b;
            }
            if (a > b) {
                System.out.println(a);
            }
            else {
                System.out.println(b);
            }
        }
    }
    static String next () throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }
    static int readInt () throws IOException {
        return Integer.parseInt(next());
    }
}