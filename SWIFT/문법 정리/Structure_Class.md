### Structure
struct 키워드를 통해 구조체를 정의 할 수 있음  
Swift의 모든 기본 데이터 타입은 구조체이다. (String, Bool, Int 등등...)  

※ 기본 데이터 타입이 값 타입인 전달인자를 통해 값을 전달하면, 값을 복사해 전달할 뿐, 함수 내부에서 전달받은 값을 변경해도 실제 변수나 상수에는 영향을 끼치지 못하는 이유이다. (스위트프트에서 권장하는 코딩 스타일)

다음 조건 중 하나라도 해당한다면, 구조체를 사용하는 것이 권장된다. (Swift Programming Language Guide)
- 연관된 간단한 값의 집합을 캡슐화하는 것만이 목적일 때
- 캡슐화 한 값을 참조하는 것보다 복사하는 것이 알맞을 때
- 구조체에 저장된 프로퍼티가 값 타입이며 참조하는 것보다 복사하는 것이 합당할 때
- 다른 타입으로부터 상속받거나 자신을 상속할 필요가 없을 때
```swift
struct struct_name {
    // property and method
}

struct UserInfo {
    var name: String
    var age: Int
}

// Initializer를 통해 구조체 생성과 동시에 초기화가 가능하다.
var student: UserInfo = (name:"Minsu", age:10)
student:name = "Kim Minsu" // 변경이 가능하다.

let student2: UserInfo = (name: "YoungHee", age:14)
student2.age =13 // 상수 구조체의 프로퍼티 변경은 불가
```

### Class
```swift
// 정의
class Student {
    // property and method
    var koreanScore: Int
    var englishScore: Int
    var mathScore: Int
}

// 부모로부터 상속받을 수도 있다
class MyStudent: student {
    // property and method
}

var minsu: Student = Student()
minsu.koreanScore = 70

// 구조체와 다르게 클래스는 상수로 선언해도 프로퍼티 값을 변경할 수 있다.
let younghee: Student = Student()
younghee.koreanScore = 88

class DeInitClass {
    var temp : Int

    // 메모리에서 해제될 경우
    deinit {
        print("deinitialize 될 때 출력됩니다.")
    }
}
var exercise: DeInitClass? = DeInitClass()
exercise = nil // deinit 되며 위의 출력이 콘솔창에 출력된다.

```

### Class와 Stucture 타입 비교
공통점
- 값을 정의하기 위해 프로퍼티 사용이 가능
- 기능 실행을 위한 매서드 정의 가능
- 서브스크립트 문법을 통해 프로퍼티에 접근하도록 서브스크립트 정의 가능
- 이니셜라이저 정의 가능
- 특정 기능 실행을 위한 프로토콜 정의가 가능

차이점
- 구조체는 값 타입이며 클래스는 참조 타입이다.
- 구조체는 상속을 사용할 수 없다
- 타입캐스팅은 클래스의 인스턴스에만 허용
- 디이셜라이저는 클래스에서만 사용 가능
- 참조 횟수 카운팅은 클래스에서만 사용 가능

#### 값 타입, 참조 타입
특정한 값이 전달되어지느냐, 아니면 값이 저장되어 있는 주소가 전달되어지느냐에 따라 값 타입과 참조 타입으로 구분할 수 있다.
인스턴스의 참조가 같은지 확인하기 위해 식별 연산자(Identity Operator / ===, !==)를 사용한다.



