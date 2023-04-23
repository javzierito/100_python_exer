import webbrowser
 
query = input("Input: ")
webbrowser.open("https://google.com/search?q=%s" % query)