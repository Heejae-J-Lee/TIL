class Animal {
    var name: String
    
    init(n: String) {
        name = n
    }
}

class Human: Animal {
    func code() {
        print("Typing away...")
    }
}

class Fish: Animal {
    func breathUnderWater() {
        print("Breathing under water.")
    }
}

let human = Human(n: "Heejae")
human.code()
let human2 = Human(n: "Jaekee")
let nemo = Fish(n:"Nemo")

let neighbor = [human, human2, nemo]
// let neighbor = [human, human2, nemo, 12]    // error
// let neighbor : [Any] = [human, human2, nemo, 12]
// let neighbor : [AnyObject] = [human, human2, nemo, 12]    // error


if neighbor[0] is Human {
    print("First neighbor is a Human")
}

func findNemo(from animals: [Animal]) {
    for animal in animals {
        if animal is Fish {
            print("\(animal.name) is Fish")
            //animal.breathUnderWater()    // Nemo는 물고기지만... 사용불가능하다...
            // 대신... as!로 서브클래스로 강제 다운캐스트 할 수 있다.
            let fish = animal as! Fish
            fish.breathUnderWater()
            
            // super class로 원복 Upcast
            // sub class -> super class는 절대 실패하지 않는다
            let animalFish = fish as Animal
        }
    }
}

findNemo(from: neighbor)

// 다운캐스팅이 불가한 경우, 에러가 발생한다.
//let fish = neighbor[1] as! Fish

if let fish = neighbor[1] as? Fish {
    fish.breathUnderWater()
} else {
    print("Casting has Failed")
}
