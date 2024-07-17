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
        f_url = 'google_form_link'
        driver.get(f_url)
        time.sleep(2)

        driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("name") #name

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("number") #number

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("@gmail.com") #email
                            
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("addr") #address
        
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('pin') #pincode

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys('bday') #bday

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('gender') #gender

        code = driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[1]/div/div[1]/span[1]/b').text #extract code
        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(code) #enter code

        time.sleep(3)

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        driver.save_screenshot('ss.png')

        time.sleep(5)

        email = EmailMessage(
            subject='subject',
            body='GitHub link: https://github.com/rahulsw00/python-selenium-assignment',
            from_email='from@gmail.com',
            to=['to@gmail.com'],
            cc= [' cc@gmail.com'],
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
 
