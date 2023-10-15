// 7. Adding Elements: While C++ arrays have a fixed size, you can create a new, larger array and copy elements from the original array to effectively "add" elements.
#include <iostream>
using namespace std;
int main(){
int arr[5]={5,2,6,8,9};
int n=sizeof(arr)/sizeof(arr[0]);
int newSize=n+1;
int newArr[newSize];
for(int i=0;i<n;i++){
    newArr[i]=arr[i];
}
newArr[n]=7;
for(int i=0;i<newSize;i++){
    cout<<newArr[i]<<endl;
}

    return 0;
}
