from  selenium import  webdriver # import webdriver package
url ='https://www.youtube.com/watch?v=xM1R05qHato'  #specify the url of  the website you want to scrap
browser =webdriver.Chrome()#Download the web browser
browser.get(url)
browser.find_element_by_Xpath('/html/body/link').click() #finding  the browser element to scrap