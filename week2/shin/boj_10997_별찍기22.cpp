#include <iostream>
#include <deque>
using namespace std;

deque<string> arr;

void go(){
    int sRow = arr[0].size();
    int sCol = arr.size();
    arr[0].insert(0, "* ");
    arr[0].append("**");
    string twoing = "";
    for(int i=0 ; i<sRow-2 ; i++){
        twoing.append(" ");
    }
    arr[1].append(twoing);
    for(int i=1 ; i<sCol ; i++){
        arr[i].insert(0, "* ");
        arr[i].append(" *");
    }

    string nextOne = "*  *";
    for(int i=0 ; i<sRow ; i ++){
        nextOne.insert(1, " ");
    }
    arr.push_back(nextOne);
    string nextTwo = "****";
    for(int i=0 ; i<sRow ; i ++){
        nextTwo.append("*");
    }
    arr.push_back(nextTwo);

    string beforeTwo = "* ";
    arr.push_front(beforeTwo);
    string beforeOne = "****";
    for(int i=0 ; i<sRow ; i++){
        beforeOne.append("*");
    }
    arr.push_front(beforeOne);
}
int main(){
    int n;
    scanf("%d", &n);
    if(n == 1) {
        printf("*");
    }
    else{
        arr.push_back("*****");
        arr.push_back("* ");
        arr.push_back("* ***");
        arr.push_back("* * *");
        arr.push_back("* * *");
        arr.push_back("*   *");
        arr.push_back("*****");
        for(int i=2 ; i<n ; i++){
            go();
        }
        for(int i=0 ; i<arr.size() ; i++){
            cout<<arr[i]<<endl;
        }
    }
}