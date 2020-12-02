#include <bits/stdc++.h>  
using namespace std;  
int main(){ 
  
    string str = to_string(45); 
  
    //Use of reverse iterators 
    string rev = string(str.rbegin(),str.rend()); 
  
    cout<<rev<<endl;  
    return 0; 
} 