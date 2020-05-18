from selenium import webdriwer

browser = webdriwer.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
