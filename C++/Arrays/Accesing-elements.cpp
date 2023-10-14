//Accessing Elements: You can access individual elements of an array using their indices, which start at 0.
#include <iostream>
using namespace std;
int main(){
    int arr[5]={5,6,2,7,6};
    // indexing starts from 0  in arrays in cpp
    cout<<"element at index 3:"<< arr[3]<<endl; //output: 7
    return 0;
}