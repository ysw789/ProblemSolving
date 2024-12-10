import java.io.*;

public class Main {
    final static String[] CROATIAN = new String[]{"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    final static String REPLACEMENT = "*";

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = reader.readLine().trim();

        for (String s : CROATIAN)
            input = input.replace(s, REPLACEMENT);

        writer.write(String.valueOf(input.length()));

        writer.close();
        reader.close();
    }
}
