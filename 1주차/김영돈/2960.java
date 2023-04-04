// [silver4 - 2960번: 에라토스테네스의 체]

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		List<Integer> list = new ArrayList<Integer>();
		
		for(int i=0; i<=n; i++) {
			list.add(i);
		}
		
		int cnt = 0;
		for(int i=2; i<=n; i++) {
			for(int j=i; j<=n; j=j+i) {
				if(list.get(j)==0) {
					continue;
				}
				list.set(j, 0);
				cnt++;
				if(cnt==k) {
					System.out.println(j);
					break;
				}
			}
		}
	}
}
