import java.io.*;

public class Main {
    final static String BLANK = " ";

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        double totalPoint = 0;
        double totalRating = 0;
        for (int i = 0; i < 20; i++) {
            final String[] input = reader.readLine().trim().split(BLANK);

            if (input[2].equals("P"))
                continue;

            final double point = Double.parseDouble(input[1]);
            final double rating = getRating(input[2], point);
            totalPoint += point;
            totalRating += rating;
        }

        writer.write(String.valueOf(totalRating / totalPoint));

        writer.close();
        reader.close();
    }

    private static double getRating(String grade, double point) {
        return switch (grade) {
            case "A+" -> point * 4.5;
            case "A0" -> point * 4.0;
            case "B+" -> point * 3.5;
            case "B0" -> point * 3.0;
            case "C+" -> point * 2.5;
            case "C0" -> point * 2.0;
            case "D+" -> point * 1.5;
            case "D0" -> point;
            default -> 0;
        };
    }
}
