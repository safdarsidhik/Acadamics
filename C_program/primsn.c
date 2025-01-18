#include <stdio.h>
#include <stdlib.h>
#define INF 999

// Function to input the cost matrix
void input(int num, int cost[10][10]) {
    int i, j;
    printf("Enter the cost matrix for %d vertices:\n", num);
    for (i = 1; i <=num; i++) {
        for (j = 1; j <=num; j++) {
            printf("Value of cost [%d][%d] : ", i, j);
            scanf("%d", &cost[i][j]);
            if (cost[i][j] == 0) {
                cost[i][j] = INF; // Replace 0 with INF to represent no edge
            }
        }
    }
}

// Function to display the cost matrix
void display(int num, int cost[10][10]) {
    int i, j;
    printf("The cost matrix is:\n");
    for (i = 1; i <=num; i++) {
        for (j = 1; j <=num; j++) {
            if (cost[i][j] == INF) {
                printf("INF "); // Print "INF" for no edge
            } else {
                printf("%d ", cost[i][j]);
            }
        }
        printf("\n");
    }
}

// Function to implement Prim's algorithm
void prim(int num, int cost[10][10]) {
    int visited[10] = {0}, min, mincost = 0, ne = 1, a, b, i, j;
    visited[0] = 1; // Start with the first vertex

    printf("\nEdges in the Minimum Spanning Tree:\n");
    while (ne < num) {
        for (i = 1, min = INF; i <=num; i++) {
            if (visited[i] == 1) {
                for (j = 1; j <=num; j++) {
                    if (visited[j] == 0 && cost[i][j] < min) {
                        min = cost[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }
        if (min == INF) {
            printf("Graph is disconnected. No spanning tree exists.\n");
            return;
        }
        printf("Edge %d: (%d-%d) cost = %d\n", ne++, a, b, min);
        mincost += min;
        visited[b] = 1; // Mark the vertex as visited
    }
    printf("\nMinimum cost = %d\n", mincost);
}

int main() {
    int num, cost[10][10];
    printf("Enter the number of vertices (max 10): ");
    scanf("%d", &num);

    if (num > 10 || num <= 0) {
        printf("Error: Number of vertices must be between 1 and 10.\n");
        return 1;
    }

    input(num, cost);    // Input the cost matrix
    display(num, cost);  // Display the cost matrix
    prim(num, cost);     // Run Prim's algorithm

    return 0;
}