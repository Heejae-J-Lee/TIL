```swift
// assign
var A: Int = 33

// arithmetic
A = A + 2    // add
A = A - 2    // subs
A = A * 2    // multiply
A = A / 2    // divide
A = A % 2    // moduler

// Comparison
A == 33
A >= 22
A <= 26
A > 20
A < 30 
A != 22
A === B    // same reference
A !== B
A ~ B     // patern match

// Ternary Operation
Question ? A : B    // if true is A; false is B

// Range Operation
A...B    // A to B; include A,B
A..<B    // A to B; include A, not B
A...     // A to ...; include A
...A     // ... to A; include A
..<A     // ... to A; not include A

// Bool Operation
!A   // not A
A && B    // A AND B
A || B   // A OR B

// Bit Operation
~A    // convert bits of A
A & B // bitwise A AND B
A | B // bitwise A OR B
A ^ B // bitwise A XOR B
A >> B // shift
A << B // shift

// Compound Assignment
A += B
A -= B
A *= B
A /= B
A %= B
A <<= N   // shift
A >>= N 
A &= B    // Bitwise AND
A |= B    // Bitwise OR
A ^= B    // Bitwise XOR

// prevent Overflow operation
A = A &+ B // overflow
A = A &- B 
A = A &* B 

// etc
A ?? B  // nil 병합 연산자 A가 nil 이 아니면 A를 nil이면 B를 반환한다
-A      // A의 부호를 변경한다
O!      // 옵셔널 개체 O의 값을 강제로 추출한다
V?      // 옵셔널 개체 V를 안전하게 추출하거나 V가 옵셔널 값임을 표현

// 전위 연산자 구현
prefix operator ** 

prefix func ** (value: Int) -> Int {
    return value * value
}

prefix func ! (value: String) -> Bool {
    return value.isEmpty
}

// 후위 연산자 구현
// 전위 연산자와 후위 연산자를 동시에 사용하게 되면 후위 연산자를 먼저 수행합니다.
postfix operator **

postfix func ** (value: Int) -> Int {
    return value + 10
}

// 중위 연산자 구현
// 우선순위 그룹을 명시해줄 수 있음
precedencegroup 우선순위그룹이름 {
    higherThan: 더 낮은 우선순위 그룹 이름
    lowerThan: 더 높은 우선순위 그룹 이름
    associativity: 결합 방향 (left/right/none)
    assignment: 할당방향 사용 (true/false)
}

infix operator ** : MultiplicationPrecedence

func ** (lhs: String, rhs: String) -> Bool {
    return lhs.contain(rhs)
}

var A: String = "BB"
var B: String = "BBB"
B**A // true
A**B // false

```