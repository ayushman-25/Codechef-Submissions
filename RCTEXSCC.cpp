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
//#include <boost/multiprecision/cpp_lli.hpp>

//using boost :: multiprecision :: cpp_lli;
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
#define FOR(i, j, k, in) for (lli i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (lli i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (lli)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
// #define p 1000000007
#define read(type) readlli<type>()
#define McQueen ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr)
const double pi = acos(-1.0);
typedef long long lli;
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
    lli i = 20;
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

template <typename T> inline T readlli()
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

const lli p = 998244353;
const lli N = 1e5 + 69;
vector<lli> fNI(N + 1), nNI(N + 1), fact(N + 1);


void IoN() {
    nNI[0] = nNI[1] = 1;
    for(lli i = 2; i < N + 1; i++) {
        nNI[i] = (nNI[p % i] * (p - p / i) % p);
    }
}


void IoF() {
    fNI[0] = fNI[1] = 1;
    for(lli i = 2; i <= N + 1; i++) {
        fNI[i] = (nNI[i] * fNI[i - 1]) % p;
    }
}


void f() {
    fact[0] = 1;
    for(lli i = 1; i < N + 1; i++) {
        fact[i] = (fact[i - 1] * i) % p;
    }
}


lli bino(lli N, lli R) {
    return ((fact[N] * fNI[R]) % p * fNI[N - R]) % p;
}


lli power(lli x, lli y) {
    lli res = 1;
    x %= p;
    if(x == 0) return 0;
    while(y > 0) {
        if(y & 1) res = (res * x) % p;
        y >>= 1;
        x = (x * x) % p;
    }
    return res;
}


lli pI(lli a) {
    lli m = p;
    lli m0 = m, y = 0, x = 1;
    if(m == 1) return 0;
    while(a > 1) {
        lli q = a / m;
        lli t = m;
        m = a % m, a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    if(x < 0) x += m0;
    return x;
}

//Initialize main()
int main()  {
    IoN();
    IoF();
    f();
    McQueen;
    lli m, n, k;
    cin >> m >> n >> k;
    lli sum1 = 0;
    for(lli i = 0; i < n; i++) {
        sum1 = (sum1 % p + ((((i + 1) % p * bino(n - 1, i) % p) % p) * ((k % p * power(k - 1, i) % p) % p)) % p) % p;
    }
    lli ans = (sum1 % p * (pI(power(k, n))) % p) % p;
    cout << (ans ? ans : 1);
    return 0;
}