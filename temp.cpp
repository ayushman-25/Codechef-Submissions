#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int n, i = 0, ans = 0;
    cin >> n;
    vector<int> a1(n), a2(n);
    for(int &i: a1) cin >> i;
    for(int &i: a2) cin >> i;
    while(a1 != a2) {
        if(a1[i] != a2[i]) {
            swap(a1[i], a1[find(a1.begin(), a1.end(), a2[i]) - a1.begin()]); 
            ans++;
        }
        else i++;
    } 
    cout << ans;
    return 0;
}