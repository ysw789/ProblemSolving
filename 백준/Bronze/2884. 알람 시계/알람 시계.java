import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        final int MINUTE_PREFIX = 60;
        final int HOUR_PREFIX = 24;
        final int EARLY_SETTING_PREFIX = 45;

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = reader.readLine().split(" ");
        int h = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        m = m - EARLY_SETTING_PREFIX;
        if (m < 0) {
            m += MINUTE_PREFIX;
            h--;
            if (h < 0) {
                h += HOUR_PREFIX;
            }
        }

        writer.write(h + " " + m);
        writer.close();
    }
}
