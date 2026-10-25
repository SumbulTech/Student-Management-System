import java.util.Scanner;

/**
 * InputValidator.java
 * 
 * A utility class that wraps Scanner and provides safe, validated input methods.
 * Prevents the program from crashing due to wrong input types.
 * 
 * OOP Concept: Encapsulation — validation logic is kept in one place.
 * Exception Handling: Uses try-catch to catch InputMismatchException.
 */
public class InputValidator {

    private Scanner scanner;

    public InputValidator() {
        this.scanner = new Scanner(System.in);
    }

    /**
     * Reads a non-empty String from the user.
     * Keeps asking until the user types something.
     */
    public String readString(String prompt) {
        String input = "";
        while (input.trim().isEmpty()) {
            System.out.print(prompt);
            input = scanner.nextLine();
            if (input.trim().isEmpty()) {
                System.out.println("  [!] Input cannot be empty. Please try again.");
            }
        }
        return input.trim();
    }

    /**
     * Reads an integer within a specified range [min, max].
     * Rejects non-numeric input and out-of-range values.
     */
    public int readInt(String prompt, int min, int max) {
        int value = Integer.MIN_VALUE;
        while (value < min || value > max) {
            System.out.print(prompt);
            String line = scanner.nextLine();
            try {
                value = Integer.parseInt(line.trim());
                if (value < min || value > max) {
                    System.out.println("  [!] Please enter a number between "
                            + min + " and " + max + ".");
                    value = Integer.MIN_VALUE;
                }
            } catch (NumberFormatException e) {
                System.out.println("  [!] Invalid input. Please enter a whole number.");
            }
        }
        return value;
    }

    /**
     * Reads a double within a specified range [min, max].
     * Used for marks (0.0 – 100.0).
     */
    public double readDouble(String prompt, double min, double max) {
        double value = Double.MIN_VALUE;
        while (value < min || value > max) {
            System.out.print(prompt);
            String line = scanner.nextLine();
            try {
                value = Double.parseDouble(line.trim());
                if (value < min || value > max) {
                    System.out.println("  [!] Please enter a value between "
                            + min + " and " + max + ".");
                    value = Double.MIN_VALUE;
                }
            } catch (NumberFormatException e) {
                System.out.println("  [!] Invalid input. Please enter a number (e.g. 85.5).");
                value = Double.MIN_VALUE;
            }
        }
        return value;
    }

    /**
     * Reads a yes/no confirmation from the user.
     * Returns true for 'y' or 'yes', false otherwise.
     */
    public boolean readConfirmation(String prompt) {
        System.out.print(prompt + " (y/n): ");
        String answer = scanner.nextLine().trim().toLowerCase();
        return answer.equals("y") || answer.equals("yes");
    }

    // Call this when the program exits
    public void close() {
        scanner.close();
    }
}
