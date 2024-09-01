#include<iostream>
using namespace std;
int main(){
    int i=1,ans=0;
    int a[10000];
    int nexttotalnum[10000]={0};
    while(cin>>a[i]){
     
        if(a[i]!=0&&a[i]!=-1){
            int k=0,j=i;
            for(k=0;j>1;k++) j=j/2;
            ans += a[i]*k;
        }
        i++;
        if(cin.get()=='\n') break;
    }
    cout<<ans;

return 0;
}

