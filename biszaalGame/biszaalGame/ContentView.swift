//
//  ContentView.swift
//  biszaalGame
//
//  Created by Bishal Aryal on 2020/03/11.
//  Copyright © 2020 Bishal Aryal. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(alignment: .center) {
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
            HStack {
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
                Image(randomIcon())
            }
        }
        .padding(.bottom, -250.0)
    }
}

func randomIcon () -> String {
    let icons = ["facebook", "instagram", "snapchat", "youtube", "twitter"]
    return icons.randomElement()!
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
