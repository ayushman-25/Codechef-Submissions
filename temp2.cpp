/*

*  Author : Ayushman Chahar  #
*  About  : IT Junior        #
*  Insti  : VIT, Vellore     #

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

vector<string> ans = {"3", "4", "9", "16", "27", "64", "81", "256", "243", "1024", "729", "4096", "2187", "16384", "6561", "65536", "19683", "262144", "59049", "1048576", "177147", "4194304", "531441", "16777216", "1594323", "67108864", "4782969", "268435456", "14348907", "1073741824", "43046721", "4294967296", "129140163", "17179869184", "387420489", "68719476736", "1162261467", "274877906944", "3486784401", "1099511627776", "10460353203", "4398046511104", "31381059609", "17592186044416", "94143178827", "70368744177664", "282429536481", "281474976710656", "847288609443", "1125899906842624", "2541865828329", "4503599627370496", "7625597484987", "18014398509481984", "22876792454961", "72057594037927936", "68630377364883", "288230376151711744", "205891132094649", "1152921504606846976", "617673396283947", "4611686018427387904", "1853020188851841", "18446744073709551616", "5559060566555523", "73786976294838206464", "16677181699666569", "295147905179352825856", "50031545098999707"
};

void solve() {
    ll n;
    cin >> n;
    cout << ans[n - 1] << "\n";

}

int main() {
// #ifndef ONLINE_JUDGE
//     freopen("in.txt", "r", stdin);
//     freopen("out.txt", "w", stdout);
//     freopen("error.txt", "w", stderr);
// #endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    // cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    return 0;
}