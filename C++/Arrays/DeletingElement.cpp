// 8. Deleting Elements: Similarly, you can create a new array without the elements you want to delete and copy the remaining elements.
#include <iostream>
using namespace std;
int main(){
    int arr[5]={5,2,6,8,9};
    int size=sizeof(arr)/sizeof(arr[0]);
    int newArr[size-1];
    int indexToDelete=3;
    for(int i=0,j=0;i<size;i++){
        if(i!=indexToDelete){
            newArr[j]=arr[i];
            j++;
        }
    }
    for(int i=0;i<size-1;i++){
        cout<<newArr[i]<<endl;
    }
    return 0;
}