protocol CanFly {
    func fly()
}
class Bird {
    
    var isFemale: Bool = true
    
    func layEgg() {
        if isFemale {
            print("The bird makes new bird in a shell")
        }
    }
}

class Eagle: Bird, CanFly {
    func fly() {
        print("독수리가 두 날개를 펄럭이며 하늘로 날아올랐습니다.")
    }
    func soar() {
        print("독수리가 공중을 활공했습니다.")
    }
}

class Penguin: Bird {
    func swim() {
        print("펭귄이 물속을 헤엄칩니다...")
    }
}

struct FlyingMuseum {
    func flyingDemo(flyingObject: CanFly){
        flyingObject.fly()
    }
}

struct Airplain: CanFly {
    func fly() {
        print("비행기가 엔진음을 내며 하늘로 날아올랐다...")
    }
}

let myEagle = Eagle()
myEagle.fly()
myEagle.layEgg()
myEagle.soar()

let myPenguin = Penguin()
myPenguin.layEgg()
myPenguin.swim()
myPenguin.fly()
