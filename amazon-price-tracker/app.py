#!/usr/bin/env python
from selenium import webdriver as wb
from selenium import common
from twilio.rest import Client
from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def constructMessage(price,title,rating):
    return ("The price of "+title+ " that you subscribed, which was rated at "+rating+", is "+price+" as per as "+(datetime.now()).strftime("%m-%d %H:%M:%S"))

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
            driver.get(url.rstrip())
            title = driver.find_element_by_id("productTitle")
            try:
                allprices = driver.find_element_by_id("priceblock_ourprice")
            except common.exceptions.NoSuchElementException:
                allprices=driver.find_element_by_id("priceblock_saleprice")
            try:
                rating = str(driver.find_element_by_id("acrPopover").get_attribute("title"))
            except common.exceptions.NoSuchElementException:
                rating = "NA"
            exactText=str(allprices.text).strip()
            exactTitle= str(title.text).strip()
            messageBody= constructMessage(exactText,exactTitle,rating)
            messageToSend = client.messages.create(
                        to="+918754513405",
                        from_="+14159801286",
                        body=messageBody
                    )
            print messageToSend.body
            driver.quit()
    except IOError, AttributeError:
        print "Error hai bhai"
    finally:
        print "Done"
mainConstruct()
# scheduler = BlockingScheduler()
# scheduler.add_job(mainConstruct, 'interval', hours=2)
# scheduler.start()