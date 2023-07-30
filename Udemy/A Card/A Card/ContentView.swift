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
                    Image("Cat")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 150.0, height: 150.0)
                        .clipShape(Circle())
                        .overlay(
                            Circle().stroke(Color.white, lineWidth: 5)
                        )
                    Text("이희재")
                        .font(Font.custom("Gaegu-Regular", size: 40))
                        .bold()
                    .foregroundColor(.white)
                    Text("iOS Developer ")
                        .foregroundColor(.white)
                        .font(.system(size: 25))
                    Divider()
                    InfoView(text: "+82 10 0000 0000", imageName: "phone.fill")
                    InfoView(text: "hee.404.jerry@gmail.com", imageName: "envelope.fill")
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

