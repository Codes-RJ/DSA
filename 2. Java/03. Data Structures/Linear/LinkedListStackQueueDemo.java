import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class LinkedListStackQueueDemo {
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    static void printList(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        printList(head);

        Stack<Integer> stack = new Stack<>();
        stack.push(5);
        stack.push(15);
        System.out.println("Stack top: " + stack.peek());

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        queue.offer(2);
        System.out.println("Queue front: " + queue.peek());
    }
}
