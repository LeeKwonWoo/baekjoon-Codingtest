package codingTest;
import java.util.Scanner;
/*
 * 먼저 wb찾고 /그 다음 8x8 위치 찾고 거기서 8x8칸을 만들고 /변환 개수 찾음
 */
public class Main1018 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();
		String[] wb = new String[n];
		int cnt = 0;
		
		for (int h = 0; h < n; h++) {
			wb[h] = scan.next();
			if (wb[h].contains("W") && wb[h].contains("B")) {
				int idxW = wb[h].indexOf("W");
				int idxB = wb[h].indexOf("B");
				if (idxW > idxB) {
					
				} else {
					
				}
			}
			for (int w = 0; w < m; w++) {
				if (w+1 >= m) {
					break;
				}
				if (wb[h].charAt(w) == wb[h].charAt(w+1)) {
					cnt++;
					w++;
				}
			}
		}
		System.out.println(cnt);
	}
}