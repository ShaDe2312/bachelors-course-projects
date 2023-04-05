#include<stdio.h>  

// Function to find waiting time 
void findWaitingTime(int processes[], int n,   
                          int bt[], int wt[])  
{  
    // waiting time for first process is 0  
    wt[0] = 0;  
    
    // calculating waiting time  
    for (int  i = 1; i < n ; i++ )  
        wt[i] =  bt[i-1] + wt[i-1] ;  
}  
    
// Function to calculate turn around time  
void findTurnAroundTime( int processes[], int n,int bt[], int wt[], int tat[])  
{  
    for (int  i = 0; i < n ; i++)  
        tat[i] = bt[i] + wt[i];  
}  
    
//Calculate average time  
void findavgTime( int processes[], int n, int bt[])  
{  
    int wt[n], tat[n], total_wt = 0, total_tat = 0;  
    
    //Waiting time of all processes  
    findWaitingTime(processes, n, bt, wt);  
    
    // Turn around time for all processes  
    findTurnAroundTime(processes, n, bt, wt, tat);  
     
    printf("Processes\tBurst time\tWaiting time\tTurn around time\n");  
    
    // Calculate total waiting time and total turnaround time  
    for (int  i=0; i<n; i++)  
    {  
        total_wt = total_wt + wt[i];  
        total_tat = total_tat + tat[i];  
        printf("%d ",(i+1)); 
        printf(" \t\t%d ", bt[i] ); 
        printf(" \t\t%d",wt[i] ); 
        printf(" \t\t%d\n",tat[i] );  
    }  
    int s=(float)total_wt / (float)n; 
    int t=(float)total_tat / (float)n; 
    printf("Average waiting time = %d",s); 
    printf("\n"); 
    printf("Average turn around time = %d ",t);  
}  
 
int main()  
{    
    printf("\n\n");
    int processes[] = { 1, 2, 3};  
    int n = sizeof processes / sizeof processes[0];  
    
    //Burst time of all processes  
    int  burst_time[] = {10, 5, 8};  
    
    findavgTime(processes, n,  burst_time);  
    return 0;  
}  
