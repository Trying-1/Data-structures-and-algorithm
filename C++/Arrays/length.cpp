// Finding Length: Determine the number of elements in an array, usually using the sizeof operator or by keeping track of the array's size.
#include<iostream>
using namespace std;
int main(){
    int arr[5]={3,5,4,1,8};
    // length of array is the number of element in array like here 5
    // to find length we calculate by size of array/size of data type
    int length=sizeof(arr)/sizeof(int);
    cout<<length<<endl;

    length=size(arr);// inbuitl method for length of arrays
    cout<<length<<endl;
    return 0;
}