//
//  ResultViewController.swift
//  Tipsy
//
//  Created by Heejae on 2023/06/24.
//  Copyright © 2023 The App Brewery. All rights reserved.
//

import UIKit

class ResultViewController: UIViewController {
    @IBOutlet weak var totalLabel: UILabel!
    @IBOutlet weak var settingsLabel: UILabel!
    
    var tipValueString: String!
    var splitValue: Int!
    var totalValue: String!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        totalLabel.text = totalValue
        settingsLabel.text = """
        Split between \(splitValue ?? 0),
        with \(tipValueString ?? "nil") tip.
        """
    }
    
    @IBAction func recalculatePressed(_ sender: UIButton) {
        self.dismiss(animated: true)
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
