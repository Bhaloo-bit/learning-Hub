const myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// const newnums = myNumbers.map ((num) => { return num + 10})
// console.log(newnums);

// const newNums = []

// myNumbers.forEach( (MyNumbers) => {
//     numb = MyNumbers + 10
//     newNums.push( numb )
// })
// console.log(newNums);

// const newNums = myNumbers
//     .map( (num) => (num * 10) + 1 )
//     // .map( (num) => num + 1)

// console.log(newNums);

const myNumbs = [1, 2, 3]

// const myTotal = myNumbs.reduce( function (acc, curval){
//      console.log(`acc: ${acc} and curval: ${curval}`);
//     return acc + curval
// }, 3)

const myTotal = myNumbs.reduce( (acc, curval) => acc + curval, 0)
console.log(myTotal);

const shoppingCart = [
    {
        itemName: "js course",
        price: 2999
    },
    {
        itemName: "py course",
        price: 999
    },
    {
        itemName: "mobile dev course",
        price: 5999
    },
    {
        itemName: "data science course",
        price: 12999
    },
    {
        itemName: "tailwind course",
        price: 599
    }
]

// shoppingCart.reduce ((item) =>(),0)

// const Totalamu = shoppingCart.reduce(function(acc, item) {
//     return acc + item.price

// },0)
// console.log(Totalamu);

const Totalamu = shoppingCart.reduce((acc, item) => acc + item.price, 0)
console.log(Totalamu);