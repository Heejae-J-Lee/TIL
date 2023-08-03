//
//  PostData.swift
//  H4K0R News
//
//  Created by Heejae on 2023/08/03.
//

import Foundation

struct Results: Decodable {
    let hits: [Post]
    
}

struct Post: Decodable {
    var id: String {
        return objectID
    }
    let objectID: String
    let title: String
    let points: Int
    let url: String
}
