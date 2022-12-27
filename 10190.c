#include <stdio.h>
#include <math.h>
int a,b;

int show(int num,int cut){
    while (num>1)
    {
        printf("%d ",num);
        num = num / cut;

    }
    printf("1");
    
}

int boring(){
    printf("Boring!\n");
}

int m(int j ,int k ,int cu){
    if (j == k || k/cu == j)
    {
        show(a,b);
    }
    else if (k>j && k/cu != j){
        boring();
    }
    else
    {
        j = j/cu;
        k = k*cu;
        m(j,k,cu);
    }
    
    
}

int main(){
    scanf("%d%d",&a,&b);
    m(a,1,b);
    system("pause");
}