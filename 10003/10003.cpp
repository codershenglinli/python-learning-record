#include<iostream>
using namespace std;
int divide(int array[], int low, int high, int &num)
{   int pivoit=array[low],i=0,size=high-low,low2=low;

    if(size==1){//当长度为2时，直接比较，
        if(array[low]>array[high]){
            int tmp1=array[low];
            array[low]= array[high];
            array[high] = tmp1;
        };
        num++;
        if(size==1){
        return high;}
        else return low;
    }

    int *tmplow,*tmphigh;
    tmplow = new int [high-low];
    tmphigh = new int [high-low];
    low++;
    int l=low,h=high,j=0,k=0;
    
        while(l<=high){if(array[l++]<=pivoit) tmplow[i++]= array[l-1];

                        else tmphigh[j++]= array[l-1];
                        num++;}
        low--;

    for(int j=0;j<high- low+1;j++){
        if(j<i){array[j+low]= tmplow[j];}
        if(j>i){array[j+low] = tmphigh[k++];}
        if(j==i){array[j+low] = pivoit;}
    };
    int w=low-1;

    return i+low;
    delete [] tmphigh;
    delete [] tmplow;

}
void quicksort(int array[],int low,int high,int &num){
    int mid;
    if(low>=high) return;
    mid = divide(array,low,high,num);

    quicksort(array,low,mid-1,num);
    quicksort(array,mid+1,high,num);
}

int main(){

    int n=0,m=0,num=0;
    cin>>n;
    cin.get();
    int *array;
    array= new int [n];
    while(m++<n){cin>>array[m-1];}
    quicksort(array,0,n-1,num);
    cout<<num;
    delete [] array;
    return 0;
    
};