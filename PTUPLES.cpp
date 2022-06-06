/*

*  Author : Ayushman Chahar   #
*  About  : IT Sophomore      #
*  Insti  : VIT, Vellore      #

*/

#pragma GCC optimize("Ofast")  
#pragma GCC target("avx,avx2,fma") 
#pragma GCC optimization ("unroll-loops")

#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define mod 998244353

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T, typename U> inline void amin(T &x, U y) {if(y < x) x = y;}
template<typename T, typename U> inline void amax(T &x, U y) {if(x < y) x = y;}

const int N = 1e6 + 1;
vector<int> ans;

int isPrime(int n) {
    if(n <= 1) return 0;
    if(n <= 3) return 1;
    if(n % 2 == 0 || n % 3 == 0) return 0;
    for(int i = 5; i <= sqrt(n); i += 6) {
        if(n % i == 0 || (n % (i + 2)) == 0) return 0;
    }
    return 1;
}

void solve() {
    int n;
    cin >> n;
    cout << ans[n] << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    for(int i = 0; i <= 2; i++) ans.push_back(0);
    int start = 0;
    for(int i = 3; i <= N + 1; i++) {
        if(isPrime(i - 2) && isPrime(i)) start++;
        ans.push_back(start);
    }
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}

