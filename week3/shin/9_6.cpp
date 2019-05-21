#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> v[51];
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0 ; i<n ; i++){
        string temp;
        cin>>temp;

        int index = temp.length();
        v[index].push_back(temp);
    }
    for(int i=1 ; i<=50 ; i++) {
        if(v[i].size() != 0) {
            sort(v[i].begin(), v[i].end());
            auto a = v[i].begin();
            while (a != v[i].end()) {
                if ((a != v[i].begin())&&(*a == *(a - 1))) {
                    a++;
                    continue;
                }
                cout << *a << endl;
                a++;
            }
        }
    }

}