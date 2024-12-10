import java.io.*;

public class Main {
    final static String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    final static String SPACING = " ";
    final static int NOT_INCLUDED = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = reader.readLine();

        for (char i : ALPHABET.toCharArray()) {
            if (input.contains(String.valueOf(i))) {
                writer.write(input.indexOf(i) + SPACING);
                continue;
            }
            writer.write(NOT_INCLUDED + SPACING);
        }

        writer.close();
        reader.close();
    }
}
