import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
예제 출력 1
3
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int decimal[] = new int[1001];
        decimal[1] = 1;

        for(int i = 2 ; i <= 1000 ; i++)
        {
            int multiples = 2;
            while(i*multiples <= 1000){
                decimal[i*multiples] = 1;
                multiples++;
            }
        }
        

        int decimalCount = 0;
        while(st.hasMoreTokens()){
            int number = Integer.parseInt(st.nextToken());
            if(decimal[number] == 0)
                decimalCount++;
        }
        System.out.println(decimalCount);

    }
}
