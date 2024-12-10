import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        final int wordsCount = Integer.parseInt(reader.readLine().trim());

        int groupCount = 0;
        for (int cnt = 0; cnt < wordsCount; cnt++) {
            final String input = reader.readLine().trim();
            int error = 0;
            for (int i = 0; i < input.length() - 1; i++) {
                if (input.charAt(i) != input.charAt(i + 1)) {
                    final String newInput = input.substring(i + 1);
                    for (int j = 0; j < newInput.length(); j++)
                        if (input.charAt(i) == newInput.charAt(j))
                            error++;
                }
            }
            if (error == 0) groupCount++;
        }

        writer.write(String.valueOf(groupCount));

        writer.close();
        reader.close();
    }
}
