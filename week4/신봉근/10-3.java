import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1
3 16
예제 출력 1
3
5
7
11
13
*/
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int decimal[] = new int[1000001];
        decimal[1] = 1;

        for(int i = 2 ; i <= 1000000 ; i++)
        {
            int multiples = 2;
            while(i*multiples <= 1000000){
                decimal[i*multiples] = 1;
                multiples++;
            }
        }


        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        for(int i = start ; i <= end ; i ++){
            if(decimal[i] == 0)
                System.out.println(i);
        }


    }
}
