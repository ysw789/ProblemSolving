import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        final String input = reader.readLine().trim();

        int result = 1;
        for (int i = 1; i <= input.length() / 2; i++) {
            if ((int) input.charAt(i - 1) != (int) input.charAt(input.length() - i)) {
                result = 0;
                break;
            }
        }

        writer.write(String.valueOf(result));

        writer.close();
        reader.close();
    }
}
