import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> stack = new Stack<Integer>();
		StringBuilder result = new StringBuilder();
		
		
		int num = Integer.parseInt(br.readLine());
		
		int str[] =  new int[num];
		
		for(int i = 0 ; i < num ; i ++)
		{
			str[i] = Integer.parseInt(br.readLine());	
		}
		int index = 0;
		int top = 1;
		int curr;
		
		
		while(index < str.length)
		{
			curr = str[index];
			if(stack.isEmpty()) {
				result.append("+\n");
				stack.push(top);
				top++;
			}
			else if(stack.peek() < curr)
			{
				result.append("+\n");
				stack.push(top);
				top++;
			}
			else if(stack.peek() ==  curr)
			{
				result.append("-\n");
				stack.pop();
				index++;
			}
			else
			{
				System.out.println("NO");
				System.exit(0);
			}
		}
		System.out.println(result);
	}
}
