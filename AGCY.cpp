/*

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

*/

//Directive, Optimisation Flags, Targets
#pragma GCC optimize("Ofast")  
#pragma GCC target("avx,avx2,fma") 
#pragma GCC optimization ("unroll-loops")

//Header Files
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
//#include <boost/multiprecision/cpp_int.hpp>

//using boost :: multiprecision :: cpp_int;
using namespace std;
using std :: string;

//Pre-Processors and TypeDef constants
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define read(type) readInt<type>()
#define McQueen ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr)
const double pi = acos(-1.0);
typedef long long int lli;
typedef unsigned long long int ulli;
typedef long int li;
typedef unsigned long int uli;


//Basic min and max
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

/**********************************************/

// Fast I/O Methods
template <typename T> inline void write(T x)
{
    int i = 20;
    char buf[21];
    // buf[10] = 0;
    buf[20] = '\n';
    do
    {
        buf[--i] = x % 10 + '0';
        x /= 10;
    }while(x);
    do
    {
        putchar(buf[i]);
    } while (buf[i++] != '\n');
}

template <typename T> inline T readInt()
{
    T n = 0,s = 1;
    char p = getchar();
    if(p == '-')
        s =- 1;
    while((p < '0' | p > '9') && p != EOF && p != '-')
        p = getchar();
    if(p == '-')
        s =- 1,p = getchar();
    while(p >= '0' && p <= '9') {
        n = (n << 3) + (n << 1) + (p - '0');
        p = getchar();
    }

    return n * s;
}

// RISKY!! (Don't use if not necessary!)

// static struct IO {
//     char tmp[1 << 10];

//     // fast input routines
//     char cur;

// //#define nextChar() (cur = getc_unlocked(stdin))
// //#define peekChar() (cur)
//     inline char nextChar() { return cur = getc_unlocked(stdin); }
//     inline char peekChar() { return cur; }

//     inline operator bool() { return peekChar(); }
//     inline static bool isBlank(char c) { return (c < '-' && c); }
//     inline bool skipBlanks() { while (isBlank(nextChar())); return peekChar() != 0; }

//     inline IO& operator >> (char & c) { c = nextChar(); return *this; }

//     inline IO& operator >> (char * buf) {
//         if (skipBlanks()) {
//             if (peekChar()) {
//                 *(buf++) = peekChar();
//                 while (!isBlank(nextChar())) *(buf++) = peekChar();
//             } *(buf++) = 0; } return *this; }

//     inline IO& operator >> (string & s) {
//         if (skipBlanks()) {    s.clear(); s += peekChar();
//             while (!isBlank(nextChar())) s += peekChar(); }
//         return *this; }

//     inline IO& operator >> (double & d) { if ((*this) >> tmp) sscanf(tmp, "%lf", &d); return *this;    }

// #define defineInFor(intType) \
//     inline IO& operator >>(intType & n) { \
//         if (skipBlanks()) { \
//             int sign = +1; \
//             if (peekChar() == '-') { \
//                 sign = -1; \
//                 n = nextChar() - '0'; \
//             } else \
//                 n = peekChar() - '0'; \
//             while (!isBlank(nextChar())) { \
//                 n += n + (n << 3) + peekChar() - 48; \
//             } \
//             n *= sign; \
//         } \
//         return *this; \
//     }

// defineInFor(int)
// defineInFor(unsigned int)
// defineInFor(long long)
// defineInFor(unsigned long long)

//     // fast output routines

// //#define putChar(c) putc_unlocked((c), stdout)
//     inline void putChar(char c) { putc_unlocked(c, stdout); }
//     inline IO& operator << (char c) { putChar(c); return *this; }
//     inline IO& operator << (const char * s) { while (*s) putChar(*s++); return *this; }

//     inline IO& operator << (const string & s) { for (int i = 0; i < (int)s.size(); ++i) putChar(s[i]); return *this; }

//     char * toString(double d) { sprintf(tmp, "c", d, '\0'); return tmp; }
//     inline IO& operator << (double d) { return (*this) << toString(d); }


// #define defineOutFor(intType) \
//     inline char * toString(intType n) { \
//         char * p = (tmp + 30); \
//         if (n) { \
//             bool isNeg = 0; \
//             if (n < 0) isNeg = 1, n = -n; \
//             while (n) \
//                 *--p = (n % 10) + '0', n /= 10; \
//             if (isNeg) *--p = '-'; \
//         } else *--p = '0'; \
//         return p; \
//     } \
//     inline IO& operator << (intType n) { return (*this) << toString(n); }

// defineOutFor(int)
// defineOutFor(unsigned int)
// defineOutFor(long long)
// defineOutFor(unsigned long long)

// #define endl ('\n')
// #define cout __io__
// #define cin __io__
// } __io__;


/************************************/

// Let's Debug!
#define DEBUG

#ifdef DEBUG

    #define debug(args...)     (Debugger()) , args

    class Debugger
    {
        public:
        Debugger(const std::string& _separator = " - ") :
        first(true), separator(_separator){}

        template<typename ObjectType> Debugger& operator , (const ObjectType& v)
        {
            if(!first)
                std:cerr << separator;
            std::cerr << v;
            first = false;
            return *this;
        }
        ~Debugger() {  std:cerr << endl;}

        private:
        bool first;
        std::string separator;
    };

#else
    #define debug(args...)                  // Just strip off all debug tokens
#endif

/**************************************/


const int rt = 131072;
const int size = 255005;
int K[size];
int D[size];
int LK[size];
int LD[size];
int S[size];


int q(int l, int r, int n = 1, int a = 1, int b = rt) {
    if(a > r || b < l) return 0;
    if(a >= l && b <= r) return S[n];
    if(LK[n] != 0 or LD[n] != 0) {
        int sz = (b - a + 1) / 2;
        K[2 * n] += LK[n];
        K[2 * n + 1] += LK[n] + LD[n] * sz;
        D[2 * n] += LD[n];
        D[2 * n + 1] += LD[n];
        S[2 * n] += LK[n] * sz + LD[n] * sz * (sz - 1) / 2;
        S[2 * n + 1] += (LK[n] + LD[n] * sz) * sz + LD[n] * sz * (sz - 1) / 2;
        LK[2 * n] += LK[n];
        LK[2 * n + 1] += LK[n] + LD[n] * sz;
        LD[2 * n] += LD[n];
        LD[2 * n + 1] += LD[n];
        LK[n] = LD[n] = 0;
    }
    int mid = (a + b) / 2;
    return q(l, r, 2 * n, a, mid) + q(l, r, 2 * n + 1, mid + 1, b);
}


void u(int l, int r, int k, int d, int n = 1, int a = 1, int b = rt) {
    if(a >= l && b <= r) {
        K[n] += k;
        D[n] += d;
        LK[n] += k;
        LD[n] += d;
        S[n] += (k * (b - a + 1)) + d * (b - a + 1) * ((b - a + 1) - 1) / 2;
        return;
    } 
    if(LK[n] != 0 || LD[n] != 0) {
        int sz = (b - a + 1) / 2;
        K[2 * n] += LK[n];
        K[2 * n + 1] += LK[n] + LD[n] * sz;
        D[2 * n] += LD[n];
        D[2 * n + 1] += LD[n];
        S[2 * n] += LK[n] * sz + LD[n] * sz * (sz - 1) / 2;
        S[2 * n + 1] += (LK[n] + LD[n] * sz) * sz + LD[n] * sz * (sz - 1) / 2;
        LK[2 * n] += LK[n];
        LK[2 * n + 1] += LK[n] + LD[n] * sz;
        LD[2 * n] += LD[n];
        LD[2 * n + 1] += LD[n];
        LK[n] = LD[n] = 0;
    }
    int mid = (a + b) / 2; 
    if(l <= mid) u(l, min(mid, r), k, d, 2 * n, a, mid);
    if(r > mid) u(max(mid + 1, l), r, k + d * max(mid - l + 1, 0), d, 2 * n + 1, mid + 1, b);
    S[n] = S[2 * n] + S[2 * n + 1];
}


void reset() {
    for(int i = 0; i < size; i++) {
        K[i] = 0;
        D[i] = 0;
        LK[i] = 0;
        LD[i] = 0;
        S[i] = 0;
    }
}


//Initialize main()
int main() 
{
    //McQueen;
    int t;
    cin >> t;
    while(t--) {
        int n, qu;
        cin >> n >> qu;
        while(qu--) {
            int a, b;
            cin >> a >> b;
            u(a, b, 1, 1);
        } 
        for(int i = 1; i <= n; i++)  cout << q(i, i) << " \n"[i == n];
        reset();
    }
    return 0;
}

