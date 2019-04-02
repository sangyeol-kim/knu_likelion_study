package d0329;

public class Algorithm1 {

	public static void main(String[] args) {
		int input = 6;
		int count = 0;

		for (int i = 0; i <= input - 3; i++) {
			for (int j = i + 1; j <= input - 2; j++) {
				for (int z = j + 1; z <= input - 1; z++) {
					for (int x = z + 1; x <= input; x++) {
						System.out.printf("%d %d %d %d\n", i, j, z, x);
						count++;
					}

				}

			}

		}
		System.out.println("ÃÑ°³¼ö : " + count);

	}

}
