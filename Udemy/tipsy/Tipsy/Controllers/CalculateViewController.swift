//
//  ViewController.swift
//  Tipsy
//
//  Created by Angela Yu on 09/09/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit

class CalculateViewController: UIViewController {
    @IBOutlet weak var billTextField: UITextField!
    @IBOutlet weak var zeroPctButton: UIButton!
    @IBOutlet weak var tenPctButton: UIButton!
    @IBOutlet weak var TwentyPctButton: UIButton!
    @IBOutlet weak var splitNumberLabel: UILabel!
    
    var currentSelectedButton: UIButton!
    var tipValue: Double!
    var splitValue: Int!
    var totalValue: String!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        currentSelectedButton = tenPctButton
        tipValue = 0.1
        splitValue = 2
    }

    @IBAction func tipChanged(_ sender: UIButton) {
        currentSelectedButton.isSelected = false
        
        currentSelectedButton = sender
        currentSelectedButton.isSelected = true
        
        switch (sender.currentTitle) {
        case "0%":
            tipValue = 0.0
        case "10%":
            tipValue = 0.1
        case "20%":
            tipValue = 0.2
        default:
            print("it is not allowed")
        }
        
        billTextField.endEditing(true)
    }
    
    @IBAction func stepperValueChanged(_ sender: UIStepper) {
        splitValue = Int(sender.value)
        splitNumberLabel.text = String(format: "%d", splitValue)
        billTextField.endEditing(true)
    }
    
    @IBAction func calculatePressed(_ sender: UIButton) {
        if let billValue = Double(billTextField.text!) {
            totalValue = String(format:"%.2f", billValue * (1 + tipValue) / Double(splitValue))
            
            performSegue(withIdentifier: "goToResult", sender: self)
        }
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
        if segue.identifier == "goToResult" {
            let destinationVC = segue.destination as! ResultViewController
            
            destinationVC.tipValueString = currentSelectedButton.currentTitle
            destinationVC.splitValue = splitValue
            destinationVC.totalValue = totalValue
        }
    }
}

