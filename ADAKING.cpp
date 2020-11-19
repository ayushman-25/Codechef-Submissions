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

//Initialize main()
int main() 
{
    McQueen;
   	int t;
   	cin >> t;
   	while(t--) {
   		int n;
   		cin >> n;
   		vector<int> A(n), B(n);
   		for(int& i : A) cin >> i;
   		for(int& i : B) cin >> i;
   		if(n == 1) {
   			if(A[0] != B[0]) cout << -1 << "\n";
   			else cout << 0 << "\n";
   			continue;
   		}
   		vector<int> tempA(A);
   		vector<int> tempB(B);
   		sort(tempA.begin(), tempA.end());
   		sort(tempB.begin(), tempB.end());
   		if(tempA == tempB) {
   			cout << 0 << "\n";
   			continue;
   		}
   		bool ans = true;
   		set<int> combinedset;
   		vector<int> combinedvector;
   		for(int i = 0; i < n; i++) {
   			combinedset.insert(A[i]);
   			combinedset.insert(B[i]);
   			combinedvector.push_back(A[i]);
   			combinedvector.push_back(B[i]);
   		}
   		for(auto it = combinedset.begin(); it != combinedset.end(); it++) {
   			if(count(combinedvector.begin(), combinedvector.end(), *it) & 1) {
   				ans = false;
   				cout << -1 << "\n";
   				break;
   			}
   		}
   		if(ans) {
   			vector<int> ansVector;
   			for(auto it = combinedset.begin(); it != combinedset.end(); it++) {
   				int acntit = count(A.begin(), A.end(), *it);
   				int bcntit = count(B.begin(), B.end(), *it);
   				if(acntit != bcntit) {
   					for(int j = 0; j < ((abs(acntit - bcntit)) / 2); j++)
   						ansVector.push_back(*it);
   				}
   			}
   			sort(ansVector.begin(), ansVector.end());
   			lli ans = 0;
   			for(int i = 0; i < (int) ansVector.size() / 2; i++) {
   				ans += ansVector[i];
   			}
   			cout << ans << "\n";
   		}
   	}
    return 0;
}

