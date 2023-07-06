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
            let task = session.dataTask(with: url) { (data, response, error) in
                if error != nil {
                    print(error!)
                    return
                }
                
                if let safeData = data {
                    parseJSON(weatherData: safeData)
                }
            }
            // Networking 4 : Start the task
            task.resume()
        }
    }
    
    func parseJSON(weatherData: Data) {
        let decoder = JSONDecoder()
        do {
            let decodedData = try decoder.decode(WeatherData.self, from: weatherData)
            print(decodedData)
        } catch {
            print(error)
        }
    }
}
