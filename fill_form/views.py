from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.core.mail import EmailMessage
import time

def form(request):
    
    options = Options()
    #options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2,})
    driver = webdriver.Chrome(options=options)

    try:
        f_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfFXnxiFhCCK5a2INyDEgQp6GQEYvHocWGBdTDyY3EVhWr1Ag/viewform?vc=0&c=0&w=1&flr=0'
        driver.get(f_url)
        time.sleep(2)

        driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Rahul") #name

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("1234567890") #number

        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("example@gmail.com") #email
                            
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("address") #address
        
        driver.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('pincode') #pincode

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys('17102000') #bday

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Male') #gender

        code = driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[1]/div/div[1]/span[1]/div[1]/span/b').text #extract code
        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(code) #enter code

        time.sleep(3)

        driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        driver.save_screenshot('ss.png')

        time.sleep(5)

        email = EmailMessage(
            subject='Python (Selenium) Assignment - Rahul Wadangekar',
            body='htmlBody',
            from_email='rahulwadangekar@email.com',
            to=['rahulsw12234@gmail.com'],
            cc= ['rahul67052@gmail.com'],
        )
        email.content_subtype = "html"
        email.attach_file("ss.png")
        email.send(fail_silently=False)
    
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
    finally:
        driver.quit()
    
    return HttpResponse("Form Submitted Successfully.")

# def email(request):

#     try:
#         email = EmailMessage(
#             subject='Python (Selenium) Assignment - Rahul Wadangekar',
#             body='htmlBody',
#             from_email='rahulwadangekar@email.com',
#             to=['rahulsw12234@gmail.com'],
#             cc= ['rahul67052@gmail.com'],
#         )
#         email.content_subtype = "html"
#         #email.attach_file("ss.png")
#         email.send(fail_silently=False)
    
#     except Exception as e:
#         return HttpResponse(f"Email Error: {e}")

#     return HttpResponse("\nEmail Sent Successfully.")
