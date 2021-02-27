#include<stdio.h>

int main() {
    long long n, rev = 0;
    scanf("%lld", &n);
    while(n > 0) {
        rev <<= 1;
        if(n & 1 == 1) rev ^= 1;
        n >>= 1;
    }
    printf("%lld", rev);
}