import java.io.*;

public class Main {
    final static String BLANK = " ";

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] split = reader.readLine().trim().split(BLANK);
        int n = Integer.parseInt(split[0]);
        int m = Integer.parseInt(split[1]);

        int[] cards = new int[n];
        String[] cardsInput = reader.readLine().trim().split(BLANK);
        for (int i = 0; i < n; i++)
            cards[i] = Integer.parseInt(cardsInput[i]);

        writer.write(String.valueOf(getResult(n, m, cards)));

        writer.close();
        reader.close();
    }

    public static int getResult(int n, int m, int[] input) {
        int max = 0;
        for (int i = 0; i < n - 2; i++) {

            for (int j = i + 1; j < n - 1; j++) {
                if (input[i] + input[j] > m) continue;

                for (int k = j + 1; k < n; k++) {
                    if (input[j] + input[k] > m) continue;

                    int temp = input[i] + input[j] + input[k];

                    if (temp == m)
                        return temp;

                    if (max < temp && temp < m)
                        max = temp;
                }
            }
        }
        return max;
    }
}
