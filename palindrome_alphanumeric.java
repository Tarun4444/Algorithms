/* package codechef; // don't place package name! */
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String args[])throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());

        while(t>0){
            String c=br.readLine();
            String q=c.toLowerCase();
            char[] s=q.toCharArray();
            int l=s.length;

            int a=0;
            int b=l-1;

            while(a<b){
                if((s[a]>='0' && s[a]<='9') && (s[b]>='0' && s[b]<='9') ||
                (('a'<=s[a] && s[a] <='z') && ('a'<=s[b] && s[b]<='z') ||
                ('A'<=s[a] && s[a] <='Z') && ('A'<=s[b] && s[b]<='Z')) ){

                    if(s[a]!=s[b]){
                        System.out.println("NO");
                        break;
                    }else{
                        //System.out.println(s[a]+" "+s[b]);
                        a++;
                        b--;
                    }

                }else{
                    //Special Character
                    if(s[a]==' '&&s[b]==' '){
                        a++;
                        b--;
                    }else if(s[a]==' '){
                        a++;
                    }else if(s[b]==' '){
                        b--;
                    }else{

                    }

                    if((!Character.isDigit(s[a]) && !Character.isLetter(s[a])) && (!Character.isDigit(s[b]) && !Character.isLetter(s[b]))){
                        a++;
                        b--;
                    }
                    else if(!Character.isDigit(s[a]) && !Character.isLetter(s[a])){
                        a++;
                    }else if(!Character.isDigit(s[b]) && !Character.isLetter(s[b])){
                        b--;
                    }else{

                    }
                }
            }

            if(a>=b){
                System.out.println("YES");
            }
            t--;
        }
	}
}
