//
//  Constants.swift
//  Flash Chat iOS13
//
//  Created by Heejae on 2023/07/19.
//  Copyright © 2023 Angela Yu. All rights reserved.
//

struct K {
    static let appName = "⚡️FlashChat"
    
    static let cellIdentifier = "ReusableCell"
    static let cellNibName = "MessageCell"
    
    static let WelcomeToRegisterSegue = "goToRegister"
    static let WelcomeToLoginSegue = "goToLogin"
    static let registerSegue = "goToChatFromRegister"
    static let loginSegue = "goToChatFromLogin"
    
    struct BrandColors {
        static let purple = "BrandPurple"
        static let lightPurple = "BrandLightPurple"
        static let blue = "BrandBlue"
        static let lighBlue = "BrandLightBlue"
    }
    
    struct FStore {
        static let collectionName = "messages"
        static let senderField = "sender"
        static let bodyField = "body"
        static let dateField = "date"
    }
}
