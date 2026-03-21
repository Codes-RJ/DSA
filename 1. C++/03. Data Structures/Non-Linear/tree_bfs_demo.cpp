#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int data) : value(data), left(nullptr), right(nullptr) {}
};

void bfs(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    queue<TreeNode*> pending;
    pending.push(root);

    while (!pending.empty()) {
        TreeNode* current = pending.front();
        pending.pop();
        cout << current->value << ' ';

        if (current->left != nullptr) {
            pending.push(current->left);
        }
        if (current->right != nullptr) {
            pending.push(current->right);
        }
    }
    cout << "\n";
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    cout << "Tree BFS: ";
    bfs(root);

    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
