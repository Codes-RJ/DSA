#include <iostream>
#include <queue>
#include <stack>
using namespace std;

struct Node {
    int data;
    Node* next;

    explicit Node(int value) : data(value), next(nullptr) {}
};

void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << ' ';
        head = head->next;
    }
    cout << "\n";
}

int main() {
    Node* head = new Node(10);
    head->next = new Node(20);
    head->next->next = new Node(30);

    cout << "Linked list: ";
    printList(head);

    stack<int> st;
    st.push(5);
    st.push(15);
    cout << "Stack top: " << st.top() << "\n";
    st.pop();

    queue<int> q;
    q.push(1);
    q.push(2);
    cout << "Queue front: " << q.front() << "\n";

    while (head != nullptr) {
        Node* nextNode = head->next;
        delete head;
        head = nextNode;
    }

    return 0;
}
