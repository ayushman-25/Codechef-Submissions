#include<bits/stdc++.h>
using namespace std;

int main() {
    int n1, n2, i;
    cin >> n1 >> n2;
    string sn1 = to_string(n1), sn2 = to_string(n2);
    int m = sn1.size(), n = sn2.size();
    int mn = min(m, n);
    vector<string> ans(4);
    for(i = 0; i < mn; i++) {
        ans[0] += sn1[i]; ans[0] += sn2[i];
        ans[1] += sn2[i]; ans[1] += sn1[i];
        ans[2] += sn1[mn-i-1]; ans[2] += sn2[mn-i-1];
        ans[3] += sn2[mn-i-1]; ans[3] += sn1[mn-i-1];
    }
    if(m < n) {
        ans[0] += sn2.substr(i+1);
        ans[1] += sn2.substr(i+1);
        reverse(sn2.begin(), sn2.end());
        ans[3] += sn2.substr(i+1);
        ans[4] += sn2.substr(i+1);
    } else if(m > n) {
        ans[0] += sn1.substr(i+1);
        ans[1] += sn1.substr(i+1);
        reverse(sn1.begin(), sn1.end());
        ans[3] += sn1.substr(i+1);
        ans[4] += sn1.substr(i+1);
    }
    int maxans = 0;
    for(string i: ans) {
        maxans = max(maxans, stoi(i));
    }
    cout << maxans;
}
