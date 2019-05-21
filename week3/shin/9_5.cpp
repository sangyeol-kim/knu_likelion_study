#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
/*


 */
vector<int> v;
int main(){
    int n;
    scanf("%d", &n);
    while(n > 0){
        int temp = n%10;
        n /= 10;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());

    auto i = v. rbegin();
    while( i != v.rend()){
        printf("%d", *i);
        i++;
    }
    printf("\n");
}