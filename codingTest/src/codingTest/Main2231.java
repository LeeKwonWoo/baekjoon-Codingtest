package codingTest;
import java.util.Scanner;

public class Main2231 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int sum = 0, result = 0, mid = 0;
		for (int i = 1; i < 10; i++) {
			for (int j = 1; j < 10; j++) {
				for (int k = 1; k < 10; k++) {
					sum = i + k + j;
					String s1 = Integer.toString(i);
					String s2 = Integer.toString(j);
					String s3 = Integer.toString(k);
					String m = s1 + s2 + s3;
					mid = Integer.valueOf(m);
					result = n - mid;
					if (result == sum) {
						System.out.print(mid);
					}
				}
			}
			if (i==9) {
				mid = 0;
				System.out.println(mid);
			}
		}
	}
}
