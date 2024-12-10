import java.io.*;

public class Main {
    final static char SEVERAL = '?';
    final static char ASCII_A_INDEX = 65;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        final String input = reader.readLine().trim().toUpperCase();

        int[] array = new int[26];

        for (int i = 0; i < input.length(); i++)
            array[input.charAt(i) - ASCII_A_INDEX]++;

        int max = -1;
        char ch = SEVERAL;

        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
                ch = (char) (i + 65);
            } else if (array[i] == max) {
                ch = SEVERAL;
            }
        }

        writer.write(String.valueOf(ch));

        writer.close();
        reader.close();
    }
}
