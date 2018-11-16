import java.util.*;
import java.io.*;

class Interval {
    int buy, sell;
}

class StockBuySell {
    void stockBuySell(double price[],String time[], int n) {
        if (n == 1)
            return;
        int count = 0;
        ArrayList<Interval> sol = new ArrayList<Interval>();
        int i = 0;
        while (i < n - 1) {
            while ((i < n - 1) && (price[i + 1] <= price[i]))
                i++;
            if (i == n - 1)
                break;
 
            Interval e = new Interval();
            e.buy = i++;
            
            while ((i < n) && (price[i] >= price[i - 1]))
                i++;
            
            e.sell = i-1;
            sol.add(e);
            count++;
        }
 
        if (count == 0)
            System.out.println("There is no day when buying the stock "
                                                  + "will make profit");
        else{
            for (int j = 0; j < count; j++){
                System.out.println("Buy on time: " + time[sol.get(j).buy]); 
                System.out.println("Sell on time : " + time[sol.get(j).sell]);
            }
        }
        return;
    }
    
    public double maxProfit(double[] prices,String time[]) {
        if (prices.length <= 1) return 0;
    
        double minPrice = prices[0];
        double maxSoFar = Integer.MIN_VALUE;
        double profitSoFar = Integer.MIN_VALUE;
        int minIndex=0,maxIndex=0;
        for (int i = 1; i < prices.length; i++){
            profitSoFar = prices[i] - minPrice;
       
            if(prices[i]<minPrice){
                minPrice=prices[i];
                minIndex=i;
            }
            if(maxSoFar<profitSoFar){
                maxSoFar=profitSoFar;
                maxIndex=i;
            }
        }
        if(maxSoFar>0){
            System.out.println("TIME TO BUY:"+time[minIndex]+"       "+"TIME TO SELL:"+time[maxIndex]);
        }
    return Math.max(maxSoFar, 0);
}
 
    public static void main(String args[]) 
    {
        StockBuySell stock = new StockBuySell();
         
        // stock prices and respective times 
        double price[] = { 4.9, 4.8 , 5.0, 9.0,9.01};
        String time[] ={ "02:00","03:30","04:00","05:30","10:00"};
        int n = price.length;
 
        System.out.println("More than one transaction allowed not parallel:");
        stock.stockBuySell(price,time, n);
        
        System.out.println();
        
        System.out.println("one transaction allowed");
        System.out.println("maxProfit="+stock.maxProfit(price,time));
    }
}