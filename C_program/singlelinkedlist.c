#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *head = NULL, *temp, *newnode;

void create() {
    newnode = (struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->data);
    newnode->next = NULL;

    if (head == NULL)
        head = newnode;
    else {
        temp = head;
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = newnode;
    }
}

void display() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    temp = head;
    printf("Linked list: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

void ins_beg() {
    newnode = (struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->data);
    newnode->next = head;
    head = newnode;
}

void ins_end() {
    newnode = (struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->data);
    newnode->next = NULL;
    
    if (head == NULL)
        head = newnode;
    else {
        temp = head;
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = newnode;
    }
}

void ins_pos() {
    int pos, i = 1;
    printf("Enter position: ");
    scanf("%d", &pos);

    if (pos == 1) {
        ins_beg();
        return;
    }

    newnode = (struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d", &newnode->data);

    temp = head;
    while (i < pos - 1 && temp != NULL) {
        temp = temp->next;
        i++;
    }

    if (temp == NULL) {
        printf("Invalid position!\n");
        free(newnode);
    } else {
        newnode->next = temp->next;
        temp->next = newnode;
    }
}

void del_beg() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    temp = head;
    head = head->next;
    free(temp);
}

void del_end() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    temp = head;
    if (head->next == NULL) {
        head = NULL;
        free(temp);
        return;
    }

    struct node *prev;
    while (temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    free(temp);
}

void del_pos() {
    int pos, i = 1;
    printf("Enter position: ");
    scanf("%d", &pos);

    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    temp = head;
    struct node *prev;

    if (pos == 1) {
        head = head->next;
        free(temp);
        return;
    }

    while (i < pos && temp != NULL) {
        prev = temp;
        temp = temp->next;
        i++;
    }

    if (temp == NULL) {
        printf("Invalid position!\n");
    } else {
        prev->next = temp->next;
        free(temp);
    }
}

int main() {
    int choice;
    while(1) {
        printf("\n1. Create\n2. Display\n3. Insert at Beginning\n4. Insert at End\n5. Insert at Position\n");
        printf("6. Delete from Beginning\n7. Delete from End\n8. Delete from Position\n9. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: create(); break;
            case 2: display(); break;
            case 3: ins_beg(); break;
            case 4: ins_end(); break;
            case 5: ins_pos(); break;
            case 6: del_beg(); break;
            case 7: del_end(); break;
            case 8: del_pos(); break;
            case 9: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}