import webbrowser

new =2
tabUrl="https://www.linkedin.com/search/results/index/?keywords="
term=input("Enter search query ")

webbrowser.open(tabUrl+term,new=new)