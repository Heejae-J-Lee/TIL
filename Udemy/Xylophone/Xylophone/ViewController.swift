//
//  ViewController.swift
//  Xylophone
//
//  Created by Angela Yu on 28/06/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController {
    
    var player: AVAudioPlayer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func KeyPressed(_ sender: UIButton) {
        
        if let key = sender.titleLabel?.text {
            playSound(key)
        }
        
        sender.alpha = 1.0
        
    }
    
    @IBAction func KeyDown(_ sender: UIButton) {
        sender.alpha = 0.5
    }
    
    func playSound(_ fileName: String) {
        guard let url = Bundle.main.url(forResource: fileName, withExtension: "wav") else {return}
        do {
            try AVAudioSession.sharedInstance().setCategory(.playback, mode: .default)
            try AVAudioSession.sharedInstance().setActive(true)
            
            player = try AVAudioPlayer(contentsOf: url)
            
            guard let player = player else { return }
            
            player.play()
            
        } catch let error {
            print(error.localizedDescription)
        }
    }

}

