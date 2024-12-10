import java.io.*;

public class Main {
    static final String PRICE_MATCHED = "Yes";
    static final String PRICE_NOT_MATCHED = "No";

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        final int totalPrice = Integer.parseInt(reader.readLine());
        final int totalCount = Integer.parseInt(reader.readLine());

        int sum = 0;
        for (int i = 0; i < totalCount; i++) {
            String[] input = reader.readLine().split(" ");
            sum += (Integer.parseInt(input[0]) * Integer.parseInt(input[1]));
        }

        writer.write((sum == totalPrice) ? PRICE_MATCHED : PRICE_NOT_MATCHED);

        writer.close();
        reader.close();
    }
}
