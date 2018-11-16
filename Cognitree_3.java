import java.util.*;
import java.io.*;

class StockBuySell{
    //"O(n^2)"
    void stockBuySell(double price[],String time[], int n) {
        int buy_time=-1,sell_time=-1;
        double max_profit=Integer.MIN_VALUE;
        double curr_profit=0;
        for(int i=0;i<n-1;i++){
          for(int j=i+1;j<n;j++){
            curr_profit=price[j]-price[i];
            if(curr_profit > 0 && curr_profit > max_profit){
              max_profit=curr_profit;
              sell_time=j;
              buy_time=i;
            }
          }
        }
        if(buy_time==-1 || sell_time==-1){
            System.out.print("No Profit");
            return;
        }
        System.out.println("Buy time:"+time[buy_time]);
        System.out.println("Sell time:"+time[sell_time]);
    }

    //"O(n)"
    void StockBuySell(double price[],String time[],int n) {
        int i=0,min=0,buy_time=-1,sell_time=-1;
        double profit=0;
        for (i=0;i<n;i++) {
            if(price[i]<price[min])
                min = i;
            else if(price[i]- price[min] > profit) {
                buy_time = min;
                sell_time = i;
                profit=price[i]-price[min];
            }
        }
        if(buy_time==-1 || sell_time==-1){
            System.out.print("No Profit");
            return;
        }
        System.out.println("Buy time:"+time[buy_time]);
        System.out.println("Sell time:"+time[sell_time]);
}

    public static void main(String args[]){
        StockBuySell stock = new StockBuySell();
        // stock prices and respective times
        double price[] = { 7.5, 7.9 , 8.0, 6.8,9.01};
        String time[] ={ "02:00","03:30","04:00","06:00","8:00"};
        int n = price.length;
        System.out.println("O(n^2)");
        stock.stockBuySell(price,time, n);
        System.out.println("O(n)");
        stock.StockBuySell(price,time,n);

    }
}
