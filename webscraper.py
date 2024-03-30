from  selenium import  webdriver # import webdriver package
url ='https://hurawatchtv.to/'  #specify the url of  the website you want to scrap
browser =webdriver.chrome()#Download the web browser
browser.get(url)
browser.find_element_by_Xpath('//*[@id="RxCzoB"]/script[3]').click() #finding  the browser element to scrap