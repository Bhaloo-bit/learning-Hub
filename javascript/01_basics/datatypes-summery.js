//  # Primitive 

// 7  types : String, Number, Boolearn, Null, undefined, Symbol, BigInt

const score = 100
const scoreValue =100.3

const isLoggedIn = false 
const outsidetemp = null
let userEmail;

const id =Symbol('1233')
const anotherId = Symbol("123")
// console.log(typeof (id))
// console.log(typeof anotherId)
// console.log(id ==anotherId);

// // types of val {
//     undefined = "undefined"
//     Null= "obeject"
//     Boolen= "boolean"
//     Number= "number"
//     string="string"
//     obejct 'object 
//     function= "function,


const bigNumber =123123234234n
// console.log(typeof (bigNumber))


// Reference (Non primtive)

//  Array, Objects, Functions 

const heros =["shatiman", "naagraj","odga"]
let myObh={
    name : "bhaloo",
    age:23,
}

const myFunction= function(){
    console.log("hello world");

}

// **************************************

// stack (Primitive ), Heap (Non-Primitive)

let myYoutubename = "bhaloobit"

let anothername= myYoutubename
anothername= "chaiurcode"

console.log(anothername);
console.log(anothername);

let userOne= {
    name:"ramu",
    email:"userone@gmail.com",
    upi: "userone@upi"

}




