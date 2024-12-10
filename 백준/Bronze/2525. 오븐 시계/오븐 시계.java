import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        final int MINUTE_PREFIX = 60;
        final int HOUR_PREFIX = 24;

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] currentTime = reader.readLine().split(" ");
        int h = Integer.parseInt(currentTime[0]);
        int m = Integer.parseInt(currentTime[1]);

        int cookingTime = Integer.parseInt(reader.readLine());

        m += cookingTime;
        if (m >= MINUTE_PREFIX) {
            int addedHour = m / MINUTE_PREFIX;
            m %= MINUTE_PREFIX;
            h += addedHour;
            if (h >= HOUR_PREFIX)
                h -= HOUR_PREFIX;
        }

        writer.write(h + " " + m);
        writer.close();
    }
}
