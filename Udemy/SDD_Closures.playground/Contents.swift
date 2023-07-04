import UIKit

func calculator (n1: Int, n2: Int, operation: (Int, Int) -> Int) -> Int {
    return operation(n1, n2)
}

func add (no1: Int, no2: Int ) -> Int {
    return no1 + no2
}

func multiply (no1: Int, no2: Int) -> Int {
    return no1 * no2
}

calculator(n1: 2, n2: 3, operation: add)
calculator(n1: 2, n2: 3, operation: multiply)

// Closure :
// 코드를 간결하게 만들 수 있지만, 가독성 면에서는 다소 트레이드 오프가 발생할 수 있다
// 간결함과 가독성 사이의 균형을 잘 맞춰야 함
/*
 { (parameters) -> return type in
    statement
 }
 */

calculator(n1: 2, n2: 3, operation: { (no1, no2) in no1 * no2 })
calculator(n1: 2, n2: 3, operation: { $0 * $1 })


// Map :

let array = [6,3,2,1,5,6]

func addOne(n1: Int) -> Int {
    return n1 + 1
}

array.map(addOne)

array.map({ (n1: Int) -> Int in n1 + 1 })

array.map({ (n1) in n1 + 1 })

array.map({$0 + 1})

let newArray = array.map{"\($0)"}
