#include <iostream>
#include<vector>
using namespace std;

vector <int> adj[10000];

void addEdge(int u,int v){
  adj[u].push_back(v);
  adj[v].push_back(u);
}
void DFSutil(int u,vector<bool> &vis){
  vis[u]=true;
  cout << u;
  for(int i=0;i<adj[u].size();i++){
    if(adj[u][i]==false){
      DFSutil(adj[u][i],vis);
    }
  }
}
void DFS(int V){
  vector <bool> vis(V,false);
  for(int u=0;u<=V;u++){
    if(vis[u]==false){
      DFSutil(u,vis);
    }
  }
}
int main(){
  int V;
  cin>>V;
  int x,y;
  for(int i=0;i<V;i++){
    cin>>x >> y;
    addEdge(x,y);
  }
  DFS(V);
  return 0;
}
