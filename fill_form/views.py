from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.core.mail import EmailMessage
import time

def form(request):
    
    options = Options()
    driver = webdriver.Chrome(options=options)

    try:
        f_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform'
        driver.get(f_url)
        time.sleep(2)

        driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Rahul Wadangekar") #name

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("9325094486") #number

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("rahulwadangekar@gmail.com") #email
                            
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("974 E ward shahupuri 7th Lane Kolhapur") #address
        
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('416001') #pincode

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys('17102000') #bday

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Male') #gender

        code = driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[1]/div/div[1]/span[1]/b').text #extract code
        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(code) #enter code

        time.sleep(3)

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        driver.save_screenshot('ss.png')

        time.sleep(5)

        email = EmailMessage(
            subject='Python (Selenium) Assignment - Rahul Wadangekar',
            body='htmlBody',
            from_email='rahulwadangekar@email.com',
            to=['tech@themedius.ai'],
            cc= [' hr@themedius.ai'],
        )
        email.content_subtype = "html"
        email.attach_file("ss.png")
        email.attach_file("Project Documentation.pdf")
        email.send(fail_silently=False)
    
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
    finally:
        driver.quit()
    
    return HttpResponse("Form Submitted Successfully.")
 
