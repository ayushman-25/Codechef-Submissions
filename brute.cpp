#include<iostream>
using namespace std;

#define N 1000000007

unsigned long moduloInverse[11] = {0};
unsigned long factorial[501] = {0};

unsigned long exponentiate(unsigned long a, unsigned long p) {
    if(p == 0) return 1;
    if(p%2) { // odd
        unsigned long res = exponentiate(a,(p-1)>>1);
        res = (res*res)%N;
        res = (a*res)%N;
        return res;
    }
    // even
    unsigned long res = exponentiate(a,p>>1);
    res = (res*res)%N;
    return res;
}

int main(int argc, char** argv) {
    // pre-calculate
    unsigned long start = 1;
    moduloInverse[start] = 1;
    for(unsigned long i=2; i<=10; i++){
        start *= i;
        moduloInverse[i] = exponentiate(start, N-2);
    }

    start = 1;
    factorial[start] = 1;
    for(unsigned long i=2; i<=500; i++){
        start = (start*i)%N;
        factorial[i] = start;
    }

    int t = 1;
    string s;
    // cin >> t;
    while(t--){
        cin >> s;
        int lowCount[26] = {0};
        int highCount[26] = {0};
        for(int i=0; i<s.length(); i++){
            if(s[i] >= 'a' && s[i] <= 'z') lowCount[s[i]-'a']++;
            if(s[i] >= 'A' && s[i] <= 'Z') highCount[s[i]-'A']++;
        }
        
        unsigned long ways = factorial[s.length()];
        for(int i=0; i<26; i++){
            if(lowCount[i] > 0) ways = (ways * moduloInverse[lowCount[i]])%N;
            if(highCount[i] > 0) ways = (ways * moduloInverse[highCount[i]])%N;
        }
        cout << ways << endl;
    }
}