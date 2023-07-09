import UIKit

var myDouble = 3.141591

extension Double {
    
    func round(to places: Int) -> Double {
        let precisionNumber = pow(10, Double(places))
        var n = self
        n = n * precisionNumber
        n.round()
        n = n / precisionNumber
        
        return n
    }
}

let myRoundedDouble = String(format: "%.2f", myDouble)

myDouble.round(to: 3)

let button = UIButton(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
button.backgroundColor = .red
//button.layer.cornerRadius = 25
//button.clipsToBounds = true

extension UIButton {
    func makeCircular() {
        self.layer.cornerRadius = 25
        self.clipsToBounds = true
    }
}

button.makeCircular()
