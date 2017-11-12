import webbrowser

new =2
tabUrl="https://www.facebook.com/search/top/?q="
term=input("Enter search query ")

webbrowser.open(tabUrl+term,new=new)