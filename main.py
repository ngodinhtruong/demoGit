import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service

import Gui
edge_service = Service(os.path.join(os.getcwd(),'msedgedriver.exe'))

text2 = "Welcomto IUH"
index = 4
def submit_button_clicked(cookie_value):
    cookie = cookie_value.get()
    cookies = [
        {'name': 'ASC.AUTH',
         'value': f'{cookie}'}
    ]
    browser = webdriver.Edge(service=edge_service)
    browser.maximize_window()
    browser.get('https://sv.iuh.edu.vn')
    for cookie in cookies:
        browser.add_cookie(cookie)
    time.sleep(0.8)
    browser.get('https://sv.iuh.edu.vn')
    if(browser.title=='Khảo sát sự kiện'):
        while True:
            try:
                time.sleep(2)
                # get survey
                element = browser.find_element("xpath", '//*[@id="contnet"]/div/div[2]/div/div/div[2]/div[1]/a')
                element.click()
                time.sleep(0.8)
                #click rs
                i=2
                while True:
                    time.sleep(0.01)
                    try:
                        e = browser.find_element("xpath",f'//*[@id="form0"]/div/div[1]/div[{i}]/ul/li[{index}]/label/span')
                        e.click()
                        i+=1
                    except Exception as e:
                        break
                # input idea
                try:
                    input_element = browser.find_element("xpath", '//*[@id="LayYKien_5809_5809"]')
                    input_element.send_keys(f"{text2}")
                except Exception as e:
                    input_element = browser.find_element("xpath", '//*[@id="LayYKien_4450_4450"]')
                    input_element.send_keys(f"{text2}")
                # submit
                submit = browser.find_element("xpath", '//*[@id="btnGui"]')
                submit.click()
            except Exception as e:
                browser.close()
                Gui.windowTK.after(100, lambda: Gui.window_caution("DONE !"))

                break
    elif(browser.title=="Cổng thông tin sinh viên"):
        browser.close()
        Gui.windowTK.after(100,lambda :Gui.window_caution("There are no more survey forms !"))
    else:
        browser.close()
        Gui.windowTK.after(100,lambda :Gui.window_caution("The cookie is not valid !"))
def options_button_clicked(text1,choice_value):
    global text2
    global index
    choices = ['A. Hoàn toàn không đồng ý', 'B. Không đồng ý', 'C. Phân vân', 'D. Đồng ý', 'E. Hoàn toàn đồng ý']
    index = choices.index(choice_value) + 1
    text2 = text1
if __name__ == "__main__":
    Gui.start()


