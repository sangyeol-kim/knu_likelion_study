import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack stack = new Stack();
		Queue result = new LinkedList();
		String line = null;
		
		int num = input.nextInt();
		input.nextLine();
		for(int i = 0 ; i < num ; i++)
		{
			line = input.nextLine();
			if(line.equals("pop"))
			{
				if(stack.isEmpty())
					result.add(-1);
				else
				{
					result.add(stack.pop());
				}
			}
			else if(line.equals("top"))
			{
				if(stack.isEmpty())
					result.add(-1);
				else
					result.add(stack.peek());
			}
			else if(line.equals("empty"))
			{
				if(stack.empty())
					result.add(1);
				else
					result.add(0);
			}
			else if(line.equals("size"))
			{
				result.add(stack.size());
			}
			else
			{
				stack.push(line.substring(5));
			}
		}
		while(result.isEmpty() != true)
			System.out.println(result.poll());

	}

}
