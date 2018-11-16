#include<math.h>
#include<iostream>
using namespace std;
/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct node
{
    int data;
    struct node* left;
    struct node* right;
};

int maxDepth(struct node* root){
  if(root==NULL)return 0;
  else{return 1+max(maxDepth(root->left), maxDepth(root->right));}
}

int diameter(struct node* root){
  if(root==NULL)return 0;
  else{
    int lDepth=maxDepth(root->left);
    int rDepth=maxDepth(root->right);

    int lDiameter=diameter(root->left);
    int rDiameter=diameter(root->right);

    return max(1+lDepth+rDepth,max(lDiameter,rDiameter));
  }
}

/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct node* newNode(int data) {
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return(node);
}

int main(){
  struct node *root = newNode(1);
  root->left = newNode(2);
  root->right = newNode(3);
  root->left->left = newNode(4);
  root->left->right = newNode(5);
  root->left->right->left = newNode(6);
  root->left->right->right= newNode(7);
  root->right->right = newNode(8);
  root->right->right->right = newNode(9);
  root->right->right->right->left = newNode(10);
  root->right->right->right->right= newNode(11);
  root->right->right->right->left->left = newNode(12);
  root->right->right->right->left->right = newNode(13);

  cout<< diameter(root);
  //printf("Hight of tree is %d", maxDepth(root));
  getchar();
    return 0;
}
