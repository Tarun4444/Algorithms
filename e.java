import java.util.*;
import java.io.*;

class ticket{
  public static void main(String[] args)throws IOException{
    Queue<Integer> q1=new LinkedList<>();
    Queue<Integer> q2=new LinkedList<>();
    int a[]=new int[100000];
    boolean b[]=new boolean[100000];
    int n,x,t,T=1;
    Scanner sc=new Scanner(System.in);
    t=sc.nextInt();
    while(t>0){
        n=sc.nextInt();
        for(int i=0;i<n;i++){
          a[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++){
          b[i]=true;
        }
        x=sc.nextInt();

        for(int i=0;i<n;i++){
          q1.add(a[i]);
          q2.add(i);
        }
        int y,z;
        while(b[x]==true){
          z=q1.poll();
          y=q2.poll();
          y+=1;
          z-=1;
          if(z>0){
            q1.add(z);
            q2.add(y);
            T++;
          }else{
            b[y]=false;
          }
        }
        System.out.println(T);
        t--;
    }
  }
}
