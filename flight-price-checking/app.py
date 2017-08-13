#!/usr/bin/env python
from selenium import webdriver as wb
from twilio.rest import Client
from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def constructMessage(price):
    timestamp= float(time.time())
    totalStamp= datetime.fromtimestamp(timestamp)
    return ("The price of MAA-IXB flight is "+price+" as per as "+totalStamp.strftime("%m-%d %H:%M:%S"))

def mainConstruct():
    credFile= open('client.secret.txt').readlines()
    sID=credFile[0].rstrip()
    authToken=credFile[1].rstrip()
    client = Client(sID,authToken)
    urldummy= open("buffer.txt").readlines()

    try:
        for url in urldummy:
            driver = wb.PhantomJS()
            driver.set_window_size(1120, 550)
            driver.get(url)
            allprices = driver.find_elements_by_xpath("//span[@class='js-total-amt-pay']")
            # print allprices
            for price in allprices:
                exactPrice = price.find_element_by_xpath(".//span[@class='price']")
                if not len(exactPrice.text)==0:
                    message = constructMessage(exactPrice.text)
                    messageToSend = client.messages.create(
                        to="+918754513405",
                        from_="+14159801286",
                        body=message
                    )
                    print (messageToSend.body)
                    break
            driver.quit()
    except IOError, AttributeError:
        pass
    finally:
        print "Done"

scheduler = BlockingScheduler()
scheduler.add_job(mainConstruct, 'interval', hours=2)
scheduler.start()