import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		
		LinkedList list = new LinkedList();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testOfCase = Integer.parseInt(br.readLine());
		int number[] = new int[testOfCase];
		int temp = 0;
		for(int i = 0 ; i < testOfCase ; i++)
		{
			temp = Integer.parseInt(br.readLine());
			number[i] = temp;
		}
		for(int j = number.length - 2 ; j  >= 0 ; j--)
		{
			int index = j;
			while(index <= number.length -2)
			{
				if(number[index+1] < number[index])
				{
					temp = number[index];
					number[index] = number[index+1];
					number[index+1] = temp;
					index++;
				}
				else
					break;
			}
		}
		for(int k = 0 ; k < number.length ; k++)
		{
			System.out.println(number[k]);
		}
	}

}
