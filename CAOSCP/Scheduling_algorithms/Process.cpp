#include<stdio.h> 
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
  
  
int main() 
{ 
    for(int i=0;i<5;i++)
    { 
        if(fork() == 0) 
        { 
            printf("[son] pid %d from [parent] pid %d\n",getpid(),getppid()); 
            exit(0); 
        } 
    } 
    for(int i=0;i<5;i++) 
    wait(NULL); 
      
}