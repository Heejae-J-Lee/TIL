### if 구문
```swift
// swift 조건은 아래와 같이 표현가능
// 조건절을 ()로 묶는 것은 선택 사항
let a: Int = 3
if a == 4 {

} else if a == 5 {

} else {

}
```
### switch 구문
```swift
let a: Int = 5
switch a {
    case 0:
        print(a)
    case 1...10:
        print("10이하 상수")
        // fallthrough 키워드를 사용하면 다음 case도 실행됨
        fallthrough
    // 아래와 같이 다양한 조건으로 넣을 수도 있음
    case Int.min..<0, 101..<Int.max:
        print("TT")
        break
    // @unknown case _:
    // 열거형의 경우 unknown 속성을 통해 예상치 못한 케이스가 발생할 경우 컴파일러 경고를 띄울 수 있다.
    //    print("wildcard 문자 _를 통해 모든 케이스에 대응도 가능하다")
    default:
        print("모든 케이스에 맞지 않을 경우")
    

}
```
### 반복문
```swift
for a in sqeunce_item {
    // code
}
```
### while문
```swift
var cnt: Int = 0

while cnt < 10 {
    cnt = cnt + 1
}

// repeat-while 문
// 일단 최초 1회 실행 후 그 다음에 while문 반복을 실행한다.
// do-while문과 동일
repeat {

} while cnt < 10
```
### 구문 이름표
```swift
// 반복문 구문에는 이름표를 할당할 수 있다.
// 구문 이름표를 통해 제어 키워드의 범위를 보다 명확하게 명시할 수 있다.

var numbers: [Int] = [1,2,3,4]

numbersLoop: for number in numbers {
    if number == 2 {
        print("2")
        continue numbersLoop
    }
    InfiniteLoop: while True {
        print("무한루프에 빠졌습니다.")
        break InfiniteLoop
    }
}
```