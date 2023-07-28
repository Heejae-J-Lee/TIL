//
//  ContentView.swift
//  A Card
//
//  Created by Heejae on 2023/07/29.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack {
            Color(red: 0.00, green: 0.72, blue: 0.58)
                .edgesIgnoringSafeArea(/*@START_MENU_TOKEN@*/.all/*@END_MENU_TOKEN@*/)
            VStack {
                VStack {
                    Text("Hello, world!")
                        .font(Font.custom("Gaegu-Regular", size: 40))
                        .bold()
                    .foregroundColor(.white)
                }
            }
            .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
