//
//  AppDelegate.swift
//  Clima
//
//  Created by Heejae on 2023/07/02.
//  Copyright © 2023 App Brewery. All rights reserved.
//

import Foundation

struct WeatherManager {
    let weatherURL = "https://api.openweathermap.org/data/2.5/weather?appid=5260a20e3b7a4eb96195513c0c8f2d37&units=metric"
    
    func fetchWeather(cityName: String) {
        let urlString = "\(weatherURL)&q=\(cityName)"
        performRequest(urlString: urlString)
    }
    
    func performRequest(urlString: String) {
        // Networking 1 : Create URL
        if let url = URL(string: urlString) {
            
            // Networking 2 : Create a URLSession
            let session = URLSession(configuration: .default)
            
            // Networking 3 : Give the Session a task
            let task = session.dataTask(with: url, completionHandler: handle(data:response:error:))
            
            // Networking 4 : Start the task
            task.resume()
            
        }
    }
    
    func handle(data: Data?, response: URLResponse?, error: Error?) -> Void {
        if error != nil {
            print(error!)
            return
        }
        
        if let safeData = data {
            let dataString = String(data: safeData, encoding: .utf8)
            print(dataString)
        }
    }
}
