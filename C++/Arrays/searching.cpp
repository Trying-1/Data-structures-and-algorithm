// 5. Searching: Find a specific element in an array by comparing each element with the target value. Common search algorithms include linear search and binary search for sorted arrays.
#include<iostream>
using namespace std;
int main(){
    int arr[5]={4,5,2,1,8};
    cout<<"enter the number to search:"; 
    int numberToSearch;
    cin>>numberToSearch;
    bool found=false;
    for(int i=0;i<size(arr);i++){
        if(arr[i]==numberToSearch)
        {
            found=true;
            break;
        }
    }
    if(found){
        cout<<"number found on array"<<endl;
    }
    else {
        cout<<"number not found in array"<<endl;
    }
}
