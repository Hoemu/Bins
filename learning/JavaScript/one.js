var fs = require('fs')

//非阻塞
fs.readFile('input.txt', function(err, data){
    if(err) return console.err(err)
    else console.log(data.toString())
})
// console.log(data.toString())
console.log('执行结束')

//阻塞
// var data = fs.readFileSync('input.txt');

// console.log(data.toString());
// console.log("程序执行结束!");