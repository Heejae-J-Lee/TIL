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
        
        print(urlString)
    }
}
