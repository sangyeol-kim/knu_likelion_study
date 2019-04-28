#include <iostream>
#include <vector>

using namespace std;
/*
                       *
                      * *
                     *****
                    *     *
                   * *   * *
                  ***** *****
                 *           *
                * *         * *
               *****       *****
              *     *     *     *
             * *   * *   * *   * *
            ***** ***** ***** *****
           *                       *
          * *                     * *
         *****                   *****
        *     *                 *     *
       * *   * *               * *   * *
      ***** *****             ***** *****
     *           *           *           *
    * *         * *         * *         * *
   *****       *****       *****       *****
  *     *     *     *     *     *     *     *
 * *   * *   * *   * *   * *   * *   * *   * *
***** ***** ***** ***** ***** ***** ***** *****
 */
vector<string> arr;
void go(int mid, int end){
    for(int i = mid ; i<=end ; i++){
        arr.push_back(arr[i-(mid-1)] + " " + arr[i-(mid-1)]);
    }
    string operand = "";
    for(int i=1 ; i<mid ; i++){
        operand.append(" ");
    }
    for(int i=1 ; i<mid ; i++){
        arr[i].insert(0, operand);
        arr[i].append(operand);
    }


}
int main(){
    arr.push_back("");
    arr.push_back("  *  ");
    arr.push_back(" * * ");
    arr.push_back("*****");
    int n;
    scanf("%d", &n);
    int k=3;
    int mid;
    while(k<n){
        mid = k+1;
        k*=2;
        go(mid, k);
    }

    for(int i=1 ; i<=n ; i++){
        cout<<arr[i]<<endl;
    }
}