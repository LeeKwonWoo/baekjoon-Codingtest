package codingTest;
import java.util.Scanner;
/*
 * 먼저 wb찾고 /그다음 8x8 찾고 /변환 개수 찾음
 */
public class Main1018 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();
		String[] wb = new String[n];
		int cnt = 0;
		for (int i = 0; i < 8; i++) {
			wb[i] = scan.next();
			if (wb[i].contains("W") && wb[i].contains("B")) {
				int idxW = wb[i].indexOf("W");
				int idxB = wb[i].indexOf("B");
				if (idxW > idxB) {
					
				} else {
					
				}
			}
			for (int j = 0; j < 8; j++) {
				if (j+1 >= m) {
					break;
				}
				if (wb[i].charAt(j) == wb[i].charAt(j+1)) {
					cnt++;
					j++;
				}
			}
		}
		System.out.println(cnt);
	}
}
