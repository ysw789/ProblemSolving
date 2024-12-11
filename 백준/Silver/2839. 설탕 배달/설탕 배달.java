import java.io.*;

public class Main {
    final static int BAG_5KG = 5;
    final static int BAG_3KG = 3;
    final static int NOT_DIVIDED = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(reader.readLine().trim());
        int bags = 0;

        while (n >= 0) {
            if (n % BAG_5KG == 0) {
                bags += n / BAG_5KG;
                break;
            }
            n -= BAG_3KG;
            bags++;
        }

        if (n < 0) {
            bags = NOT_DIVIDED;
        }

        writer.write(String.valueOf(bags));

        writer.close();
        reader.close();
    }
}
