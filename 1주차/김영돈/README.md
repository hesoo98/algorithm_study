### [silver 4] 11652: 카드 </br></br>

#### 입력 & 출력
첫째 줄 카드의 개수가 주어지고 둘째 줄부터 카드의 개수만큼 카드에 적혀있는 정수를 입력한다.</br>
입력 후 카드에 적혀있는 수 중 가장 많은 수를 출력하는 문제이다. </br></br>

#### 문제 풀이 </br>

문제를 풀기 위해 구해야할 조건은 두 가지가 있다.</br>

1. 카드 적혀있는 번호</br>
2. 가지고 있는 각 카드 번호의 개수</br>
</br>
위 두 가지 항목을 동시에 구하기 위해 HashMap을 이용했고 1번은 key값, 2번은 value값으로 넣었다.</br>
초기 HashMap 생성시 key값은 value값과 다르게 변수 타입을 Long으로 설정했는데 </br>
이는 문제의 '적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다' 조건 때문에 Integer 값으로</br>
값을 넣을시 Integer의 범위를 넘기 때문이다.(런타임 에러 (InputMismatch) 발생)</br>
</br>

```java
HashMap<Long, Integer> map = new HashMap<Long, Integer>();
```
</br></br>
HashMap 생성을 하고 나면 key값과 value값을 넣는데 입력받은 카드 번호가 이미 있을 경우</br>
즉, map 안에 같은 key값이 존재할 경우 value 값을 1씩 증가시켰다. </br>
</br>
```java
for(int i=0; i<t; i++) {
		int val = 1;
		long num = sc.nextLong();
		if(map.containsKey(num)) {
				val = map.get(num);
		    val++;
	  }
		map.put(num, val);
}
```
</br></br>
그 후 map의 value 값을 조회하면서 가장 큰 값을 구하는데</br>
value 값이 같은 경우(가장 많이 가지고 있는 정수가 여러 가지라면) 가장 작은 것을 출력을 하기 위해</br>
조건문을 통해 key값 비교 후 작은 값으로 대입했다. </br>
</br>
```java
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
```
</br></br>
#### 최종 답안 </br>
```java
public class Main {
	public static void main(String args[]) throws NumberFormatException, IOException {
		
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
```
