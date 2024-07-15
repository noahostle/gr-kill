#!/usr/bin/python3

"""
author: c@shed
version: 1.0

"""

import google.generativeai as genai



genai.configure(api_key="-----")

model = genai.GenerativeModel('gemini-1.5-pro')

def getreview():
	a="Please generate a review for a local business called 'GD Cleaning'. For context that you dont have to mention, they operate in and around the macarthur region, nsw. Garry and Dianna are the owners, and they are very friendly. They drive to peoples homes and clean them. Please make the review sound as human as possible, and either none, or some missed capitalisation and punctuation, and the occasional bad grammar and spelling mistake. Write as naturally as possible and like a 40 year old person, DONT put a smiley face or emoji at the end, always capitalise the word 'I', and never double space. STRICTLY 55-70 WORDS"
	#b="Generate a positive review for a local business called 'GD Cleaning'. dont mention this, but they operate in and around macarthur nsw. Garry and Dianna are the owners and are friendly, mention this only 30% of the time. Type as much like a 40 year old human as possible, and as naturally as possible. Either type with no errors, or with some incorrect capitalisation, punctuation and grammar. Never use double spaces and always capitalise the word 'I'."
	return model.generate_content(a).text
print(getreview())