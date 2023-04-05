#include <bits/stdc++.h>
#define ll long long
#define ld long double 
#define ull unsigned long long
#define db double  
#define rep(i,a,b) for(ll i=a;i<b;++i)
#define de_rep(i,a,b) for(ll i=a-1;i>=b;--i)
#define Gausses Gauss();
using namespace std;
const int N=205,NN=205*205;
db f[N][N];
db res[NN];
void swap(db &a,db &b){
	db temp=a;
	a=b,b=temp;
}
void Gauss(){
	ll n; cin>>n;
	rep(i,0,n)rep(j,0,n+1) cin>>f[i][j];
	rep(i,0,n-1){
		int p=i,cnt=0;
		rep(j,i,n) {
			cnt++;
			if(f[j][i]!=0) {
				p=j;
				break;
			}
		} 
	//	cout<<"\n"<<p<<" "<<i<<"\n";
		if(cnt==n-i) {
			printf("‘No unique solution exists’");
			return;
		}
		if(p!=i) rep(j,0,n+1) swap(f[i][j],f[p][j]);
		
		rep(k,i+1,n){
			//cout<<"\n";
			db m=1.0*f[k][i]/f[i][i];
			rep(j,0,n+1){
			f[k][j]-=m*f[i][j];
			//cout<<f[k][j]<<" ";
			}
		}
//		rep(k,0,n){
//			cout<<"\n";
//			rep(j,0,n+1) cout<<f[k][j]<<" ";
//		}
	}	
	if(f[n-1][n-1]==0) {
		printf("‘No unique solution exists’");
		return;
	}
	res[n-1]=1.0*f[n-1][n]/f[n-1][n-1];
	de_rep(i,n-1,0){
		db temp=0;
		rep(j,i+1,n+1) temp+=f[i][j]*res[j];
		res[i]=1.0*(f[i][n]-temp)/f[i][i];
	}
	cout<<"\n";
	rep(i,0,n) printf("X%d %f\n",i+1,res[i]);
}
main(){
	Gausses;
}



