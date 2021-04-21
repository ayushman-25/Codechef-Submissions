// Ayushman  Chahar

#include <iostream>
#include <stdlib.h>

using namespace std;

const int MAX = 2000000;

int* sieve(int limit);

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int* primes = sieve(MAX-1);
    int t;
    cin >> t;
    while(t--) {
        int n, k;
        cin >> n >> k;
        int* cookie = sieve(n);
        int fakePrimes = 0, res = -1;
        for (int i=0; i<MAX; i++) {
            if (cookie[i] && !primes[i])
                fakePrimes++;
            if (fakePrimes == k) {
                res = i;
                break;
            }
        }
        cout << res << endl;
        free(cookie);
    }
    free(primes);
    return 0;
}

int* sieve(int limit) {
    int* primes = new int[MAX];
        primes[0] = primes[1] = 0;
        for (int i=2; i<MAX; i++) primes[i] = 1;
        for (int i=2; i<=limit; i++)
            for (int j=2*i; j<MAX; j+=i)
                primes[j] = 0;
    return primes;
}
