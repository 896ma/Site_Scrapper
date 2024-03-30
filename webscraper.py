from  selenium import  webdriver # import webdriver package
url ='https://github.com/896ma'  #specify the url of  the website you want to scrap
browser =webdriver.chrome()#Download the web browser
browser.get(url)
browser.find_element_by_Xpath('').click() #finding  the browser element to scrap