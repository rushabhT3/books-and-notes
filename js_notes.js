// to run this file, use node js_notes.js

// ++i, i++, i+=1 ALL SUPPORTED

// ⚠️ array and set kind of like map index: value
for (let x in set) {
    console.log(x)
}
// output: 0
//         1
//         2

// clean code notes:
// https://github.com/ryanmcdermott/clean-code-javascript?tab=readme-ov-file
// https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript


// ========= variables =========

let x = 0, y = 89, z = 80
// or, 
let x1, y1, z1
x1 = y1 = z1 = 0

// ⚠️ NOT SUPPORTED: let x = y = z = 0

// MIN and MAX
let min = Math.min(x, y, z)
let max = Math.max(x, y, z)

// absolute value
let abs = Math.abs(x)

// round
let round = Math.round(x)

// ceil
let ceil = Math.ceil(x)

// floor
let floor = Math.floor(x)

// remainder
let remainder = x % y

// power
let result = x ** 2

// to find mid (useful in binary search)
let mid = x + Math.floor((y - x) / 2)


// ========== Array ==========

const array = ["a", "b", "c"]

// basic operations

// empty array check
if (array.length == 0) {
    console.log("Array is empty")
}
// or,
if (!array.length) {
    console.log("Array is empty")
}
// ⚠️ !array is NOT correct way to check if array is empty as it will always return false

array.push("d")
console.log(array)
// output: ["a", "b", "c", "d"]

array.pop()
console.log(array)
// output: ["a", "b", "c"]

// slice
console.log(array.slice())
// output: ["a", "b", "c"]

console.log(array.slice(0, 2))
// output: ["a", "b"]

console.log(array.slice(1))
// output: ["b", "c"]

// intialize with all zero elements
let array_of_size_5 = new Array(5).fill(0)
console.log(array_of_size_5)
// output: [0, 0, 0, 0, 0]

// for loop
for (let i = 0; i < array.length; i++) {
    console.log(array[i])
}
// output: a
//         b
//         c

for (let x of array) {
    console.log(x)
}
// output: a
//         b
//         c

for (let [i, x] of array.entries()) {
    console.log(i, x)
}
// output: 0 a
//         1 b
//         2 c

for (let i in array) {
    console.log(i)
}
// output: 0
//         1
//         2

// check if element is in array
if (array.includes("a")) {
    console.log("Found a")
}

// reverse array
let i = 0, j = array.length - 1

while (i < j) {
    [array[i], array[j]] = [array[j], array[i]]
    i++
    j--
}

console.log(array)
// output: ["c", "b", "a"]

// sort the array
// e.g. Sort by start time in intervals = [[start, end], ...]
intervals.sort((a, b) => a[0] - b[0]);


// ========== Dictionary ==========

const dictionary = {"a": 1, "b": 2, "c": 3}

// basic operations
dictionary["d"] = 4
console.log(dictionary)
// output: {"a": 1, "b": 2, "c": 3, "d": 4}

delete dictionary["a"]
console.log(dictionary)
// output: {"b": 2, "c": 3, "d": 4}

dictionary["a"] = (dictionary["a"] || 0) + 1
console.log(dictionary)
// output: {"b": 2, "c": 3, "d": 4, "a": 1}

// check if key is in dictionary
if ("a" in dictionary) {
    console.log("Found a")
}

// check if key is NOT in dictionary
if (!("a" in dictionary)) {
    console.log("Not found a")
}

// for loop
for (let [key, value] of Object.entries(dictionary)) {
    console.log(key, value)
}
// output: b 2
//         c 3
//         d 4
//         a 1

for (let key of Object.keys(dictionary)) {
    console.log(key)
}
// output: b
//         c
//         d
//         a

for (let value of Object.values(dictionary)) {
    console.log(value)
}
// output: 2
//         3
//         4
//         1

for (let key in dictionary) {
    console.log(key)
}   
// output: b
//         c
//         d
//         a


// ========== Set ==========

const set = new Set(["a", "b", "c"])
// ⚠️ NOT SUPPORTED: const set = {"a", "b", "c"}
const sec_array = ["x", "y", "z"]

// length
let length = set.size
// ⚠️ NOT set.length

// basic operations and for loop
for (let x of sec_array) {
    set.add(x)
}

console.log(set)
// output: Set { 'a', 'b', 'c', 'x', 'y', 'z' }

for (let x of sec_array) {
    set.delete(x)
}

console.log(set)
// output: Set { 'a', 'b', 'c' }

for (let x of set) {
    console.log(x)
}
// output: a
//         b
//         c


// ========== String ==========

const string = "abc"

// change case
console.log(string.toUpperCase()) // ABC
console.log(string.toLowerCase()) // abc

// for loop
for (let x of string) {
    console.log(x)
}
// output: a
//         b
//         c

for (let [i, x] of Array.from(string).entries()) {
    console.log(i, x)
}
// output: 0 a
//         1 b
//         2 c

for (let i in string) {
    console.log(string[i])
}
// output: a
//         b
//         c

const new_string = "xyz"
// string to array
const new_string_array = new_string.split("")

const result_array = [...string, ...new_string_array]
// array to string
console.log(result_array.join(""))
// output: abcxyz

// reverse string
let m = 0, n = string.length - 1

const string_array = string.split("")
while (m < n) {
    [string_array[m], string_array[n]] = [string_array[n], string_array[m]]
    m++
    n--
}
console.log(string_array.join(""))
// output: cba

// or,
console.log(string.split("").reverse().join(""))
// output: cba

// string-literal
console.log(`any string ${string} ${string.length}`)
// output: any string abc 3


// ========== Conversations string to array to dictionary count ==========

string = "abcaakc"
array = string.split("")
dictionary = {}

for (let i = 0; i < array.length; i++) {
    dictionary[array[i]] = (dictionary[array[i]] || 0) + 1
}

console.log(array)
// output: ["a", "b", "c"]

console.log(dictionary)
// output: {a: 3, b: 1, c: 2}


// ========== Functions ==========

function add(a, b) {
    return a + b
}

console.log(add(1, 2))
// output: 3

// lambda function
const add = (a, b) => a + b
console.log(add(1, 2))
// output: 3


// ========== Class ==========

class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    greet() {
        console.log(`Hello, ${this.name}`)
    }
}

const person = new Person("John", 30)
person.greet()
// output: Hello, John

class Student extends Person {
    constructor(name, age, grade) {
        super(name, age)
        this.grade = grade
    }

    greet() {
        console.log(`Hello, ${this.name}. I am in grade ${this.grade}`)
    }
}

const student = new Student("John", 30, "A")
student.greet()
// output: Hello, John. I am in grade A


// ========== Some other useful things ==========

// when input is a list of numbers
const array_input = prompt("Enter a list of numbers separated by spaces").split(" ").map(Number)
console.log(array_input)
// output: [1, 2, 3]


// js methods
let array_js = [1, 2, 3]
array_js = array_js.map(x => x * 2)
console.log(array_js)
// output: [2, 4, 6]

array_js = array_js.filter(x => x % 2 == 0)
console.log(array_js)
// output: [2, 4]

array_js = array_js.sort((a, b) => a - b)
console.log(array_js)
// output: [2, 4]

// ⚠️ array becomes single value
array_js = array_js.reduce((a, b) => a + b)
console.log(array_js)
// output: 6

// replace method with regex
let palindrome = "A man, a plan, a canal: Panama"
palindrome = palindrome.replace(/[^a-z0-9]/g, "")
console.log(palindrome)
// output:AmancanalPanama
// ^ for negation here; g for finding all NOT just first occurrence


