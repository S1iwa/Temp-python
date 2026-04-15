import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class FileReader {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String filePath = scanner.nextLine().trim();
        scanner.close();

        long totalCharacters = 0;
        long totalWords = 0;
        long totalLines = 0;

        Map<Character, Long> charFrequencies = new HashMap<>();
        Map<String, Long> wordFrequencies = new HashMap<>();

        try (BufferedReader reader = new BufferedReader(new java.io.FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                totalLines++;
                // +1 jeśli znak nowej linii zaliczamy jako character
                totalCharacters += line.length() + 1;

                // Zliczanie znaków ignorując białe znaki
                for (char c : line.toCharArray())
                    if (!Character.isWhitespace(c))
                        charFrequencies.put(c, charFrequencies.getOrDefault(c, 0L) + 1);

                // Zliczanie słów (podział po białych znakach)
                String[] words = line.split("\\s+");
                for (String word : words) {
                    if (word.isEmpty())
                        continue;
                    totalWords++;
                    String cleanWord = word.replaceAll("[^\\p{L}\\p{Nd}]+", "").toLowerCase();
                    if (!cleanWord.isEmpty())
                        wordFrequencies.put(cleanWord, wordFrequencies.getOrDefault(cleanWord, 0L) + 1);
                }
            }

            // Znalezienie najczęściej występującego znaku
            char mostFrequentChar = '\0';
            long maxCharCount = 0;
            for (Map.Entry<Character, Long> entry : charFrequencies.entrySet())
                if (entry.getValue() > maxCharCount) {
                    maxCharCount = entry.getValue();
                    mostFrequentChar = entry.getKey();
                }

            // Znalezienie najczęściej występującego słowa
            String mostFrequentWord = "";
            long maxWordCount = 0;
            for (Map.Entry<String, Long> entry : wordFrequencies.entrySet())
                if (entry.getValue() > maxWordCount) {
                    maxWordCount = entry.getValue();
                    mostFrequentWord = entry.getKey();
                }

            // Wypisanie wyniku w formacie JSON
            System.out.println("{");
            System.out.println("  \"file_path\": \"" + escapeJson(filePath) + "\",");
            System.out.println("  \"total_characters\": " + totalCharacters + ",");
            System.out.println("  \"total_words\": " + totalWords + ",");
            System.out.println("  \"total_lines\": " + totalLines + ",");
            System.out.println("  \"most_frequent_character\": \"" + escapeJson(String.valueOf(mostFrequentChar)) + "\",");
            System.out.println("  \"most_frequent_word\": \"" + escapeJson(mostFrequentWord) + "\"");
            System.out.println("}");

        } catch (IOException e) {
            System.err.println("{ \"error\": \"Nie można odczytać pliku: " + escapeJson(e.getMessage()) + "\" }");
        }
    }

    private static String escapeJson(String input) {
        if (input == null)
            return "";
        return input.replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\n", "\\n")
                .replace("\r", "\\r");
    }
}