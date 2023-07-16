//
//  CoinData.swift
//  ByteCoin
//
//  Created by Heejae on 2023/07/16.
//  Copyright © 2023 The App Brewery. All rights reserved.
//

import Foundation

struct CoinData: Decodable {
    let time: String
    let asset_id_base: String
    let asset_id_quote: String
    let rate: Double
}
