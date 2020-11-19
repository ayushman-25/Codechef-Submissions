/*

* Author : Ayushman Chahar #

*/
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
defineInFor(long)
defineInFor(long long)
defineInFor(unsigned int)
defineInFor(unsigned long)
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
defineOutFor(long)
defineOutFor(long long)
defineOutFor(unsigned int)
defineOutFor(unsigned long)
defineOutFor(unsigned long long)

#define endl ('\n')
#define cout __io__
#define cin __io__
} __io__;

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
    //McQueen;
    int t;
    cin >> t;
    while(t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        for(auto& i : arr) cin >> i;
        vector<int> temparr = arr;
        //vector<int> sorted_arr;
        //for(int i = 1; i <= n; i++)
        //    sorted_arr.push_back(i);
        int ans_flag1 = 0;
        vector<vector<int> > ans1;
        vector<vector<int> > ans2;
        vector<int> sorted_arr;
        for(int i = 1; i <= n; i++) sorted_arr.push_back(i);
        if(sorted_arr == arr)
        {
            cout << 0 << "\n";
            continue;
        }
        bool ans_achieved1 = false;
        bool ans_achieved2 = false;
        int i = 0;
        while(true)
        {
            if((arr[n - 1] == (n)) & (i == n))
            {
                ans_flag1 = 1;
                ans_achieved1 = true;
                break;
            }
            if(arr[i] == (i + 1))
            {
                i++;
                continue;
            }
            const int id1 = i;
            const int tempid2 = arr[i] - 1;
            if(arr[tempid2] - 1 != i)
            {
                int id3 = arr[tempid2] - 1;
                if(id3 < tempid2)
                {
                    const int id2 = id3;
                    id3 = tempid2;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans1.push_back({id3, id2, id1});
                    arr[id1] = val2;
                    arr[id2] = val3;
                    arr[id3] = val1;
                }
                else
                {
                    const int id2 = tempid2;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans1.push_back({id1, id2, id3});
                    arr[id1] = val3;
                    arr[id2] = val1;
                    arr[id3] = val2;
                }
            }
            else
            {
                bool got_the_index = false;
                //int temp_idd1 = -1;
                //int temp_idd2 = -1;
                int temp_id = -1;
                /*
                if((tempid2 - id1) > 1)
                {
                    for(int x = id1 + 1; x < n; x++)
                    {
                        if(x != tempid2)
                        {
                            if(arr[x] != (x + 1))
                            {
                                temp_id = x;
                                got_the_index = true;
                                break;
                            }
                        }
                    }
                }
                else
                {
                    for(int x = n - 1; x > tempid2; x--)
                    {
                        if((arr[x] - arr[x - 1]) == -1)
                        {
                            temp_id = x;
                            got_the_index = true;
                            break;

                        }
                    }
                }
                */
                //for(int x = id1 + 1; x < n; x++)
                //{
                 //   if((x != tempid2) && (arr[x] != (x + 1)))
                  //  {
                //        if(arr[arr[x] - 1] == (x + 1))
                 //       {
                  //          temp_idd1 = arr[x] - 1;
                //            got_the_index = true;
                 //           break;
                  //      }
                //        /*
                 //       else
                  //      {
                //            temp_id = x;
                 //           got_the_index = true;
                  //          break;
                //        }
                 //       */
                  //  }
                //}
                //if(!got_the_index)
                //{
                for(int x = id1 + 1; x < n; x++)
                    {
                        if((x != tempid2) && (arr[x] != (x + 1)))
                        {
                            temp_id = x;
                            got_the_index = true;
                            break;
                        }
                    }
                //}
                if(!got_the_index)
                {   
                    ans1.clear();
                    ans_achieved1 = false;
                    break;
                }
                /*
                if(arr[id1 + 1] != (id1 + 2))
                {
                    temp_id = id1 + 1;
                    got_the_index = true;
                }
                if((!got_the_index) && (arr[tempid2 - 1] != (tempid2)))
                {
                    temp_id = tempid2 - 1;
                    got_the_index = true;
                }
                if(!got_the_index)
                {
                    cout << - 1 << "\n";
                    break;
                }
                */
                //if(temp_idd1 > temp_idd2)
                 //   temp_id = temp_idd1;
                //else if(temp_idd1 < temp_idd2)
                 //   temp_id = temp_idd2;
                //else
                 //   temp_id = temp_idd1;
                if(temp_id < tempid2)
                {
                    const int id3 = tempid2;
                    const int id2 = temp_id;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans1.push_back({id1, id2, id3});
                    arr[id1] = val3;
                    arr[id2] = val1;
                    arr[id3] = val2;
                }
                else
                {
                    const int id2 = tempid2;
                    const int id3 = temp_id;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans1.push_back({id3, id2, id1});
                    arr[id1] = val2;
                    arr[id2] = val3;
                    arr[id3] = val1;
                }
            }
        }
        i = 0;
        arr = temparr;
        //for(int zz = 0; zz < n; zz++)
         //   cout << arr[zz] << " ";
        //cout << "\n";
        int ans_flag2 = 0;
        while(true)
        {
            if((arr[n - 1] == (n)) & (i == n))
            {
                ans_flag2 = 1;
                ans_achieved2 = true;
                break;
            }
            if(arr[i] == (i + 1))
            {
                i++;
                continue;
            }
            const int id1 = i;
            const int tempid2 = arr[i] - 1;
            if(arr[tempid2] - 1 != i)
            {
                int id3 = arr[tempid2] - 1;
                if(id3 < tempid2)
                {
                    const int id2 = id3;
                    id3 = tempid2;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans2.push_back({id3, id2, id1});
                    arr[id1] = val2;
                    arr[id2] = val3;
                    arr[id3] = val1;
                }
                else
                {
                    const int id2 = tempid2;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans2.push_back({id1, id2, id3});
                    arr[id1] = val3;
                    arr[id2] = val1;
                    arr[id3] = val2;
                }
            }
            else
            {
                bool got_the_index = false;
                //int temp_idd1 = -1;
                //int temp_idd2 = -1;
                int temp_id = -1;
                /*
                if((tempid2 - id1) > 1)
                {
                    for(int x = id1 + 1; x < n; x++)
                    {
                        if(x != tempid2)
                        {
                            if(arr[x] != (x + 1))
                            {
                                temp_id = x;
                                got_the_index = true;
                                break;
                            }
                        }
                    }
                }
                else
                {
                    for(int x = n - 1; x > tempid2; x--)
                    {
                        if((arr[x] - arr[x - 1]) == -1)
                        {
                            temp_id = x;
                            got_the_index = true;
                            break;

                        }
                    }
                }
                */
                for(int x = id1 + 1; x < n; x++)
                {
                    if((x != tempid2) && (arr[x] != (x + 1)))
                    {
                        if(arr[arr[x] - 1] == (x + 1))
                        {
                            temp_id = arr[x] - 1;
                            got_the_index = true;
                            break;
                        }
                        /*
                        else
                        {
                            temp_id = x;
                            got_the_index = true;
                            break;
                        }
                        */
                    }
                }
                if(!got_the_index)
                {
                for(int x = id1 + 1; x < n; x++)
                    {
                        if((x != tempid2) && (arr[x] != (x + 1)))
                        {
                            temp_id = x;
                            got_the_index = true;
                            break;
                        }
                    }
                }
                if(!got_the_index)
                {
                    ans2.clear();
                    ans_achieved2 = false;
                    break;
                }
                /*
                if(arr[id1 + 1] != (id1 + 2))
                {
                    temp_id = id1 + 1;
                    got_the_index = true;
                }
                if((!got_the_index) && (arr[tempid2 - 1] != (tempid2)))
                {
                    temp_id = tempid2 - 1;
                    got_the_index = true;
                }
                if(!got_the_index)
                {
                    cout << - 1 << "\n";
                    break;
                }
                */
                //if(temp_idd1 > temp_idd2)
                 //   temp_id = temp_idd1;
                //else if(temp_idd1 < temp_idd2)
                 //   temp_id = temp_idd2;
                //else
                 //  temp_id = temp_idd1;
                if(temp_id < tempid2)
                {
                    const int id3 = tempid2;
                    const int id2 = temp_id;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans2.push_back({id1, id2, id3});
                    arr[id1] = val3;
                    arr[id2] = val1;
                    arr[id3] = val2;
                }
                else
                {
                    const int id2 = tempid2;
                    const int id3 = temp_id;
                    const int val1 = arr[id1];
                    const int val2 = arr[id2];
                    const int val3 = arr[id3];
                    ans2.push_back({id3, id2, id1});
                    arr[id1] = val2;
                    arr[id2] = val3;
                    arr[id3] = val1;
                }
            }
        }
        //if((ans2.size() <= (n / 2)) && (ans2.size() > 0))
        //{
         //   int a2s = ans2.size();
          //  cout << a2s << "\n";
        //    for(auto i : ans2)
         //   {
          //      for(auto j : i)
        //            cout << j + 1 << " ";
         //       cout << "\n";
          //  }
        //    continue;
        //}
        if((!ans_achieved1) && (!ans_achieved2))
        {
            cout << -1 << "\n";
            continue;
        }
        if((!ans_achieved2) && ans_achieved1)
        {
            cout << ans1.size() << "\n";
            for(auto i : ans1)
            {
                for(auto j : i)
                    cout << j + 1 << " ";
                cout << "\n";
            }
            continue;
        }
        if((!ans_achieved1) && ans_achieved2)
        {
            cout << ans2.size() << "\n";
            for(auto i : ans2)
            {
                for(auto j : i)
                    cout << j + 1 << " ";
                cout << "\n";
            }
            continue;
        }
        if(ans_achieved1 && ans_achieved2)
        {   
            int a1s = ans1.size();
            int a2s = ans2.size();
            //cout << a1s << " " << a2s << " ";
            if(a1s < a2s)
            {
                cout << a1s << "\n";
                for(auto i : ans1)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }
            else
            {
                cout << a2s << "\n";
                for(auto i : ans2)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }
            /*
            if((a1s == 0) && (a2s > 0))
            {
                cout << a2s << "\n";
                for(auto i : ans2)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }
            else if((a2s == 0) && (a1s > 0))
            {
                cout << a1s << "\n";
                for(auto i : ans1)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }
            else if((a1s > 0) && (a2s > 0))
            {
                cout << a2s << "\n";
                for(auto i : ans2)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }
            else
            {
                cout << a2s << "\n";
                for(auto i : ans2)
                {
                    for(auto j : i)
                        cout << j + 1 << " ";
                    cout << "\n";
                }
            }*/
        }
    }
    return 0;
}
