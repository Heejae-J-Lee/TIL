### Property
클래스, 구조체 또는 열거형 등에 관련된 값  
크게 아래의 세 종류로 분류할 수 있음
- Stored Property : 인스턴스의 변수 또는 상수
- Computed Property : 특정 연산을 실행한 결과값을 저장
- Type Property : 특정 타입에 사용되는 프로퍼티  

#### Stored Property
클래스 또는 구조체의 인스턴스와 연관된 값을 저장  
내부에서 var와 let 키워드를 통해 정의하여 사용할 수 있다.
초깃값을 설정해 줄 수 있으며, class의 경우 프로퍼티에 맞는 이니셜 라이저를 따로 제공하지 않아서 프로퍼티의 초깃값이 설정되어 있지 않다면 생성시 따로 값을 설정할 필요가 있다.  
다만 프로퍼티를 옵셔널로 설정하면, 생성시 꼭 값을 넣어줄 필요는 없다.
#### Lazy Stored Property
호출이 있어야 값을 초기화(처음 접근할 때)하며, 이 때는 lazy var 키워드를 사용한다.  
잘 사용하면 불필요한 성능저하나 공간 낭비를 줄일 수 있다.

#### Computed Property
실제 값을 저장한다기보다는 특정 상태에 따른 값을 연산하는 프로퍼티  
getter와 setter의 역할을 할 수도 있다.  
이는 매서드로 정의할 수도 있지만, 매서드로 정의할 시 다음의 비교할 만한 부분이 있다.
- 두 개의 매서드로 따로 정의해야하기 때문에 가독성이 저하될 수 있음.
- 다만 연산 프로퍼티는 쓰기 전용 상태로 구현할 수는 없다는 단점도 있다.
```swift
struct CoordinatePoint {
    var x: Int // 저장 프로퍼티
    var y: Int // 저장 프로퍼티  

    var oppositePoint: CoorcdinatePoint {
        // getter
        get {
            return CoordinatePont(x: -x, y: -y)
        }

        // setter
        // 매개변수 opposite는 생략이 가능하다, 대신 그럴 경우 newValue로 매개변수이름을 대신할 수 있다.
        set(opposite) {
            x = -opposite.x
            y = -opposite.y
        }
    }
}
```
#### Property Observers
프로퍼티의 값이 변하는 걸 감시.  
값이 바뀔 때마다 호출되며, 바뀌는 값이 현재와 같더라도 호출된다.
전역 변수와 전역 상수에서도 사용할 수 있지만 lazy stored property에는 사용할 수 없다.  
저장 프로퍼티에 적용할 수 있으며 부모클래스로부터 상속받을 수 있다.
프로퍼티 감시자의 경우 값이 변경되기 전에 호출되는 willSet(전달인자는 변경될 값)과 전달된 이후에 호출되어지는 didSet(전달인자는 변경되기 전의 값)이 있다.  
매개변수의 이름을 따로 지정하지 않을 경우 willSet의 경우에는 newValue,  
didSet의 경우에는 oldValue가 매개변수 이름으로 자동으로 지정된다.
```swift
class Account {
    var credit: Int = 0 {
        willSet {
            print("\(credit) -> \(newValue)")
        }
        didSet {
            print("\(oldValue)->\(credit)")
        }
    }
}
```
#### Type Property 
각각의 인스턴스가 아닌 타입 자체에 속하는 프로퍼티  
- 저장 타입 프로퍼티 : 변수 또는 상수로 선언 가능  </br>
반드시 초깃값을 설정하여야 하며 지연 연산된다.
- 연산 타입 프로퍼티 : 변수로만 선언할 수 있음
```swift
class AClass {
    // 저장 타입 프로퍼티
    static var typeProperty: Int = 0

    var instanceProperty: Int = 0 {
        didSet {
            Self.typeProperty = instanceProperty + 100
        }
    }

    // 연산 타입 프로펄티
    static var typeComputedProperty: Int {
        get {
            return typeProperty
        }
        set {
            typeProperty = newValue
        }
    }
}
AClass.typeProperty = 123
```

#### keyPath
keyPath를 사용하며 프로퍼티의 위치를 참조하도록 할 수 있다.

### Method
특정 타입에 관련된 함수
#### Instence Method
특정 타입의 특정 인스턴스에 속한 함수, 인스턴스가 존재할 때만 사용할 수 있음  
클래스의 인스턴스 매서드는 상관없지만, 구조체나, 열거형의 인스턴스의 값 타입이므로 매서드를 사용할 때 mutating 키워드를 붙여 해당 매서드가 인스턴스 내부의 값을 변경한다는 것을 명시해야 한다.
#### self
스위프트에서 모든 인스턴스는 암시적으로 생성된 self 프로퍼티를 갖는다.  
클래스의 경우 참조형이므로 self를 통해 자기 자신의 참조를 변경할 수는 없지만, 값 타입인 열거형, 구조체는 self 프로퍼티를 통해 자기 자신의 값을 치환할 수도 있다.
#### Type Method
타입 자체에 호출이 가능한 매서드, 흔히 static 키워드를 앞에 붙여 타입 매서드임을 나타낸다. static 대신 class 키워드를 사용할 경우에는 상속 후 매서드 재정의가 가능해진다.  
또한, type method의 경우 instence method와 달리 self가 instence가 아닌 type 그 자체를 가르킨다.
```swift
class AClass {
    static func staticTypeMethod() {
        print("AClass staticTypeMethod")
    }
    
    class func classTypeMethod() {
        print("AClass classTypeMethod")
    }
}

// 상속 후 타입 매서드 재정의
class BClass : AClass {
    // statictype method의 경우 override시 에러가 발생한다.
    static func staticTypeMethod() {
        print("BClass staticTypeMethod")
    }
    
    class func classTypeMethod() {
        print("BClass classTypeMethod")
    }
}
```