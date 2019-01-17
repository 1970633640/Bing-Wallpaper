# coding=utf-8
import urllib
import socket
from PIL import Image, ImageDraw, ImageFont
import os, sys, requests
import win32api,win32con,win32gui
os.chdir(sys.path[0])


def setWallpaper(bmp):

    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp, 1 + 2)


def getPage(url):
  #  request = urllib.Request(url)
 #   response = urllib.urlopen(request)
    content = requests.get(url)
    return content.text


def test1():
    import os
    return1 = os.system('ping www.baidu.com -n 1')
    if return1:
        return 404
    else:
        return 0


if test1() == 0:
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    result2 = getPage(url)
    # print result
    # page = result.read()
    result = result2
    ans = "http://cn.bing.com" + result[result.find("\"url\":\"") + 7:result.find(".jpg\",\"urlbase") + 4]
    print (ans)
    ans2 = result[result.find("copyright\":\"") + 12:result.find(u" (©")]
    print(ans2)
    url2 = ans
    f = requests.get(url2)
    data = f.content
    with open("down.jpg", "wb") as code:
        code.write(data)
    # urllib.urlretrieve(url2,  "down.jpg")
    image = Image.open( 'down.jpg')
    image = image.point(lambda x: x * 0.8)
    ttfont = ImageFont.truetype("C:/Windows/Fonts/SimHei.ttf", 20)
    draw = ImageDraw.Draw(image)
    print(ans2)
    draw.text((1920 - 20 * len(ans2) + 1, 1000 + 1), ans2, fill=(80, 80, 80), font=ttfont)
    draw.text((1920 - 20 * len(ans2) - 1, 1000 - 1), ans2, fill=(80, 80, 80), font=ttfont)
    draw.text((1920 - 20 * len(ans2) - 1, 1000 + 1), ans2, fill=(80, 80, 80), font=ttfont)
    draw.text((1920 - 20 * len(ans2) + 1, 1000 - 1), ans2, fill=(80, 80, 80), font=ttfont)
    draw.text((1920 - 20 * len(ans2), 1000), ans2, fill=(230, 230, 230), font=ttfont)
    image.save("Enhanced.jpg")
    setWallpaper("D:/bing/Enhanced.jpg")
