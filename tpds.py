class tpds:
    def __init__(self, url, user, passw, memw):
        self.url = url
        self.user = user
        self.passw = passw
        self.memw = memw

    def scrape(self):

        with TorBrowserDriver("/home/liam/DataMule/tor-browser/") as driver:
            driver.get(self.url)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[1]').send_keys(self.user)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[2]').send_keys(self.passw)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[5]').click()
            time.sleep(10)
            while(driver.current_url.find('ddos')):
                time.sleep(10)
                if(driver.execute_script("return window.location.href.includes('ddos')")):
                    print('ddos in url')
                    driver.execute_script("window.location.href = 'http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion';")
                else:
                    print('ddos not in url')
                    break
            driver.find_element(By.XPATH, '/html/body/section[2]/ul[2]/li[2]/a').click()
            time.sleep(10)
            newURL = driver.current_url + '&ipp=100'
            driver.execute_script("window.location.href = '"+newURL+"';") #WHY DOES THE TOR MODULE NOT HAVE NAVIGATION
            time.sleep(10)
            pages = driver.find_element(By.XPATH, '/html/body/section[3]/div/div[2]/div[304]/div[2]').get_attribute('text')
            print(pages)

            totalPages = 99

            i = 0

            while i < totalPages:
                js = 'var listingData=\"[\";drugTitle=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)\").innerText};drugCat=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)\").innerText};drugLocation=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)\").innerText};drugStock=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)\").innerText};drugSales=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)\").innerText};drugPrice=function(c){return parseFloat(document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > strong:nth-child(1) > span:nth-child(1)\").innerText)};drugCurrency=function(c){a=document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > strong:nth-child(1) > span:nth-child(1)\").innerText;b=a.split(\" \");return b[1]};drugUnit=function(c){return document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)\").innerText};listing=document.getElementsByClassName(\"listings__product\");for(i=0;i<listing.length;i++){if(i==listing.length-1){last=\"]\"}else{last=\",\"}listingData=listingData+\'{\"title\":\"\'+drugTitle(i)+\'\",\"cat\":\"\'+drugCat(i)+\'\",\"loc\":\"\'+drugLocation(i)+\'\",\"stock\":\"\'+drugStock(i)+\'\",\"sales\":\"\'+drugSales(i)+\'\",\"price\":\"\'+drugPrice(i)+\'\",\"currency\":\"\'+drugCurrency(i)+\'\",\"unit\":\"\'+drugUnit(i)+\'\"}\'+last};return listingData'
                jsonD = driver.execute_script(js)
                pageData = json.loads(jsonD)
                print(pageData)
                sql = "INSERT INTO `Drugs`(`Advert title`, `Category`, `Location`, `Stock`, `Sales`, `Price`, `Units`, `Currency`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])"
                sequel.execute(sql, val)
                mydb.commit()
                if i == totalPages-1:
                    break
                i += 1
        mydb.close()