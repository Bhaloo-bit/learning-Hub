// var c = 300
let a = 300
if (true) {
    let a = 10
    const b = 20 
    // console.log("inner",a)
    
}

// console.log(a);
// console.log(b);
// console.log(c);s

function one (){
    const username = "hitesh"

    function two (){
        const website = "youtube"
        console.log(username);

    }
    // console.log(website);
    // two()

}

// one()

if (true){
    const username = "hitesh"
    if (username === "hitesh"){
        const website = "youtube"
        // console.log(username + website);
    }
    // console.log(website);
}
// console.log(username);

// ******************* interesting ++++++++++++++++++

function addone(num){
    return num +1
}
console.log(addone(5))

const addtwo = function (num){
     second = num +2
    //  console.log(second)
     return second
}
addtwo(5)