class tpds:
    def __init__(self, url, user, passw, memw):
        self.url = url
        self.user = user
        self.passw = passw
        self.memw = memw

    def scrape(self):

        with TorBrowserDriver("/home/liam/DataMule/tor-browser/") as driver:
            driver.get(self.url)


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
