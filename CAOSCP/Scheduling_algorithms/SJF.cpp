#include <stdio.h>
#include <stdlib.h>
#define max 20
int main()
{

   int n,burstTime[20],waitingTime[20],turnAroundTime[20],averageWaitingTime=0,averageTurnAroundTime=0,i,j;
    printf("Enter total number of processes(maximum 20):");
    scanf("%d",&n);

    printf("\nEnter Process Burst Time\n");
    for(i=0;i<n;i++)
    {
        printf("P[%d]:",i+1);
        scanf("%d",&burstTime[i]);
    }

    waitingTime[0]=0;

    for(i=1;i<n;i++)
    {
        waitingTime[i]=0;
        for(j=0;j<i;j++)
            waitingTime[i]+=burstTime[j];
    }

printf("\nProcess\t\tBurst Time\tWaiting Time\tTurnaround Time");

    for(i=0;i<n;i++)
    {
        turnAroundTime[i]=burstTime[i]+waitingTime[i];
        averageWaitingTime+=waitingTime[i];
        averageTurnAroundTime+=turnAroundTime[i];
        printf("\nP[%d]\t\t%d\t\t%d\t\t%d",i+1,burstTime[i],waitingTime[i],turnAroundTime[i]);
    }

    averageWaitingTime/=i;
    averageTurnAroundTime/=i;
    printf("\n\nAverage Waiting Time:%d",averageWaitingTime);
    printf("\nAverage Turnaround Time:%d",averageTurnAroundTime);

return 0;
}