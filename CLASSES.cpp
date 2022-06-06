#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void solve(){
    int long long  n{},m{};
    cin>>n>>m;
    vector<int>a{};
    
    int  arr[n];
    for(int i{};i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);
    for(int i{};i<n;i++){
        if(arr[i]!=arr[i+1]){
            a.push_back(arr[i]);
        }else{
            continue;
        }
    }
    for(int i: a) {
        cout << i << " ";
    }
    cout << "\n";
    if(a.size()==m){
        cout<<"No"<<endl;
    }
    else if(m>a.size()){
        cout<<"Yes"<<endl;
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        solve();
        
    }
}