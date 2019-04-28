import java.util.Scanner;

//높이 n [3*2^k (k = 1~10)] > 최대 : 3072
//삼각형 밑변 2*n-1 > 최대 : 6144

public class Q11 {

	final static int BASESIZE = 3; // 작은 삼각형 사이즈
	static char[][] board; // *을 그릴판

	public static void main(String[] args) {
	// 입력
		Scanner input = new Scanner(System.in);
		int n = input.nextInt(); // 3*2^k (k = 1~10)

		board = new char[n][2 * n - 1];
		for (int i = 0; i < board.length; i++) { // 모두 공백으로 초기화 / 마지막부분만 \n
			for (int j = 0; j < board[i].length; j++) {
				board[i][j] = j == board[i].length - 1 ? '\n' : ' ';
			}
		}

	// 처리
		recursiveDraw(n, 0, n - 1); // 가장 위 꼭지점기준 x,y좌표로 그리기

	// 출력
		print();
	}
	
	//처리함수 - 재귀
	public static void recursiveDraw(int n, int x, int y) {
		if (n == BASESIZE) { // 가장 작은 (base) 삼각형일경우
			board[x][y] = '*'; // x,y좌표 == 삼각형 위 꼭지점을 기준으로 base삼각형 그리기
			board[x + 1][y - 1] = '*';
			board[x + 1][y + 1] = '*';
			for (int i = 0; i < 5; i++) {
				board[x + 2][y - 2 + i] = '*';
			}
			return;
		}

		recursiveDraw(n / 2, x, y);
		recursiveDraw(n / 2, x + n / 2, y - n / 2); // 위에서 그림 x,y축기준으로 좌표구하기
		recursiveDraw(n / 2, x + n / 2, y + n / 2); // //위에서 그림 x,y축기준으로 좌표구하기

	}
	
	//출력함수
	public static void print() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				System.out.print(board[i][j]);
			}
		}
	}
}