// to run this file, use: go run go_notes.go

// i++, i+=1 SUPPORTED; ++i NOT SUPPORTED
// go DOES NOT have "of", "in" keyword like in JS

package main

import (
	"fmt"
	"math"
	"slices"
	"sort"
	"strings"
)

func main() {
	here()
}

func here() {
	// ========== Variables =========
	var x int = 10
	var y string = "Hello"
	var z bool = true

	// or,
	x1, y1, z1 := 10, "Hello", true

	fmt.Println(x, y, z)
	// output: 10 Hello true

	fmt.Println(x1, y1, z1)
	// output: 10 Hello true

	// MIN and MAX
	min := min(x, x1)
	max := max(x, x1)

	// absolute value
	abs := math.Abs(float64(x))

	// remainder
	remainder := x % x1

	// power
	result := math.Pow(float64(x), float64(x1))

	// to find mid (useful in binary search)
	mid := x + (x1 - x) // 2

	// round
	rounded := math.Round(float64(x))

	// ceil
	ceiled := math.Ceil(float64(x))

	// floor
	floored := math.Floor(float64(x))

	fmt.Println(min, max, abs, remainder, result, mid, rounded, ceiled, floored)

	
	// ========== Array =========
	array := []string{"a", "b", "c"}

	// basic operations
	array = append(array, "d")
	fmt.Println(array)
	// output: [a b c d]

	// pop and slice
	popped := array[len(array)-1]
	array = array[:len(array)-1]
	fmt.Println(popped, array)
	// output: d [a b c]

	// for loop
	for i := 0; i < len(array); i++ {
		fmt.Println(array[i])
	}
	// output: a
	//         b
	//         c

    for i, x := range(array) {
		if x == "b" {
			fmt.Println("Found b")
		} else if x != "c" {
			fmt.Println("Found a")
		} else {
			fmt.Println("Found c")
		}
		fmt.Println(i, x)
	}
	// output: 0 a
	//         1 b
	//         2 c

	for _, x := range(array) {
		fmt.Println(x)
	}
	// output: a
	//         b
	//         c
	
	for i := range(array) {
		fmt.Println(i)
	}
	// output: 0
	//         1
	//         2

	// check if element is in array
	if slices.Contains(array, "a") {
		fmt.Println("Found a")
	}

	// reverse array
	i, j := 0, len(array)-1
	for i < j {
		array[i], array[j] = array[j], array[i]
		i++
		j--
	}
	fmt.Println(array)
	// output: [c b a]

	// sort the array
	arrayl := []int{45, 23, 12, 67, 89}
	sort.Slice(arrayl, func(a, b int) bool {
		return a < b
	})
	fmt.Println(arrayl)
	// output: [12 23 45 67 89]

	// sort the array interval
	array_interval := [][]int{{1, 2}, {3, 4}, {5, 6}}
	sort.Slice(array_interval, func(a, b int) bool {
		return array_interval[a][0] < array_interval[b][0]
	})
	fmt.Println(array_interval)
	// output: [[1 2] [3 4] [5 6]]


	// ========== Dictionary ========== 
	// An empty map
	// map[Key_Type]Value_Type{}

	// Map with key-value pairs
	// map[Key_Type]Value_Type{key1: value1, ..., keyN: valueN}

	dictionary := map[string]int{"a": 1, "b": 2, "c": 3}

	// basic operations
	dictionary["d"] = 4
	fmt.Println(dictionary)
	// output: {a:1 b:2 c:3 d:4}

	delete(dictionary, "a")
	fmt.Println(dictionary)
	// output: {b:2 c:3 d:4}

	// go automatically sets value to 0 if key is not found
	dictionary["z"] = dictionary["z"] + 1
	fmt.Println(dictionary)
	// output: {b:2 c:3 d:4 z:1}

	// check if key is in dictionary
	if value, ok := dictionary["a"]; ok {
		fmt.Println("Found a", value)
	}
	// output: Found a 1

	// for loop
	for key, value := range dictionary {
		fmt.Println(key, value)
	}
	// output: z 1
	//         b 2
	//         c 3
	//         d 4
	// Note: order of output is not guaranteed

	for key := range dictionary {
		fmt.Println(key)
	}
	// output: z
	//         b
	//         c
	//         d
	// Note: order of output is not guaranteed

	for _, value := range dictionary {
		fmt.Println(value)
	}
	// output: 4
	//         1
	//         2
	//         3
	// Note: order of output is not guaranteed

	
	// ========== Set: go DOES NOT have it; use map[T]struct{} ========== 
	set := map[string]struct{}{"a": {}, "b": {}, "c": {}}
	yok_array := []string{"x", "y", "z"}

	// basic operations and for loop
	for _, x := range(yok_array) {
		set[x] = struct{}{}
	}

	fmt.Println(set)
	// output: map[a:{} b:{} c:{} x:{} y:{} z:{}]

	delete(set, "a")
	fmt.Println(set)
	// output: map[b:{} c:{} x:{} y:{} z:{}]

	for _, x := range(yok_array) {
		delete(set, x)
	}

	fmt.Println(set)
	// output: map[b:{} c:{}]

	for x := range set {
		fmt.Println(x)
	}
	// output: b
	//         c

	// check if element is in set
	if _, ok := set["a"]; ok {
		fmt.Println("Found a")
	}
	// output: Found a	


	// ========== String ========== 
	stringg := "abc"

	// for loop
	for _, x := range(stringg) {
		fmt.Println(string(x)) // Convert rune to string
	}
	// output: a
	//         b
	//         c

	// ⚠️ otherwise,
	for _, x := range(stringg) {
		fmt.Println(x)
	}
	// output: 97
	//         98
	//         99

	new_string := "xyz"
	fmt.Println(stringg + new_string)
	// output: abcxyz

	for _, x := range(new_string) {
		stringg += string(x)
	}
	fmt.Println(stringg)
	// output: abcxyz

	// reverse string (string -> rune -> reverse -> string)
	// https://claude.ai/chat/5ab732fc-1f73-4cb2-987a-c66daab037bd
	not_reversed_string := "abc"
	runes := []rune(not_reversed_string)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	fmt.Println(string(runes))
	// output: cba

	// array to string
	array_to := []string{"a", "b", "c"}
	fmt.Println(strings.Join(array_to, ""))
	// output: abc


	// ========== Conversations string to array to dictionary count ========== 

	string_g := "abcaakc"
	array_g := strings.Split(string_g, "")
	dict_g := map[string]int{}

	for _, x := range(array_g) {
		dict_g[x] = dict_g[x] + 1
	}

	fmt.Println(dict_g)
	// output: map[a:3 b:1 c:2]


	// ========== Functions ========== 

	// func add(a, b int) int {
	// 	return a + b
	// }
	// fmt.Println(add(1, 2))
	// ⚠️ Error: Function declarations cannot be nested inside other functions in Go.
	// nested functions possible in python, js

	// lambda function
	add_lambda := func(a, b int) int {
		return a + b
	}
	fmt.Println(add_lambda(1, 2))
	// output: 3


	// ========== Class ========== 
	type Person struct {
		Name string
		Age int
	}

	hehe := func (p Person) string {
		return p.Name + " " + string(p.Age)
	}
	fmt.Println(hehe(Person{Name: "John", Age: 30}))
	// output: John 30

}
