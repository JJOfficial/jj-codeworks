import json

from selenium import webdriver
import time
#创建驱动对象
driver=webdriver.Chrome()
#取到jd网址
url='https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_93042f518fa345c6b9e3d150b049c13f'
driver.get(url)
#在搜索框中输入
input_text=driver.find_element_by_xpath('//input[@class="text"]')
#input_text=driver.find_eleent_by_name('wd')
#对输入框中的内容进行清除
input_text.clear()
#写入搜索文本
input_text.send_keys('七海nanami')
time.sleep(5)
#点击搜索按钮搜索相关数据
input_button=driver.find_element_by_xpath('//button[@class="button"]')
input_button.click()
time.sleep(4)
jsdemo='window.scrollTo(1000,50000)'
driver.execute_script(jsdemo)
time.sleep(2)
item_list=driver.find_elements_by_xpath('//li[@class="gl-item"]')

for item in item_list:
    print(item)
    itemdir =""
    item_price=item.find_element_by_xpath('.//div[@class="p-price"]').text
    item_content=item.find_element_by_xpath('.//div[@class="p-name p-name-type-2"]').text.replace('\n','')
    itemdir=item_price+item_content
    with open('jingdong.html','a',encoding='utf-8') as file:
        json.dump(itemdir, file, ensure_ascii=False)
        file.write('\n')


