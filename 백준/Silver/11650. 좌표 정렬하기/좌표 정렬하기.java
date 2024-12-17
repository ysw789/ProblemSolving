import java.io.*;
import java.util.Arrays;

public class Main {
    final static String NEXT_LINE = "\n";
    final static String BLANK = " ";

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int size = Integer.parseInt(reader.readLine().trim());
        int[][] points = new int[size][2];

        for (int i = 0; i < size; i++) {
            String[] input = reader.readLine().trim().split(BLANK);
            points[i][0] = Integer.parseInt(input[0]);
            points[i][1] = Integer.parseInt(input[1]);
        }

        Arrays.sort(points, (p1, p2) -> {
            if (p1[0] != p2[0]) {
                return Integer.compare(p1[0], p2[0]);
            } else {
                return Integer.compare(p1[1], p2[1]);
            }
        });

        for (int i = 0; i < size; i++)
            writer.write(points[i][0] + BLANK + points[i][1] + NEXT_LINE);

        writer.close();
        reader.close();
    }
}
