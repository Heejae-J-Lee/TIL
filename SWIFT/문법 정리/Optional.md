### Optional 
스위프트에서는 optional 변수 혹은 상수가 아니면 nil 을 할당할 수 없다.</br>
옵셔널의 의미는 해당 변수 혹은 상수에는 값이 없을 수 있음을 의미한다. </br>
일반적으로 데이터 타입 뒤에 ?를 붙여 사용하며, Optional<데이터타입>과 같이 사용할 수도 있다.</br>
 ※nil과 0 혹은 빈 문자열 ""은 다르다!

 옵셔널을 사용하는 상황 예시 :
</br>
전달인자의 값이 잘못되어 리턴이 없을 경우, 간단히 nil을 리턴

오류 발생
 ```swift
 var myNum: Int = 3
 myNum = nil // error!
  ```

옵셔널 사용
```swift
 var myNum: Int? = 3
 myNum = nil

 // 옵셔널은 switch 문을 사용하여 값을 확인할 수도 있다.
 switch myNum {
    case .none:
        print("nil")             // nil일 경우의 리턴
    case .some(let value):
        print("\(value)")   // 값이 있을 경우 리턴
    }
 }
  ```

### Optional Unwrapping
#### Forced unwrapping
가장 간단하며 Runtime error가 발생항 확률이 높아 위험한 방법이다.
옵셔널 변수 뒤에 !를 붙이면 강제로 unwrapping 하여 반환하지만, 만약 해당 변수가 nil의 값을 가지고 있다면 런타임 오류가 발생한다.
```swift
 var myNum: Int? = 3
 myNum!    // 3
 myNum = nil
 myNum!   // Runtime Error가 발생하여 프로그램이 강제 종료된다.

```
#### Optional binding
옵셔널에 값이 있다면 추출한 값을 일정 블록 안에서 사용할 수 있는 상수나 변수로 할당하여 사용한다.
if while guard-else 등의 구문과 결합하여 사용할 수도 있다.
```swift
 var myNum: Int? = 3
 
 // example 1
if let Num = myNum {
    print(Num)    // 3
    Num = 4
    print(Num)    // 4 Num은 변수이므로 내부에서 변경도 가능하다.
} else {
    print("nil")    // myNum이 nil일 경우 nil을 프린트한다.
}


 // example 2
```
#### Implicitly Unwrapped Optionals
때때로 nil을 할당하지만, 옵셔널 바인딩으로 매번 값을 추출하고 싶지 않거나 nil 때문에 런타임 오류가 발생하지 않을 것 같을때는 Implicitly Unwrapped Optionals을 사용할 수 있다.</br>
이 경우 nil을 할당할 수는 있지만, nil이 할당되어 있을 때 접근을 시도하면 런타임 오류가 발생한다.
```swift
var myName: String! = "Heejae"
print(myName)    // Heejae
myName = nil

// 옵셔널 바인딩 또한 사용 가능
if let name = myName {
    print("My Name is \(name)")
} else {
    print("myName == nil")
}

myName.isEmpty  // 오류 발생
```
