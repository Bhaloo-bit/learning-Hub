//for of 

//["", "", ""]
//[{},{},{}]

const arr = [1, 2, 3, 4, 5]

for (const num  of arr) {
    // console.log(num)
}
const arry = ["my","name","is","bipul","nirala"]

for (const items of arry) {
    // console.log(arry)
}

// Maps

const map = new Map()
map.set('IN',"India")
map.set("USA","United States of america")
map.set("Fr","France")
map.set("IN","India")

// // console.log(map)



const myObjects = {
    'game1': 'NFS',
    'game2':"Spiderman"
}
for (const [key, value] of myObjects) {
    console.log([key, ':-',value])
}    