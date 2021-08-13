/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
   let lenStr1 = strs[0].length;
    
    let result = "";
    for(i=1; i<=lenStr1; i++) {
        let temp = strs[0].substring(0,i);
        
        if(! strs.every(str => str.substring(0,i) == temp)) break;
        result = temp;
    }
    return result; 
};
​
​
​
