#include <iostream>
using namespace std;

int main() {
    int t,n;
    cin>>t;
    while(t--){
        long long int prod=1;
        cin>>n;
        int arr[15];
        for(int i=0;i<n;i++){
            cin>>arr[i];
            prod*=arr[i];
        }
      cout<<prod<<" ";
    }
    
    return 0;
}