import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String nums = br.readLine();
		String[] numss = nums.split(" ");
		
		int n = Integer.parseInt(numss[0]);
		int m = Integer.parseInt(numss[1]);
		
		Map<String, Integer> map = new HashMap<String, Integer>();
		PriorityQueue<String> pq = new PriorityQueue<String>();
		
		for(int i=0; i<n+m; i++) {
			int val = 1;
			String str = br.readLine();
			if(map.containsKey(str)) {
				val = map.get(str);
				val++;
			}
			map.put(str, val);
		}
		
		for(String key : map.keySet()) {
			if(map.get(key)>1) {
				pq.add(key);
			}
		}
		
		bw.write(String.valueOf(pq.size())+"\n");
		while(!pq.isEmpty()) {
			bw.write(pq.poll()+"\n");
		}
		
		bw.flush();
	}
}
