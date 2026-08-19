const coding =["js","rubi","java", "python","cpp"]
// coding.forEach(function (items) {
//     console.log(items);
// } )

coding.forEach(  (val) => {
    console.log(val);
} )



const myCoding = [
    {
        languageName: "Javascripts",
        languageFileName: "Js",
    },
    {
        languageName : "Java",
        languageFileName : "Java",
    },
    {
        languageName:"python",
        languageFileName:"py",
    }
]

myCoding.forEach( (items) => {
    console.log(items.languageName);
} )