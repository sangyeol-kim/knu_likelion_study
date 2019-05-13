/*'수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다
 */

#include <iostream>
#include <vector>
#include <memory.h>
#include <algorithm>
#include <cmath>

using namespace std;



vector<int> v, result;

int arr[8001];
int main(){
    memset(arr, 0, sizeof(arr));
    double avg = 0;
    int n, temp;
    scanf("%d", &n);
    for(int i=0 ; i<n ; i++){
        scanf("%d", &temp);
        v.push_back(temp);
        arr[temp+4000]++;
        avg+=temp;
    }
    sort(v.begin(), v.end());

    avg /= n;
    avg = floor(avg+0.5);
    int mid = v[(n-1)/2];
    int freq = 0, freqIndex;
    for(int i=0 ; i<8001 ; i++){
        if(freq < arr[i]) {
            result.clear();
            result.push_back(i-4000);
            freq = arr[i];
        }
        else if(freq == arr[i]){
            result.push_back(i-4000);
        }
    }


    if(result.size() >= 2)
        freqIndex = result[1];
    else
        freqIndex = result[0];

    int range = v[n-1] - v[0];


    printf("%d\n%d\n%d\n%d\n", (int)avg, mid, freqIndex, abs(range));

}