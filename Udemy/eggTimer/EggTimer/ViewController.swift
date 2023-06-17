//
//  ViewController.swift
//  EggTimer
//
//  Created by Angela Yu on 08/07/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var titleLable: UILabel!
    @IBOutlet weak var progressBar: UIProgressView!
    //let eggTimes: [String: Int] = ["Soft":300, "Medium":420, "Hard": 720]
    let eggTimes: [String: Int] = ["Soft":3, "Medium":4, "Hard": 7]
    
    var timer: Timer?
    var boilTime = 0
    var entireTime = 0
    
    @IBAction func hardnessSelected(_ sender: UIButton) {
        let hardness = sender.currentTitle!
        self.timer?.invalidate()
        progressBar.progress = 0.0
        
        if let time = eggTimes[hardness] {
            
            boilTime = time
            entireTime = time
            
            self.timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(updateCounter), userInfo: nil, repeats: true)
        }
    }
    
    @objc func updateCounter() {
        progressBar.progress = 1.0 - Float(boilTime) / Float(entireTime)
        if boilTime > 0 {
            print("\(boilTime) seconds are remain.")
            boilTime -= 1
        } else {
            titleLable.text = "Done!"
            self.timer?.invalidate()
        }
    }
}
