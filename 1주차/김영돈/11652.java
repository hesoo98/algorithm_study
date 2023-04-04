// [Silver4 - 11652번: 카드]

import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String args[]){
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		HashMap<Long, Integer> map = new HashMap<Long, Integer>();
		
		for(int i=0; i<t; i++) {
			int val = 1;
			long num = sc.nextLong();
			if(map.containsKey(num)) {
				val = map.get(num);
				val++;
			}
			map.put(num, val);
		}
		
		long maxKey = 0;
		long maxValue = 0;
		for(long i : map.keySet()) {
			if(maxValue < map.get(i)) {
				maxValue = map.get(i);
				maxKey = i;
			}
			if(maxValue == map.get(i)) {
				maxKey = maxKey > i? i : maxKey;
			}
		}
		System.out.println(maxKey);
	}
}
