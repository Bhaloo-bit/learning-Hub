//  singleton
// obejct.create
 
// object literals 

const mySym = Symbol("mykey")

const JsUser = {
    name : "hitesh",
    [mySym] : "mykey",
    "full name ": "hitesh choudhary",
    age : 18,
    location: "delhi",
    email : "bhaloo@gmail.com",
    isLoggesIn: false ,
    lastloginDays: ["monday","saturday"]

}

// console.log(JsUser.email)
// console.log(JsUser["location"])
// console.log(JsUser["full name "])
// console.log(JsUser[mySym]);

JsUser.email = "bhalobit@gmail.com"
// Object.freeze(JsUser)
// console.log(JsUser);

// JsUser.greeting = function(){
//     console.log("hello JsUser");
// }
// // console.log(JsUser.greeting);

// JsUser.greetingTwo = function(){
//     console.log(`hello js user, ${this.name}`);
// }
// console.log(JsUser.greeting());
// console.log(JsUser.greetingTwo());

JsUser.greeting = function() {
    console.log("Hello JS User")
}
console.log(JsUser.greeting());

JsUser.greetingTwo = function(){
    console.log(`Hello JsUser ${this["full name "]}`)
}
console.log(JsUser.greetingTwo());