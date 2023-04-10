### [silver 4] 1764: 듣보잡
https://www.acmicpc.net/problem/11652
</br></br>

#### 입력 & 출력
첫째 줄에 듣도 못한 사람, 보도 못한 사람의 수를 입력한다.</br>
첫째 줄에 입력된 수에 따라 각 사람의 이름을 입력한다. </br>
(듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.)</br></br>
듣보잡의 수와 그 명단을 사전순으로 출력한다.</br></br>

#### 문제 풀이 </br>

입력받은 듣도 못한 사람의 수와 보도 못한 사람의 수만큼 이름을 순서대로 입력받는다.</br>
문제에서 최종적으로 구하고 싶은 것은 듣보잡의 명단과 수이기 때문에 두가지의 값이 필요하다.</br>

위 두가지 값을 동시에 구하기 위해 Map을 이용해서 이름과 수를 동시에 구했다.</br>
하지만 May의 key 값은 중복될 경우 value 값이 update 되기 때문에 기존의 value 값을 얻어 1씩 증가하도록 설정했다.</br>
<details>
<summary>코드</summary>

```java
Map<String, Integer> map = new HashMap<String, Integer>();
for(int i=0; i<n+m; i++) {
			int val = 1;
			String str = br.readLine();
			if(map.containsKey(str)) {
				val = map.get(str);
				val++;
			}
			map.put(str, val);
		}
```

</details>

</br>
사전순으로 출력하라는 조건이 있기 때문에 key 값(이름)이 PriorityQueue에 key 값을 넣어 오름차순 정렬을 했다.</br>
이때 각 항목(듣도 못한 사람, 보도 못한 사람)에는 중복된 이름이 없기 때문에 이름이 다시 한번 나오면 듣도 보도</br>
못한 사람이라 간주하여 key 값이 2 이상인 사람만 PriorityQueue에 추가했다.</br></br>
<details>
<summary>코드</summary>

```java
PriorityQueue<String> pq = new PriorityQueue<String>();
for(String key : map.keySet()) {
			if(map.get(key)>1) {
				pq.add(key);
			}
		}
```

</details>

</br>
그 후 PriorityQueue에 담겨있는 듣보잡의 명단 수와 사람의 이름을 순서대로 출렸했다.</br>
</br>
<details>
<summary>코드</summary>

```java
bw.write(String.valueOf(pq.size())+"\n");
		while(!pq.isEmpty()) {
			bw.write(pq.poll()+"\n");
		}
		
		bw.flush();
```

</details>

</br>

<details>
<summary>전체 코드</summary>

```java
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
```
</details>
