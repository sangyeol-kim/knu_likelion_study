#include <iostream>

using namespace std;

pair<int, int> solve(int n){
    n -= 1;
    int num = 1;
    while(n - num >= 0){
        n -= num;
        num++;
    }
    if(num % 2 == 0)
        return {1 + n , num - n};
    else
        return {num - n, 1 + n};
}
int main(){
    int n;
    scanf("%d", &n);
    pair<int, int> result = solve(n);
    printf("%d/%d", result.first, result.second);
}