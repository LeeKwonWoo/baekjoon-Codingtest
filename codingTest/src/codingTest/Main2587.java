package codingTest;
import java.util.Scanner;
public class Main2587 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n1 = scan.nextInt();
		int n2 = scan.nextInt();
		int n3 = scan.nextInt();
		int n4 = scan.nextInt();
		int n5 = scan.nextInt();
		int[] arr = {n1, n2, n3, n4, n5};
		int avg = (n1+n2+n3+n4+n5)/5;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (arr[i] < arr[j]) {
					int tmp = 0;
					tmp = arr[i];
					arr[i] = arr[j];
					arr[j] = tmp;
				}
			}
		}
		System.out.println(avg);
		System.out.println(arr[2]);
	}

}
//int[] sorted = new int[5];
//void merge(int[] arr, int left, int mid, int right) {
//	int i, j, k, l;
//	i = left;
//	j = mid+1;
//	k = left;
//	while (i <= mid && j <= right) {
//		if (arr[i]<=arr[j]) {
//			sorted[k++] = arr[i++];
//		} else {
//			sorted[k++] = arr[j++];
//		}
//	}
//	if (i > mid) {
//		for (l = j; l < right; l++) {
//			sorted[k++] = arr[l];
//		}
//	} else {
//		for (l = j; l < mid; l++) {
//			sorted[k++] = arr[l];
//		}
//	}
//	for(l = left; l <= right; l++) {
//		arr[l] = sorted[l];
//	}
//}
//
//void merge_sort(int[] arr, int left, int right) {
//	int mid;
//	if (left < right) {
//		mid = (left+right)/2;
//		merge_sort(arr, left, mid);
//		merge_sort(arr, mid+1, right);
//		merge(arr,left, mid, right);
//	}
//}