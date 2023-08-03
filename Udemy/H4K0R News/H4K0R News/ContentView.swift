//
//  ContentView.swift
//  H4K0R News
//
//  Created by Heejae on 2023/08/03.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            List(posts) { post in
                Text(post.title)
            }
            .navigationBarTitle("H4X0R News")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


let posts = [
]
