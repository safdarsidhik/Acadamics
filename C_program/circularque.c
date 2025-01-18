#include <stdio.h>
#include <stdlib.h>
#define N 5

int front = -1, rear = -1;
int queue[N];

void insert() {
    int item;
    printf("Enter the item to be inserted: ");
    scanf("%d", &item);
    if (((rear + 1) % N) == front) {
        printf("The Queue is Full\n");
    } else if (front == -1 && rear == -1) {
        front = rear = 0;
        queue[rear] = item;
    } else {
        rear = (rear + 1) % N;
        queue[rear] = item;
    }
}

void delete() {
    if (front == -1 && rear == -1) {
        printf("The Queue is Empty\n");
    } else if (front == rear) {
        printf("The deleted element is %d\n", queue[front]);
        front = rear = -1;
    } else {
        printf("The deleted element is %d\n", queue[front]);
        front = (front + 1) % N;
    }
}

void display() {
    if (front == -1 && rear == -1) {
        printf("The Queue is Empty\n");
    } else {
        int i = front;
        printf("The Queue is: ");
        while (i != rear) {
            printf("%d\t", queue[i]);
            i = (i + 1) % N;
        }
        printf("%d\n", queue[i]);
    }
}

int main() {
    int choice;
    while (1) {
        printf("1. Insertion\n2. Deletion\n3. Display\n4. Exit\nEnter your choice:\n");
        scanf("%d", &choice);
        switch (choice) {
        case 1: insert(); break;
        case 2: delete(); break;
        case 3: display(); break;
        case 4: exit(0);
        default: printf("Invalid choice\n");
        }
    }
}