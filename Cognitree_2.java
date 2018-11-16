import java.util.*;
import java.io.*;

class StockBuySell {

    void stockBuySell(double price[],String time[], int n) {
        int buy_time=0,sell_time=0;
        int max_profit=Integer.MIN_VALUE;
        int curr_profit=0;
        for(int i=0;i<n-1;i++){
          for(int j=i+1;j<n;j++){
            curr_profit=price[i]-price[j];
            if(curr_profit > 0 && curr_profit > max_profit){
              max_profit=curr_profit;
              sell_time=i;
              buy_time=j;
            }
          }
        }
        System.out.println("Buy time:"+time[buy_time]);
        System.out.println("Sell time:"+time[sell_Time]);
    }
    public static void main(String args[]){
        StockBuySell stock = new StockBuySell();

        // stock prices and respective times
        double price[] = { 7, 5 , 9, 3,5};
        String time[] ={ "02:00","03:30","04:00","06:00","8:00"};
        int n = price.length;

        System.out.println("one transaction allowed only , not multiple and not parallel:");
        stock.stockBuySell(price,time, n);

    }
}
