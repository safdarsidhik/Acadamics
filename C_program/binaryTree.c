#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left, *right;
};


struct node* create();  
void inorder(struct node* root);  
void preorder(struct node* root); 
void postorder(struct node* root); 

int main() {
    struct node *root = 0; 
    root = create();  
    
    printf("\nIn-order Traversal: ");
    inorder(root);

    printf("\nPre-order Traversal: ");
    preorder(root);

    printf("\nPost-order Traversal: ");
    postorder(root);
    
    return 0;
}

struct node* create() {
    int item;
    struct node *newnode = (struct node*)malloc(sizeof(struct node));

    printf("\nEnter Data (-1 for no node): ");
    scanf("%d", &item);


    newnode->data = item;
    printf("Enter the left child of %d: ", item);
    newnode->left = create();
    printf("Enter the right child of %d: ", item);
    newnode->right = create();

    return newnode;
}

// In-order Traversal: Left -> Root -> Right
void inorder(struct node* root) {
    if (root == 0) {
        return;
    }
    inorder(root->left);      // Traverse left subtree
    printf("%d ", root->data); // Visit root node
    inorder(root->right);     // Traverse right subtree
}

// Pre-order Traversal: Root -> Left -> Right
void preorder(struct node* root) {
    if (root == 0) {
        return;
    }
    printf("%d ", root->data); // Visit root node
    preorder(root->left);     // Traverse left subtree
    preorder(root->right);    // Traverse right subtree
}

// Post-order Traversal: Left -> Right -> Root
void postorder(struct node* root) {
    if (root == 0) {
        return;
    }
    postorder(root->left);    // Traverse left subtree
    postorder(root->right);   // Traverse right subtree
    printf("%d ", root->data); // Visit root node
}
