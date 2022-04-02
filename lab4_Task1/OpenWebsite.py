import webbrowser
import random

websites = ["google", "facebook", "github"]
website = websites[random.randrange(0, len(websites))]
webbrowser.open("https://" + website + ".com/")
