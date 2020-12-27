#include <iostream>
using namespace std;
class Rectangle{
    public:
    int length;
    int breath;
    void display(){
        cout<<length<<" "<<breath<<endl;
    }
};
class Rectangle_area: public Rectangle{
    public:
    // int length;
    // int breath;
    void read_input(){
        cin>>length>>breath;
    }
    void display(){
        cout<<length*breath<<endl;
    }
};
int main()
{
    Rectangle_area obj1;
    // Rectangle obj1;
    obj1.read_input();
    obj1.Rectangle::display();
    obj1.display();
    return 0;
}