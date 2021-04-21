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

static struct IO {
    char tmp[1 << 10];

    // fast input routines
    char cur;

//#define nextChar() (cur = getc_unlocked(stdin))
//#define peekChar() (cur)
    inline char nextChar() { return cur = getc_unlocked(stdin); }
    inline char peekChar() { return cur; }

    inline operator bool() { return peekChar(); }
    inline static bool isBlank(char c) { return (c < '-' && c); }
    inline bool skipBlanks() { while (isBlank(nextChar())); return peekChar() != 0; }

    inline IO& operator >> (char & c) { c = nextChar(); return *this; }

    inline IO& operator >> (char * buf) {
        if (skipBlanks()) {
            if (peekChar()) {
                *(buf++) = peekChar();
                while (!isBlank(nextChar())) *(buf++) = peekChar();
            } *(buf++) = 0; } return *this; }

    inline IO& operator >> (string & s) {
        if (skipBlanks()) {    s.clear(); s += peekChar();
            while (!isBlank(nextChar())) s += peekChar(); }
        return *this; }

    inline IO& operator >> (double & d) { if ((*this) >> tmp) sscanf(tmp, "%lf", &d); return *this;    }

#define defineInFor(intType) \
    inline IO& operator >>(intType & n) { \
        if (skipBlanks()) { \
            int sign = +1; \
            if (peekChar() == '-') { \
                sign = -1; \
                n = nextChar() - '0'; \
            } else \
                n = peekChar() - '0'; \
            while (!isBlank(nextChar())) { \
                n += n + (n << 3) + peekChar() - 48; \
            } \
            n *= sign; \
        } \
        return *this; \
    }

defineInFor(int)
defineInFor(unsigned int)
defineInFor(long long)
defineInFor(unsigned long long)

    // fast output routines

//#define putChar(c) putc_unlocked((c), stdout)
    inline void putChar(char c) { putc_unlocked(c, stdout); }
    inline IO& operator << (char c) { putChar(c); return *this; }
    inline IO& operator << (const char * s) { while (*s) putChar(*s++); return *this; }

    inline IO& operator << (const string & s) { for (int i = 0; i < (int)s.size(); ++i) putChar(s[i]); return *this; }

    char * toString(double d) { sprintf(tmp, "c", d, '\0'); return tmp; }
    inline IO& operator << (double d) { return (*this) << toString(d); }


#define defineOutFor(intType) \
    inline char * toString(intType n) { \
        char * p = (tmp + 30); \
        if (n) { \
            bool isNeg = 0; \
            if (n < 0) isNeg = 1, n = -n; \
            while (n) \
                *--p = (n % 10) + '0', n /= 10; \
            if (isNeg) *--p = '-'; \
        } else *--p = '0'; \
        return p; \
    } \
    inline IO& operator << (intType n) { return (*this) << toString(n); }

defineOutFor(int)
defineOutFor(unsigned int)
defineOutFor(long long)
defineOutFor(unsigned long long)

#define endl ('\n')
#define cout __io__
#define cin __io__
} __io__;

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<ll> single_1(n);
    for(ll &i: single_1) cin >> i;
    vector<vector<ll>> cons_1;
    cons_1.resize(m);
    for(int i = 0; i < m; i++) {
        ll a, b, c;
        cin >> a >> b >> c;
        cons_1[i].emplace_back(a);
        cons_1[i].emplace_back(b);
        cons_1[i].emplace_back(c);
    }
    vector<ll> ans;
    for(int i = 0; i < (1 << n); i++) {
        ll score = 0;
        string checkbin;
        if(i == 0) {
            for(int j = 0; j < n; j++) {
                checkbin.push_back('0');
            }
        } else {
            int z = i;
            while(z > 0) {
                checkbin.push_back(z & 1 ? '1' : '0');
                z /= 2;
            }
            for(int j = 0; j < n - (int)log2(i) - 1; j++) {
                checkbin.push_back('0');
            }
        }
        reverse(checkbin.begin(), checkbin.end());
        vector<int> prefix = {checkbin[0] - '0'};
        for(int j = 1; j < n; j++) {
            prefix.emplace_back((checkbin[j] - '0') + prefix.back());
        }
        for(int j = 0; j < n; j++) {
            if(checkbin[j] == '1') {
                score += single_1[j];
            }
        }
        for(auto m: cons_1) {
            if(prefix[m[1] - 1] - (m[0] == 1 ? 0 : prefix[m[0] - 2]) == m[1] - m[0] + 1) {
                score += m[2];
            }
        }
        ans.emplace_back(score);
    }
    sort(ans.begin(), ans.end(), greater<ll>());
    for(int i = 0; i < k; i++) {
        cout << ans[i] << " \n"[i + 1 == k];
    }
}

int main() {
// #ifndef ONLINE_JUDGE
//  freopen("in.txt", "r", stdin);
//  freopen("out1.txt", "w", stdout);
// #endif
    // ios_base::sync_with_stdio(false);
    // cin.tie(nullptr); cout.tie(nullptr);
    int t = 1, casee = 1;
    cin >> t;
    while(t--) {
        // cout << "Case #" << casee++ << ": ";
        solve();
    }
    return 0;
}