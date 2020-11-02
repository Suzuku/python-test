//js中函数也可以作为参数，类似Python里的高阶函数
function getNum(x){
    return x+10; 
}

function high(x,y,func){
    
    console.log(func(x)+func(y));
}

high(2,3,getNum)