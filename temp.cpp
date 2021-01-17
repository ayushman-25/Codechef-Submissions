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
using namespace std; 
  
//Function to return precedence of operators 
int prec(char c) 
{ 
    if(c == '1') 
    return c; 
    if(c == '2') 
    return c; 
if(c == '3') 
    return c;
if(c == '4') 
    return c;
if(c == '5') 
    return c;
if(c == '6') 
    return c;
if(c == '7') 
    return c;
if(c == '8') 
    return c;
if(c == '9') 
    return c;
    // else if(c == '*' || c == '/') 
    // return 2; 
    // else if(c == '+' || c == '-') 
    // return 1; 
    // else
    // return -1; 
} 
  
// The main function to convert infix expression 
//to postfix expression 
void infixToPostfix(string s) 
{ 
    std::stack<char> st; 
    st.push('N'); 
    int l = s.length(); 
    string ns; 
    for(int i = 0; i < l; i++) 
    { 
          
        // If the scanned character is  
        // an operand, add it to output string. 
        if((s[i] >= 'a' && s[i] <= 'z') ||  
           (s[i] >= 'A' && s[i] <= 'Z')) 
        ns+=s[i]; 
  
        // If the scanned character is an  
        // ‘(‘, push it to the stack. 
        else if(s[i] == '(') 
          
        st.push('('); 
          
        // If the scanned character is an ‘)’,  
        // pop and to output string from the stack 
        // until an ‘(‘ is encountered. 
        else if(s[i] == ')') 
        { 
            while(st.top() != 'N' && st.top() != '(') 
            { 
                char c = st.top(); 
                st.pop(); 
               ns += c; 
            } 
            if(st.top() == '(') 
            { 
                char c = st.top(); 
                st.pop(); 
            } 
        } 
          
        //If an operator is scanned 
        else{ 
            while(st.top() != 'N' && prec(s[i]) <=  
                                   prec(st.top())) 
            { 
                char c = st.top(); 
                st.pop(); 
                ns += c; 
            } 
            st.push(s[i]); 
        } 
  
    } 
    
    // Pop all the remaining elements from the stack 
    while(st.top() != 'N') 
    { 
        char c = st.top(); 
        st.pop(); 
        ns += c; 
    } 
      
    cout << ns << endl; 
  
} 
  
//Driver program to test above functions 
int main() 
{ 
    string exp; 
    cin >> exp;
    infixToPostfix(exp); 
    return 0;
}