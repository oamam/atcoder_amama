import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int result = 0;
    for (int i = 0; i < s.length(); i++) {
      if (Character.getNumericValue(s.charAt(i)) == 1) {
        result += 1;
      }
    }
    System.out.println(result);
  }
}
