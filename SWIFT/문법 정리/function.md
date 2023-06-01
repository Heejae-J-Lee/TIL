### 매서드와 함수
- 매서드
  - 구조체, 클래스, 열거형 등 특정 타입에 연관되어 사용하는 함수
- 함수
  - 모듈 전체에서 전역적으로 사용할 수 있는 함수

```swift
// 함수의 정의
/*
function function_name(parameter...) -> return_type {
    content
    return value  
}

return_type을 명시하지 않거나, Void를 사용하면 리턴값이 없는 함수가 된다.
*/

// swift에는 또한 전달인자 레이블이 존재한다.
// 아래에서는 from, to
func greeting(from myname:String, to yourname: String) -> String {
    return "Hello, \(yourname). i am\(myname)!"
}

print(greeting(from:"Ho", to:"Hae"))

// wildcard 식별자 _ 를 사용하여 매개변수 이름을 생략할 수도 있다.
func greeting(_ myname:String, _ yourname: String) -> String {
    return "Hello, \(yourname). i am\(myname)!"
}

print(greeting("Ho", "Hae"))

// 전달인자 레이블을 사용하여, 같은 함수를 중복정의(overload) 할 수 있다.
// 위의 두 함수

// 아래와 같이 사용 시 매개변수 기본값 정의 가능
func numbering(_ number: Int = 3) -> String {
    return "my number is \(number)."
}

print(numbering())

// 가변 매개변수를 사용하면 매개변수의 개수를 몰라도 정의 할 수 있다.
func fruit(fruit names: String...) -> Int{
    var count: Int = 0

    for fruit in names {
        count += 1
    }
    return count
}

fruit("apple", "pineapple", "orange")    // 3

// inout 매개변수 사용
// inout 은 c의 포인터 개념을 생각하면 됨
// 매개변수 기본값을 가질 수 없다
var numbers: Int = [1,2,3]

func nonReferenceParameter(_ arr: [Int]) {
    var copiedArr: [Int] = arr
    copiedArr[1] = 2
}

func ReferenceParameter(_ arr: [Int]) {
    arr[1] = 2
}

nonReferenceParameter(numbers)
print(numbers[1])  // 1

ReferenceParameter(numbers)
print(numbers[1])  // 2

// 함수 타입은 일급 객체이므로 하나의 데이터 타입 처럼 사용할 수 있다.
typealias CalculateTwoInts = (Int, Int) -> Int

func addTwoInts(_ a: Int, _ b: Int) -> Int {
    return a+b
}

func multiplyTwoInts(_ a: Int, _ b: Int) -> Int {
    return a+b
}
// 함수포인터와 같은 느낌으로 아래와 같은 방식으로도 쓸 수 있다.
// 물론 함수포인터는 아니다! 일급 객체이다!
var mathFunction : CalculateTwoInts = addTwoInts
var mathFunction : CalculateTwoInts = multiplyTwoInt

func selectFunction(_ a: Bool) -> CalcuateTwoInt {
    return a? addTwoInts : multiplyTwoInt
}

// swift는 데이터 함수의 중첩이 가능하다.
// 함수안의 함수, 클래스안의 클래스 등...!
// 상상도 못한 중첩이 가능하다
typealias MoveFunc = (Int) -> Int

func functionForMove(_ shouldGoLeft: Bool) -> MoveFunc {
    func goRight(_ currentPosition: Int) -> Int{
        return currentPosition + 1
    }
    func goLeft(_ currentPosition: Int) -> Int{
        return currentPosition - 1
    }

    return shouldGoLeft ? goLeft:goRight
}

// 비반환 함수 / 비반환 매서드
// 종료되지 않는 함수
// error raise, 중대한 오류 보고 들의 역할을 하고 프로세스를 종료하는 함수
// 반환 타입을 Never로 명시함
// 어디서든 호출이 가능, guard-else 구문에서도!
func crashAndBurn() -> Never {
    fatalError("Error occurred!")
}

crashAndBurn()

// 반환값을 무시할 수 있는 함수
// @discardableResult 선언 속성을 사용하면 된다.
func somethingthat(_ something: String) -> String {
    return something
}

somethingthat("what")  // 반환값을 사용하지 않으므로 컴파일러는 경고를 보낼 수 있음

@discardableResult func discardableResultsomethingthat(_ something: String) -> String {
    return something
}
discardableResultsomethingthat("what") // 반환값을 사용하지 않지만 컴파일러는 경고하지 않는다.

```