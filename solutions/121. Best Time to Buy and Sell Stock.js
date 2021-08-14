/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    buy=prices[0];
    
    profit=0;
    if(prices.length==1) return 0
    for(i=1;i<prices.length;i++){
        if(prices[i]<buy){
            buy=prices[i]
            var ivalue=i
        } 
       
    }
    
   sell=0
    for(j=ivalue;j<prices.length;j++){
        if(prices[j]>sell){
            sell=prices[j]
           
        } 
    }
    
    return sell-buy
    
};
