import java.util.Scanner;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a=0;
		int b=0;
		int testCase = input.nextInt();
		int aa[] = new int[testCase];
		for(int i = 0 ; i < testCase ; i ++) {
			a = input.nextInt();
			b = input.nextInt();
			aa[i] = b-a;
		}
		int bb = 0;
		while(bb<testCase)
		{
		int num = aa[bb];
		int count = 0;
		int n = 1;
		if(num == 1)
		{
			System.out.println(1);
			bb++;
			continue;
		}
		
		while(true) { 
			count++;
			if(num - n <= 0)
			{
				break;
			}
			else
			{
				num -= n;
			}
			count++;
			if(num - n <= 0)
			{
				break;
			}
			else
			{
				num -= n;
			}
			n++;
		}
		System.out.println(count);
		bb++;
		}
	}

}
