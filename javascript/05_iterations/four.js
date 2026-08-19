const myObject = {
    js : 'Javascripts',
    rb :'Ruby',
    cpp: 'c++',
    swift: "swift by apple"
}

// for (const key in myObject) {
//     console.log(`${key} shortcut is for ${myObject[key]}`)
// }
// for (const value in myObject) {
//     console.log(myObject[value])
// }

const programing = ["js","rb", "py", "java", 'cpp']
for (const key in programing) {
    console.log(programing[key]);
}