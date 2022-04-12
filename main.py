import requests
from selenium import webdriver
import time

# 图片个数
num = 25

subject = input('主题(如：桃子核)')
saying_a = input('说法1(如：不能咽下去)')
saying_b = input('说法2(如：桃核太大会卡住)')
text = f'{subject}{saying_a}是怎么回事呢？{subject}相信大家都很熟悉，但是{subject}{saying_a}是怎么回事呢，下面就让小编带大家一起了解吧。\
{subject}{saying_a}，其实就是{saying_b}，大家可能会很惊讶{subject}怎么会{saying_a}呢？但事实就是这样，小编也感到非常惊讶。\
这就是关于{subject}{saying_a}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'

driver = webdriver.Chrome()


# 下载语音功能
def dl_yinpin(text):
    driver.get('http://www.liminba.com/tool/tts/')
    time.sleep(1)
    # 输入文案
    text_label = driver.find_element_by_id("itxt")
    text_label.send_keys(text)
    time.sleep(1)
    # 生成按钮
    dl = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/button[2]')
    dl.click()
    time.sleep(5)
    # 下载按钮
    dl1 = driver.find_element_by_link_text("保存为MP3")
    dl1.click()
    time.sleep(3)
    driver.close()


# 下载图片素材
def dl_pic(dl_url, img_name):
    # 下载照片
    img_resp = requests.get(dl_url)
    # img_resp.content # 拿到照片的字节信息
    with open(f"图片素材/{img_name}.jpg", mode="wb") as f:
        f.write(img_resp.content)  # 将内容写入文件
    print("图片素材", img_name, "下载完毕")
    img_resp.close()
    time.sleep(1)


bing_pic_url = 'https://cn.bing.com/images/async?q=' + subject + '&first=0&count=' + num + '&relp=35&lostate=r&mmasync=1&dgState=x*175_y*848_h*199_c*1_i*106_r*0'
driver.get(bing_pic_url)
time.sleep(1)
pics = driver.find_elements_by_xpath('//*[@id="mmComponent_images_1"]/ul/li/div/div[1]/a/div/img')
i = 0
for pic in pics:
    src = pic.get_attribute('src')
    dl_pic(src, str(subject) + str(i))
    i = i + 1

driver.quit()
