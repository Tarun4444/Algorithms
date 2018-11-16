// A simple representation of graph using STL,for the purpose of competitive programming
#include<bits/stdc++.h>
using namespace std;
int ctr=0;
int mn = 150050;
int mx = 0;
int arr[100000] = {0};

// A utility function to add an edge in an undirected graph.
void addEdge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

// A utility function to do DFS of graph recursively from a given vertex u.
void DFSUtil(int u, vector<int> adj[],vector<bool> &visited){
    visited[u] = true;
    ctr++;
    for (int i=0; i<adj[u].size(); i++)
        if (visited[adj[u][i]] == false)
            DFSUtil(adj[u][i], adj, visited);
}

// This function does DFSUtil() for all unvisited vertices.
void DFS(vector<int> adj[], int V){
    //cout<<"c"<<V;
    for (int u=0; u<V; u++){
        //cout<<"b"<<u;
        if (arr[u] == 0){
           // cout<<"a"<<u;
			continue;
		}
		ctr=0;
		vector<bool> visited(V, false);
        if (visited[u] == false){
            DFSUtil(u, adj, visited);
        }

    if (ctr > mx){
		mx = ctr;
	}
	if (ctr < mn){
	    mn = ctr;
	}
  }
	cout<<mn<<" "<<mx;
}

// Driver code
int main(){
    int n;
	cin>>n;

	int V = 0;
    vector <int> adj[150050];
    //cout<<V;
	for (int i = 0; i < n; i++){
		int x,y;
		cin>>x>>y;
		if (x > V)V = x;
		if (y > V)V = y;
		arr[x] = 1;
		arr[y] = 1;
		addEdge(adj, x, y);
	}
    DFS(adj, V);
    return 0;
}
