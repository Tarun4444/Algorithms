import java.util.*;

class linkedListAdd{
  public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    LinkedList<Integer> link1=new LinkedList<Integer>();
    LinkedList<Integer> link2=new LinkedList<Integer>();
    LinkedList<Integer> result=new LinkedList<Integer>();

    String l1=sc.next();
    for(int i=l1.length()-1;i>=0;i--){
      link1.add(l1.charAt(i)-'0');
    }
    String l2=sc.next();
    for(int i=l2.length()-1;i>=0;i--){
      link2.add(l2.charAt(i)-'0');
    }

    int a=l1.length();
    int b=l2.length();
    int carry=0,add=0;
      for(int i=0,j=0 ; i<a && j<b ; i++,j++){
        add=carry+link1.get(i)+link2.get(j);
        //System.out.println(link2.get(i)+link1.get(i))
        if(add>9){
          carry=add/10;
          add=add%10;
        }else{
          carry=0;
        }
        System.out.print(add);
      }

      int x=0,y=0;

      while(x<a){
        add=link1.get(x)+carry;
        if(add>9){
          carry=add/10;
          add=add%10;
        }else{
          carry=0;
        }
        System.out.print(add);
        x++;
      }

      while(y<b){
        add=carry+link2.get(y);
        if(add>9){
          carry=add/10;
          add=add%10;
        }else{
          carry=0;
        }
        System.out.print(add);
      }
      y++;
  }
}
