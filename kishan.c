// program 1

// #include<stdio.h>
// int main()
// {
//     int n,num,i,largest,smallest;
//     printf("enter how many numer : ");
//     scanf("%d",&n);
//     printf("enter the munber1 :");
//     scanf("%d",&num);
//     largest = num;
//     smallest = num;
//     for(i=2;i<=n;i++){
//         printf("enter the number %d : ",i);
//         scanf("%d",&num);
//         if(num>largest)
//         largest = num;
//         if(num<smallest)
//         smallest = num;
//     }
//     printf("\nlargest = %d\n",largest);
//     printf("\nsmallest = %d\n",smallest);
    // return 0;

// }


// program 2 

#include<stdio.h>
int main(){
    int n,i,j,count;
    printf("enter the n value : ");
    scanf("%d",&n);
    for(i=2;i<=n;i++){
        count=0;
        for(j=1;j<=n;j++){
            if(i%j==0)
            count++;
        }
        if(count==2)
        printf("%d\n",i);
    }
    return 0;
}