//
//  WebView.swift
//  H4K0R News
//
//  Created by Heejae on 2023/08/05.
//

import Foundation
import WebKit
import SwiftUI

struct WebView: UIViewRepresentable {
    
    let urlString: String?
    
    func updateUIView(_ uiView: WKWebView, context: Context) {
        if let safeString = urlString {
            if let url = URL(string: safeString) {
                let request = URLRequest(url: url)
                uiView.load(request)
            }
        }
    }
    
    func makeUIView(context: Context) -> WebView.UIViewType {
        return WKWebView()
    }
}
