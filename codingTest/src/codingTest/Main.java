package codingTest;
//import java.io.BufferedReader;
//import java.io.InputStreamReader;

import java.util.Scanner;

public class Main {

	private int blackJack(int N, int M, int[] m) {
		int result = 0;
		for (int i = 0; i < N-2; i++) {
			for (int j = i+1; j < N-1; j++) {
				for (int k = j+1; k < N; k++) {
					int sum = m[i] + m[j] + m[k];
					if (sum <= M && result < sum) {
						result = sum;
					}
				}
			}
		}
		return result;
	}
	
	public static void main(String[] args) {
//		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
//		int n = Integer.parseInt(br.readLine());
//		int m = Integer.parseInt(br.readLine());
		Scanner scan = new Scanner(System.in);
		int N, M = 0;
		N = scan.nextInt();
		M = scan.nextInt();
		int[] m = new int[100];
		for (int i = 0; i<N; i++) {
			m[i] = scan.nextInt();
		}
		System.out.println(new Main().blackJack(N, M, m));
		scan.close();
    }
}
