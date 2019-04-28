# include <stdio.h>

//높이 n [3*2^k (k = 1~10)] > 최대 : 3072
//삼각형 밑변 2*n-1 > 최대 : 6144

void draw(int n, int x, int y);

char board[3072][6144];
const int BASESIZE = 3;

int main(void){
	int n, i, j;
	
	scanf_s("%d", &n); //입력

	// 배열 초기화

	for (i = 0; i < n; i++) {
		for (j = 0; j < 2 * n; j++) {
			board[i][j] = j == 2 * n - 1 ? '\n' : ' '; //// 모두 공백으로 초기화 / 마지막부분만 \n
		}
	}

	draw(n, 0, n - 1); // 가장 위 꼭지점기준 x,y좌표로 그리기

	// 배열 출력
	for (i = 0; i < n; i++) {
		for (j = 0; j < 2 * n; j++) {
			printf("%c", board[i][j]);
		}
	}
	
	return 0;
}

void draw(int n, int x, int y)
{
	if (n == BASESIZE) //가장작은 (base) 삼각형일 경우
	{ // x,y좌표 == 삼각형 위 꼭지점을 기준으로 base삼각형 그리기
		board[x][y] = '*';
		board[x + 1][y - 1] = '*';
		board[x + 1][y + 1] = '*';
		board[x + 2][y - 2] = '*';
		board[x + 2][y - 1] = '*';
		board[x + 2][y + 0] = '*';
		board[x + 2][y + 1] = '*';
		board[x + 2][y + 2] = '*';
		return;
	}
	
	draw(n / 2, x, y);
	draw(n / 2, x + n / 2, y - n / 2); // 위에서 그림 x,y축기준으로 좌표구하기
	draw(n / 2, x + n / 2, y + n / 2); // //위에서 그림 x,y축기준으로 좌표구하기
	
}