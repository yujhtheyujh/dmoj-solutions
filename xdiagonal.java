import java.util.*;
import java.io.*;
 
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException{
        int n = readInt();
        int[][] xook = new int[n][n];
        int[] posslope = new int[2 * n - 1];
        int[] negslope = new int[2 * n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                xook[i][j] = readInt();
                    posslope[i + j] += xook[i][j];
                    negslope[n - 1 + i - j] += xook[i][j];
            }
        }
        int max = 0;
        int tempmax1 = 0;
        int tempmax2 = 0;
        for (int i = 0; i < n * 2 - 1; i += 2){
            if (posslope[i] > tempmax1) {
                tempmax1 = posslope[i];
            }
        }
        for (int i = n % 2; i < n * 2 - 1; i += 2){
            if (negslope[i] > tempmax2) {
                tempmax2 = negslope[i];
            }
        }
        max = tempmax1 + tempmax2;
        tempmax1 = 0;
        tempmax2 = 0;
        for (int i = 1; i < n * 2 - 1; i += 2){
            if (posslope[i] > tempmax1) {
                tempmax1 = posslope[i];
            }
        }
        for (int i = (n + 1) % 2; i < n * 2 - 1; i += 2){
            if (negslope[i] > tempmax2) {
                tempmax2 = negslope[i];
            }
        }
        if (max < tempmax1 + tempmax2) {
            max = tempmax1 + tempmax2;
        }
        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                if (posslope[i + j] + negslope[n - 1 + i - j] - xook[i][j]> max) {
                    max = posslope[i + j] + negslope[n - 1 + i - j] - xook[i][j];
                }
            }
        }
        for (int i = 0; i < n - 1; i ++) {
            for (int j = (n - i + 1) % 2; j < n - i - 1; j += 2) {
                if (posslope[i] + negslope[j] > max) {
                    max = posslope[i] + negslope[j];
                }
                if (posslope[2 * n - 2 - i] + negslope[j] > max) {
                    max = posslope[2 * n - 2 - i] + negslope[j];
                }
            }
            for (int j = n * 2 - 2 - (n + i + 1) % 2; j > n + i - 1; j -= 2) {
                if (posslope[i] + negslope[j] > max) {
                    max = posslope[i] + negslope[j];
                }
                if (posslope[2 * n - 2 - i] + negslope[j] > max) {
                    max = posslope[2 * n - 2 - i] + negslope[j];
                }
            }
        }
        System.out.println(max);
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