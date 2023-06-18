//
//  ViewController.swift
//  Quizzler-iOS13
//
//  Created by Angela Yu on 12/07/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var questionLabel: UILabel!
    @IBOutlet weak var progressBar: UIProgressView!
    @IBOutlet weak var trueButton: UIButton!
    @IBOutlet weak var FalseButton: UIButton!
    
    let quiz = [
        ["Four + Two is equal to Six", "True"],
        ["Five - Three is greater than One", "True"],
        ["Three + Eight is less than Ten", "False"]
    ]
    
    var questionNumber = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        updateUI()
    }

    @IBAction func answerButtonPressed(_ sender: UIButton) {
        if let answer = sender.currentTitle {
            if questionNumber == quiz.count {
                print("you answered every quiz")
                return
            }
            
            if answer == quiz[questionNumber][1] {
                print("Ding-Dong")
                questionNumber += 1
            } else {
                print("DD-ang!")
            }
        }
        
        updateUI()
    }
    
    func updateUI(){
        if questionNumber == quiz.count {
            questionNumber = 0
        }
        progressBar.progress = Float(questionNumber) / Float(quiz.count)
        questionLabel.text = quiz[questionNumber][0]
    }
}

