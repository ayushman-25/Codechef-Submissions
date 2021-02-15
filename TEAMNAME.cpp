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

struct custom_hash { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const
    { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
};

string alp = "abcdefghijklmnopqrstuvwxyz";

void solve() {
    int n, ans = 0;
    cin >> n;
    vector<string> arr(n); for(string& inp: arr) cin >> inp;
    unordered_map<string, int> funny;
    funny.reserve(32768); funny.max_load_factor(0.25);
    for(int i = 0; i < n; i++) funny[arr[i]] = (i + 1); 
    vector<string> pre_cut;
    for(string s: arr) pre_cut.emplace_back(s.substr(1, (int) s.size()));
    vector<vector<string>> tc;
    tc.resize(26);
    for(int i = 0; i < 26; i++) {
        for(string s: pre_cut) tc[i].emplace_back(alp[i] + s);
    }
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            if(!funny[tc[arr[j][0] - 'a'][i]] && !funny[tc[arr[i][0] - 'a'][j]]) {
                ans += 2;
            }
        }
    }
    cout << ans << "\n";

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}