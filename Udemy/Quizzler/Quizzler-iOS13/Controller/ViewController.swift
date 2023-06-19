//
//  ViewController.swift
//  Quizzler-iOS13
//
//  Created by Angela Yu on 12/07/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var scoreLable: UILabel!
    @IBOutlet weak var questionLabel: UILabel!
    @IBOutlet weak var progressBar: UIProgressView!
    @IBOutlet weak var choiceOneButton: UIButton!
    @IBOutlet weak var choiceTwoButton: UIButton!
    @IBOutlet weak var choiceThreeButton: UIButton!
    
    var quizBrain = QuizBrain()
    var timer: Timer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        updateUI()
    }

    @IBAction func answerButtonPressed(_ sender: UIButton) {
        if let userAnswer = sender.currentTitle {
            let userGotItRight = quizBrain.checkAnswer(userAnswer)
            
            if userGotItRight {
                sender.backgroundColor = UIColor.green
            } else {
                sender.backgroundColor = UIColor.red
            }
            quizBrain.nextQuestion()
            
            timer = Timer.scheduledTimer(timeInterval: 0.2, target:self, selector: #selector(updateUI), userInfo: nil, repeats: false)
        }
    }
    
    @objc func updateUI(){
        let choices = quizBrain.getAnswers()
        
        scoreLable.text = "Score: \(quizBrain.getScore())"
        progressBar.progress = quizBrain.getQuizProgress()
        questionLabel.text = quizBrain.getQuizText()
        choiceOneButton.backgroundColor = UIColor.clear
        choiceTwoButton.backgroundColor = UIColor.clear
        choiceThreeButton.backgroundColor = UIColor.clear
        
        choiceOneButton.setTitle(choices[0], for: .normal)
        choiceTwoButton.setTitle(choices[1], for: .normal)
        choiceThreeButton.setTitle(choices[2], for: .normal)
    }
    
}

