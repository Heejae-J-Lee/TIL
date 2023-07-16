//
//  CoinManager.swift
//  ByteCoin
//
//  Created by Angela Yu on 11/09/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import Foundation

protocol CoinManagerDelegate {
    func didUpdateCoinRate(_ coinManager: CoinManager, coinRate: Double)
    func didFailWithError(error: Error)
}

struct CoinManager {
    
    // https://rest.coinapi.io/v1/exchangerate/BTC?apikey=2FBDDEE1-0E74-4576-9C5F-F4E203C5F8EF
    let baseURL = "https://rest.coinapi.io/v1/exchangerate/BTC"
    let apiKey = "2FBDDEE1-0E74-4576-9C5F-F4E203C5F8EF"
    
    let currencyArray = ["AUD", "BRL","CAD","CNY","EUR","GBP","HKD","IDR","ILS","INR","JPY","MXN","NOK","NZD","PLN","RON","RUB","SEK","SGD","USD","ZAR"]

    var delegate: CoinManagerDelegate?
    
    func getCoinPrice(for currency: String){
        let urlString: String = "\(baseURL)/\(currency)?apikey=\(apiKey)"
        performRequest(with: urlString)
    }
    
    func performRequest(with urlString: String){
        // Networking 1 : Create URL
        if let url = URL(string: urlString) {
            
            // Networking 2 : Create a URLSession
            let session = URLSession(configuration: .default)
            
            // Networking 3 : Give the Session a task
            let task = session.dataTask(with: url) { (data, response, error ) in
                if error != nil {
                    delegate?.didFailWithError(error: error!)
                    return
                }
                
                if let safeData = data {
                    parseJSON(safeData)
                    return
                }
            }
            
            // Networking 4 : Start the task
            task.resume()
        }
    }
    
    func parseJSON(_ data: Data) {
        let decorder = JSONDecoder()
        
        do {
            let decodedData = try decorder.decode(CoinData.self, from: data)
            let lastPrice = round(decodedData.rate * 100) / 100
            
            self.delegate?.didUpdateCoinRate(self, coinRate: lastPrice)
        } catch {
            self.delegate?.didFailWithError(error: error)
        }
    }
}
