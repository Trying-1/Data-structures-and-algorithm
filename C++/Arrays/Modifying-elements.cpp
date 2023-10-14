//Modifying Elements: You can change the value of an array element by assigning a new value to it.
#include <iostream>
using namespace std;
int main(){
    int arr[5]={3,5,6,9,1};
    cout<<"before modifying:"<<arr[2]<<endl;
    arr[2]=8;
    cout<<"after modifying:"<<arr[2]<<endl;
    return 0;
}