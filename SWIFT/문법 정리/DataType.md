### 변수와 상수
* 변수  
```swift
/* 
swift에서는 아래와 같이 변수를 선언할 수 있다.
*/
var name: String = "Heejae"
var age: Int = 29
var job = "SW Engineer"  // Type Inference
var height = 170.1

/* 
아래와 같이 변수 값을 변경하고, 콘솔창에 출력할 수 있다.
*/
age = 20
job = "IOS Developer"
print("Greeting, My name is \(name), \(age) years old. I am \(job). Thank you!") // String Interpolation \(variable)
```  
  
* 상수  
```swift
let name: String = "Heejae"
var age: Int = 29
var job = "SW Engineer"  // Type Inference
let height = 170.1
age = 30
job = "IOS Programmer"
name = "Jaehee"  // 상수의 경우 값을 변경할 수 없기 때문에 error 가 발생한다.
print("Greeting, My name is \(name), \(age) years old. I am \(job). Thank you!") // String Interpolation \(variable)
```  
</br></bre>
### Data Type
> Swift의 모든 Data Type은 카멜 케이스를 사용한다.  
> ex) Int, UInt, Bool, Float, Double, Character, String, Any, AnyObject, nil
  
* Int, UInt
```swift
// Int, UInt 예제
var integer: Int = -100
var unsignedInteger: UInt = 50 // UInt 형은 음수값 사용 불가
print("Int 최댓값 : \(Int.max), Int 최솟값 : \(Int.min)")
print("UInt 최댓값 : \(UInt.mas), UInt 최솟값 : \(UInt.min)")
let largeInteger: Int64 = Int64.max
let smallUnsignedInteger: UInt8.max

let tooLarge: Int = Int.max + 1 // error : Int 형의 최댓값을 초과
let cannotBeNegative: UInt = -5 // error : UInt 형은 음수값을 가질 수 없음
integer = unsignedInteger       // error : Int 와 UInt형은 다른 타입임
integer = Int(unsignedInteger)  // Type Casting을 통해 UInt 값을 Int에 할당할 수 있음
/*
C language와 동일하게 다음과 같은 prefix를 사용하여 진수별로 표현이 가능하다.
Decimal : (non-prefix)
Hexadecimal : 0x
Oxtal : 0o
Binary : 0b
*/
let dex: Int = 29
let hex: Int = 0x1B    // 29
let octal: Int = 0o35  // 29
let bin: Int = 0b11101 // 29
```
* Bool (Boolean)
```swift
// Bool Type은 true와 false 두개의 값을 가질 수 있음
var boolean: Bool = true
boolean.toggle()  // true -> false로 값 반전
```
* Float, Double
```swift
// 실수 타입 Float, Double
// Float : 32 bit, Double : 64 bit
var floatValue: Float = 1234567890.1 // float 로는 표현할 수 없음 (정확도 저하)
var doubleValue: Double = 1234567890.1 // 하지만 Double로는 가능하다

/*
10 진수, 16진수의 경우 다음과 같이 확장 표현이 가능하다.
(10진수) 5e3 = 5 * 1000
(10진수) 1.2E-2 = 0.012
(16진수) 0XaP-2 = 10 * (1/4) = 2.5
(16진수) 0XAp3 = 10 * (8) = 80
*/
```
* Character
```swift
// swift 는 Unicode 9를 사용한다
let alphabetA: Character = "a"

// 유니코드 문자도 사용가능
let commandCharacter: Character = "★"

// 심지어 한글 변수 명도 지원한다. 물론 이렇게 사용하는 경우는 드뭄
let 변수명: Character = "ㄱ"
```
* String
```swift
// 상수로 된 문자열은 변경이 불가
let name: String = "Heejae"

// Initializer를 통해 빈 문자열 생성 가능
var introduce: String = String()

// method 1. append()
introduce.append("제 이름은 ")

// '+' 연산자를 통해 동일한 로직을 짤 수 있다.
introduce = introduce + name + "입니다"
introduce += "!!!"

// method 2. hasPrefix(), hasSuffix()
// 접두사, 접미어 확인 가능
var myString: String = "SuperHeejaeUltra"
myString.hasPrefix("Super") // true
myString.hasPrefix("Ultra") // false
myString.hasSuffix("Ultra") // true
myString.hasSuffix("Super") // false

// method 3. 대소문자 변환
var convertString: String = "Heejae"
convertString.uppercased()
convertString                // HEEJAE
convertString.lowercased()
convertString                // heejae

// property 1. count
// 글자 수 확인 가능
introduce.count

// property 2. isEmpty
// 빈 문자열인지 확인

//  Unicode 스칼라 값을 사용할 수도 있다.
let unicodeScalarValue: String = "\u{2665}"

// 아래와 같은 방식으로 여러줄의 문자열을 할당할 수도 있다
let multiLineString: String = """
이런 방식으로 여러줄의 스트링을
직접적으로 변수 혹은 상수로 할당할 수가 있습니다.
큰 따옴표의 경우 내려쓰기로 사용해야 합니다.
"""
```
* Any, AnyObject, nil
```swift
// Any 변수에는 어떤 형태의 값도 할당 가능하다.
// 다만 Any 변수의 경우 에러의 위험성을 증대시키므로 사용을 지양하는 것이 좋음
// 타입은 될 수 있다면 명시할 것
var AnyVariable: Any = "any"
AnyVariable = 33
AnyVariable = true

// AnyObject의 경우 클래스의 인스턴스 만을 할당할 수 있는 변수형이다.
// nil 의 경우 값이 없음을 의미하는 키워드이다.
// 값이 없음 == 비어있음
// nil 인 변수에 접근할 경우 Null Point Exception 과 같은 에러에 직면할 수도 있다.
```

### Type Inference
변수나 상수 선언 시 타입을 명시하지 않아도 컴파일러가 할당된 값을 기준으로 변수 및 상수 타입을 결정하는 것을 타입 추론이라고 한다.
```swift
var number = 3

number = "삼" // 에러가 발생한다
```

### Type Alias 
이미 존재하는 데이터 타입에 임의의 다른 이름을 부여할 수 있다.
```swift
typealias MyNumber = Int
typealias NewNumber = Int

let Num1: MyNumber = 3
var Num2: NewNumber = 33

Num2 = Num1    // 결국은 같은 타입으로 취급
```

### Tuple
지정된 데이터의 묶음  
튜플에 포함된 데이터의 개수 제한은 없다
```swift
var info: (String, Int, Double) = ("Heejae", 29, 170.1)

print ("이름 \(person.0) 나이는 \(person.1) 키는 \(person.2)")

// 각 데이터에 키워드를 지정할 수도 있다.

var otherInfo: (name: String, age: Int, height: Double) = ("Minsu", 33, 180.1)

print ("이름 \(otherInfo.name) 나이는 \(otherInfo.age) 키는 \(otherInfo.2)")


// type alias 와 함께 사용도 가능하다
typealias PersonTuple = (name: String, age: Int, height: Double)
```

### Collection Type  
- Array
  - 데이터를 순서대로 저장하는 컬렉션 타입
  - ```swift
    var lists: Array<String> = ["Pizza", "Chicken", "Jokbal"]
    // 동일한 표현 (축약형)
    var lists: [String] = ["Pizza", "Chicken", "Jokbal"]

    var emptyArray: [Any] = [Any]()
    var emptyArray: [Any] = Array<Any>()
    var emptyArray: [Any] = []

    // property .isEmpty .count
    emptyArray.isEmpty    // true
    list.count     // 3

    // 변경 
    lists[2] = "Ramyen"

    // 추가 
    lists.append("Bossam")
    lists.append(contentsOf: ["Fruits", "IceCream"])     // 여러개를 한꺼번에 추가도 가능

    // method insert() at: 위치에 데이터 추가
    lists.insert("Gopchang", at:2)
    lists[2]    // "Gopchang"
    lists.index(of: "Gopchang")    // 2
    lists.index(of: "GgaGga")    // 없으면 nil

    lists.first    // "Pizza"
    lists.last     // "IceCream"

    // 데이터 원소의 제거
    lists.removeFirst()    // "Pizza"
    lists.removeLast()     // "IceCream"
    names.remove(at: 2)    // "Gopchang"
    lists[1 ... 3]         // ["Gopchang", "Raryen", "Bossam"]

    // 범위를 변경할수도 있다
    lists[1 ... 3] = ["A", "B", "C"]
    ```
- Dictionary
  - 순서 없이 키와 값의 쌍으로 이루어진 컬렉션 타입
  - 키는 유일한 값이어야한다.
  - 없는 키로 접근해도 에러를 발생시키진 않는다. (nil을 반환)
  - ```swift
    var number: [String: Int] = [String: Int]()

    // typealias 사용 가능
    typealias StringIntDictionary = [String: Int]

    // 키와 값 쌍만 제대로 명시하면 [:] 로도 선언 가능
    var number: [String: Int] = [:]

    number.isEmpty    // true
    number.count      // 0

    number["일"] = 1

    number["일"]      // 1
    number["이"]      // nil

    number["일"] = 2  // 변경 가능
    number["진짜일"] = 1 // 추가

    // 삭제
    number.removeValue(forKey: "일")  // 2
    number.removeValue(forKey: "일")  // nil

    // 기본값 설정
    number["삼", default: 0]  // 3
    ```
- Set
  - 같은 타입의 데이터를 순서 없이 저장
  - 세트는 중복된 값이 존재하지 않는다
  - 배열과 다르게 축약형이 존재하지 않음
  - ```swift
    var names: Set<String> = Set<String>()
    var names: Set<String> = []

    var names: Set<String> = ["한놈", "두시기", "석삼"]
    names.isEmpty    // false
    names.count      // 3

    // 요소 추가
    names.insert("너구리")

    // 요소 삭제
    names.remove("한놈")    // "한놈"
    names.remove("한놈")    // nil

    let pokemon: Set<String> = ["피카츄", "라이츄", "파이리"]
    let digimon: Set<String> = ["아구몬", "파피몬", "파닥몬", "피카츄"]

    // 교집합
    pokemon.intersection(digimon)    // {"피카츄"}

    // 여집합
    pokemon.symmetricDifference(digimon)    // {"라이츄", "파이리", "아구몬", "파피몬", "파닥몬"}

    // 합집합
    pokemon.union(digimon)  // {"피카츄", "라이츄", "파이리", "아구몬", "파피몬", "파닥몬"}

    // 차집합
    pokemon.subtracting(digimon)  // {"라이츄", "파이리"}

    // sorting
    pokemon.sorted()    // ["라이츄", "피카츄", "파이리"]

    // 배타적 여부 .isDisjoint(with:) : 겹치는게 하나도 없으면 true
    // 부분집합 (포함 여부) .isSubset(of:)
    // 전체집합 .isSuperSet(of:)
    ```

### 열거형
열거형 : 연관된 항목들을 묶어서 표현할 수 있는 타입   사용하는 경우

열거형을 사용하는 경우

- 정해진 값 외에는 입력받고 싶지 않을 때
- 예상된 입력 값이 한정되어 있을 때

```swift 
// 스위프트의 열거형은 enum으로 표현이 가능하다;
// 모든 케이스는 ,로 구분하여 한줄로도 표현이 가능하다.
enum Fruit {
  case apple
  case banana
  case orange
  case pineapple
  case watermelon
}

var myFavoriteFruit: Fruit = Fruit.orange
var yourFavoriteFruit: Fruit = .apple

myFavoriteFruit: Fruit = .watermelon

// 열거형은 raw value 도 가질 수 있다.
enum Fruit: String {
  case apple = "사과"
  case banana = "바나나"
  case orange = "오랜지"
  case pineapple = "파인애플"
  case watermelon = "수박"
}
let summerFruit: Fruit = .watermelon
summerFruit.rawValue    // "수박"

// 일부의 케이스만 raw Value를 줄 수도 있다.
enum Number: Int {
  case one
  case two
  case three = 55
}
Number.one.rawValue    // 1
Number.two.rawValue    // 2
Number.three.rawValue  // 55

// rawValue로 열거형 값을 가져올 수도 있다.
Number(rawValue: 55)    // three
Number(rawValue: 3)     // nil

// 다음과 같이 연관 값을 줄 수도 있음
enum Hogwarts {
  case Gryffindor(belong: String, weapon: String)
  case Hufflepuff
  case Ravenclaw
  case Slytherin(blood: String)
}
var HarryPotter: Hogwarts = Hogwarts.Gryffindor(belong: "불사조", weapon: "딱총나무")
HarryPotter = .Slytherin(blood: "순혈")

// 열거형 항목 순회
// rawValue가 없는 경우;
enum Fruit {
  case apple
  case banana
  case orange
  case pineapple
  case watermelon
}

let allCases: [Fruit] = Fruit.allCases // [Fruit.apple, Fruit.banana, ..., Fruit.watermelon]

// rawValue 가 있는 경우;
// 프로토콜 CaseIterable 을 추가
enum Fruit: String, CaseIterable {
  case apple = "사과"
  case banana = "바나나"
  case orange = "오랜지"
  case pineapple = "파인애플"
  case watermelon = "수박"
}
let allCases: [Fruit] = Fruit.allCases // [Fruit.apple, Fruit.banana, ..., Fruit.watermelon]
/*
  특정 플랫폼 별로 case를 사용할 필요가 있을 때에는, @available 속성을 사용해야하며,
  열거형이 연관값을 갖는 경우는 allCases 프로퍼티를 사용할 수 없으니 주의하여야한다;
  사용이 필요할 경우는 직접 구현이 필요하다.
*/

// 순환 열거형
// 열거형의 연관값이 자기 자신의 값이고자 할 경우,
// indirect 키워드를 사용하여 순환 열거형을 사용할 수 있다.

// 특정 케이스에만 사용
enum ArithmeticExpression {
  case number(Int)
  indirect case addition(ArithmeticExpression, ArithmeticExpression)
  indirect case multiplication(ArithmeticExpression, ArithmeticExpression)
}

// 모든 케이스에 대하여 사용할 경우
indirect enum ArithmeticExpression {
  case number(Int)
  case addition(ArithmeticExpression, ArithmeticExpression)
  case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```
