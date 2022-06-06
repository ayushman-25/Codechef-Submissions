/*

* Author : Ayushman Chahar #
* About  : II Year, IT Undergrad #
* Insti  : VIT, Vellore #

*/

//Directive, OptimIsation Flags, Targets
#pragma GCC optimIze("Ofast")  
#pragma GCC target("avx,avx2,fma") 
#pragma GCC optimIzation ("unroll-loops")

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
#include <unordered_map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <climits>
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


//Basic mIn and max
template<typename T, typename U> inline void amIn(T &x, U y) { if(y < x) x = y; }
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

// GFG REFERENCE PRIM's ALGO for DENSE gaOS using ADJ. LIST Representaion ---
// https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/


// GFG REFERENCE for a custom hash pair to make unordered_map take pair as a key;
struct kala_jaadu { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
};

unordered_map<pair<int, int>, int, kala_jaadu> vajan_maapna;

struct aLN { 
    int swarg; 
    int vajan; 
    struct aLN* next; 
}; 

struct aL { 
    struct aLN* head;
}; 

struct gaO { 
    int V; 
    struct aL* array; 
}; 
 
struct aLN* newaLN(int swarg, int vajan) { 
    struct aLN* newNode = (struct aLN*)malloc(sizeof(struct aLN)); 
    newNode->swarg = swarg; 
    newNode->vajan = vajan; 
    newNode->next = NULL; 
    return newNode; 
} 
 
struct gaO* creategaO(int V) { 
    struct gaO* gaO = (struct gaO*)malloc(sizeof(struct gaO)); 
    gaO->V = V; 
    gaO->array = (struct aL*)malloc(V * sizeof(struct aL)); 
    for (int i = 0; i < V; ++i) 
        gaO->array[i].head = NULL; 
    return gaO; 
} 

void rastA(struct gaO* gaO, int src, int swarg, int vajan) { 
    struct aLN* newNode = newaLN(swarg, vajan); 
    newNode->next = gaO->array[src].head; 
    gaO->array[src].head = newNode; 
    newNode = newaLN(src, vajan); 
    newNode->next = gaO->array[swarg].head; 
    gaO->array[swarg].head = newNode; 
} 

struct ChotaGharNode { 
    int v; 
    int chaabi; 
}; 

struct ChotaGhar { 
    int size; 
    int capacity; 
    int* pos; 
    struct ChotaGharNode** array; 
}; 

struct ChotaGharNode* newChotaGharNode(int v, int chaabi) { 
    struct ChotaGharNode* ChotaGharNode = (struct ChotaGharNode*)malloc(sizeof(struct ChotaGharNode)); 
    ChotaGharNode->v = v; 
    ChotaGharNode->chaabi = chaabi; 
    return ChotaGharNode; 
} 

struct ChotaGhar* createChotaGhar(int capacity) { 
    struct ChotaGhar* ChotaGhar = (struct ChotaGhar*)malloc(sizeof(struct ChotaGhar)); 
    ChotaGhar->pos = (int*)malloc(capacity * sizeof(int)); 
    ChotaGhar->size = 0; 
    ChotaGhar->capacity = capacity; 
    ChotaGhar->array = (struct ChotaGharNode**)malloc(capacity * sizeof(struct ChotaGharNode*)); 
    return ChotaGhar; 
} 

void swapChotaGharNode(struct ChotaGharNode** a, struct ChotaGharNode** b) { 
    struct ChotaGharNode* t = *a; 
    *a = *b; 
    *b = t; 
} 

void ChotaGharify(struct ChotaGhar* ChotaGhar, int idx) { 
    int smallest, left, right; 
    smallest = idx; 
    left = 2 * idx + 1; 
    right = 2 * idx + 2; 
    if (left < ChotaGhar->size && ChotaGhar->array[left]->chaabi < ChotaGhar->array[smallest]->chaabi) smallest = left; 
    if (right < ChotaGhar->size && ChotaGhar->array[right]->chaabi < ChotaGhar->array[smallest]->chaabi) smallest = right; 
    if (smallest != idx) { 
        ChotaGharNode* smallestNode = ChotaGhar->array[smallest]; 
        ChotaGharNode* idxNode = ChotaGhar->array[idx]; 
        ChotaGhar->pos[smallestNode->v] = idx; 
        ChotaGhar->pos[idxNode->v] = smallest; 
        swapChotaGharNode(&ChotaGhar->array[smallest], &ChotaGhar->array[idx]); 
        ChotaGharify(ChotaGhar, smallest); 
    } 
} 

int khaali(struct ChotaGhar* ChotaGhar) { 
    return ChotaGhar->size == 0; 
} 

struct ChotaGharNode* extractMin(struct ChotaGhar* ChotaGhar) { 
    if (khaali(ChotaGhar)) 
        return NULL; 
    struct ChotaGharNode* root = ChotaGhar->array[0]; 
    struct ChotaGharNode* lastNode = ChotaGhar->array[ChotaGhar->size - 1]; 
    ChotaGhar->array[0] = lastNode; 
    ChotaGhar->pos[root->v] = ChotaGhar->size - 1; 
    ChotaGhar->pos[lastNode->v] = 0; 
    --ChotaGhar->size; 
    ChotaGharify(ChotaGhar, 0); 
  
    return root; 
} 

void decreasechaabi(struct ChotaGhar* ChotaGhar, int v, int chaabi) { 
    int i = ChotaGhar->pos[v]; 
    ChotaGhar->array[i]->chaabi = chaabi; 
    while (i && ChotaGhar->array[i]->chaabi < ChotaGhar->array[(i - 1) / 2]->chaabi) { 
        ChotaGhar->pos[ChotaGhar->array[i]->v] = (i - 1) / 2; 
        ChotaGhar->pos[ChotaGhar->array[(i - 1) / 2]->v] = i; 
        swapChotaGharNode(&ChotaGhar->array[i], &ChotaGhar->array[(i - 1) / 2]); 
        i = (i - 1) / 2; 
    } 
} 

bool isInChotaGhar(struct ChotaGhar* ChotaGhar, int v) { 
    if (ChotaGhar->pos[v] < ChotaGhar->size) 
        return true; 
    return false; 
} 
 
void dikha(int arr[], int n) { 
    lli ans = 0;
    for (int i = 1; i < n; ++i)  ans += vajan_maapna[{min(arr[i], i), max(arr[i], i)}];
    cout << abs(ans) << "\n";
} 

void jaadu(struct gaO* gaO) { 
    int V = gaO->V;
    int mapa[V];
    int chaabi[V];
    struct ChotaGhar* ChotaGhar = createChotaGhar(V); 
    for (int v = 1; v < V; ++v) { 
        mapa[v] = -1; 
        chaabi[v] = INT_MAX; 
        ChotaGhar->array[v] = newChotaGharNode(v, chaabi[v]); 
        ChotaGhar->pos[v] = v; 
    } 
    chaabi[0] = 0; 
    ChotaGhar->array[0] = newChotaGharNode(0, chaabi[0]); 
    ChotaGhar->pos[0] = 0; 
    ChotaGhar->size = V; 
    while (!khaali(ChotaGhar)) { 
        struct ChotaGharNode* ChotaGharNode = extractMin(ChotaGhar); 
        int u = ChotaGharNode->v;
        struct aLN* saanp_ki_chaal = gaO->array[u].head; 
        while (saanp_ki_chaal != NULL) { 
            int v = saanp_ki_chaal->swarg; 
            if (isInChotaGhar(ChotaGhar, v) && saanp_ki_chaal->vajan < chaabi[v]) { 
                chaabi[v] = saanp_ki_chaal->vajan; 
                mapa[v] = u; 
                decreasechaabi(ChotaGhar, v, chaabi[v]); 
            } 
            saanp_ki_chaal = saanp_ki_chaal->next; 
        } 
    } 
    dikha(mapa, V); 
}


// Initialize main()
int main() {    
    // McQueen;
    int V, dim;
    cin >> V >> dim;
    struct gaO* gaO = creategaO(V);
    vector<vector<int> > black_holes;
    for(int i = 0 ; i < V; i++) {
        vector<int> d(dim);
        for(int& inp: d) cin >> inp;
        black_holes.push_back(d);
    }
    for(int i = 0; i < V; i++) {
        int temp = 1;
        for(int j = 0; j < V; j++) {
            int curr_w = 0;
            if(i != j) {
                for(int z = 0; z < dim; z++)  curr_w += abs(black_holes[i][z] - black_holes[j][z]);
                // cout << i << " " << j << "\n";
                rastA(gaO, i, i + temp, -curr_w);
                pair<int, int> jodi(i, i + temp);
                vajan_maapna[jodi] = -curr_w;
                // vajan_maapna.insert({{i, i + temp}, -curr_w});
                temp++;
            }
        }
    }
    jaadu(gaO);
    return 0;
}
