# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import os
import re
import sys

import cv2
import pytesseract
import wx
import wx.xrc

from PIL import Image, ImageEnhance
from pandas import np
from pywt import dwt2, idwt2


###########################################################################
## Class Login
###########################################################################


class Login(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"登录界面", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer3.AddSpacer(10)

        self.sys_name = wx.StaticText(self, wx.ID_ANY, u"图 像 压 缩 系 统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sys_name.Wrap(-1)
        self.sys_name.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer3.Add(self.sys_name, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        gSizer2.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0)
        self.username.SetMaxLength(6)
        gSizer2.Add(self.username, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"密  码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        gSizer2.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.password = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1),
                                    wx.TE_PASSWORD)
        self.password.SetMaxLength(6)
        gSizer2.Add(self.password, 0, wx.ALL, 5)

        bSizer3.Add(gSizer2, 1, wx.EXPAND, 5)

        ok_cancel_help = wx.StdDialogButtonSizer()
        self.ok_cancel_helpOK = wx.Button(self, wx.ID_OK)
        ok_cancel_help.AddButton(self.ok_cancel_helpOK)
        self.ok_cancel_helpCancel = wx.Button(self, wx.ID_CANCEL)
        ok_cancel_help.AddButton(self.ok_cancel_helpCancel)
        self.ok_cancel_helpHelp = wx.Button(self, wx.ID_HELP)
        ok_cancel_help.AddButton(self.ok_cancel_helpHelp)
        ok_cancel_help.Realize();

        bSizer3.Add(ok_cancel_help, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.register = wx.Button(self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
        self.register.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer3.Add(self.register, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ok_cancel_helpCancel.Bind(wx.EVT_BUTTON, self.cancel_event)
        self.ok_cancel_helpHelp.Bind(wx.EVT_BUTTON, self.help_event)
        self.ok_cancel_helpOK.Bind(wx.EVT_BUTTON, self.ok_event)
        self.register.Bind(wx.EVT_BUTTON, self.open_register_frame_event)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancel_event(self, event):
        self.Close()

    def help_event(self, event):
        wx.MessageBox("初始用户名和密码为admin和000000")

    def ok_event(self, event):
        username = self.username.GetValue()
        password = self.password.GetValue()
        if username == '' or password == '':
            wx.MessageBox("用户名或密码为空，请输入用户名和密码登录")
        else:
            f = open('login_info.txt', 'r')
            login_info = f.readlines()
            f.close()
            flag = 0
            for info in login_info:
                u_name = info.split(',')[0]
                pwd = info.split(',')[1][0:6]
                if u_name == username and pwd == password:
                    main_frame = Main(parent=None)
                    main_frame.Show()
                    self.Close()
                    flag = 1
                    break
            if flag == 0:
                wx.MessageBox("用户名或密码错误")

    def open_register_frame_event(self, event):
        register = Register(parent=None)
        register.Show()


###########################################################################
## Class Register
###########################################################################

class Register(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"注册界面", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.AddSpacer(30)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        gSizer3.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_BOTTOM, 5)

        self.username = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.username.SetMaxLength(6)
        self.username.SetMinSize(wx.Size(150, -1))

        gSizer3.Add(self.username, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"密  码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        gSizer3.Add(self.m_staticText11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.password = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1),
                                    wx.TE_PASSWORD)
        self.password.SetMaxLength(6)
        gSizer3.Add(self.password, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(gSizer3, 1, wx.EXPAND, 5)

        bSizer4.AddSpacer(20)

        ok_cancel_help = wx.StdDialogButtonSizer()
        self.ok_cancel_helpOK = wx.Button(self, wx.ID_OK)
        ok_cancel_help.AddButton(self.ok_cancel_helpOK)
        self.ok_cancel_helpCancel = wx.Button(self, wx.ID_CANCEL)
        ok_cancel_help.AddButton(self.ok_cancel_helpCancel)
        self.ok_cancel_helpHelp = wx.Button(self, wx.ID_HELP)
        ok_cancel_help.AddButton(self.ok_cancel_helpHelp)
        ok_cancel_help.Realize();

        bSizer4.Add(ok_cancel_help, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.AddSpacer(50)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ok_cancel_helpCancel.Bind(wx.EVT_BUTTON, self.cancel_event)
        self.ok_cancel_helpHelp.Bind(wx.EVT_BUTTON, self.help_event)
        self.ok_cancel_helpOK.Bind(wx.EVT_BUTTON, self.ok_event)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancel_event(self, event):
        self.Close()

    def help_event(self, event):
        wx.MessageBox("用户名和密码仅支持字母和数字，用户名长度不超过6位，密码长度为6位")

    def ok_event(self, event):
        u_name = self.username.GetValue()
        pwd = self.password.GetValue()
        if re.match('\w', u_name) != None and re.match('\w', pwd) != None:
            if len(pwd) < 6:
                wx.MessageBox("密码必须6位，请重新输入")
            else:
                f = open('login_info.txt', 'a')
                f.write('\n' + u_name + ',' + pwd)
                f.close()
                wx.MessageBox("注册成功")
                self.Close()
        else:
            wx.MessageBox("用户名或密码不规范")


###########################################################################
## Class Main
###########################################################################

class Main(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"主界面", pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        self.compression = wx.Button(self, wx.ID_ANY, u"压缩图像", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer6.Add(self.compression, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.extract_text = wx.Button(self, wx.ID_ANY, u"提取文本", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer6.Add(self.extract_text, 0, wx.ALL, 5)

        gSizer7.Add(gSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.select_image = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                              wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer7.Add(self.select_image, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5.Add(gSizer7, 0, wx.EXPAND, 5)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.image = wx.StaticBitmap(self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizer6.Add(self.image, 1, wx.ALL | wx.EXPAND, 5)

        self.m_scrolledWindow2.SetSizer(bSizer6)
        self.m_scrolledWindow2.Layout()
        bSizer6.Fit(self.m_scrolledWindow2)
        bSizer5.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.compression.Bind(wx.EVT_BUTTON, self.compression_event)
        self.extract_text.Bind(wx.EVT_BUTTON, self.extract_text_event)
        self.select_image.Bind(wx.EVT_FILEPICKER_CHANGED, self.select_image_event)

    def __del__(self):
        pass

    __imagename = None

    # Virtual event handlers, overide them in your derived class
    def compression_event(self, event):
        if self.__imagename != None:
            cprs_image = self.jpeg_image(self.__imagename)
            output = Output(parent=None, ori_image_path=self.__imagename, cpr_image_path=cprs_image)
            output.Show()
            self.Close()
        else:
            wx.MessageBox('未选择图片')

    def extract_text_event(self, event):
        if self.__imagename != None:
            text = self.extract_text_from_image(self.__imagename)
            wx.MessageBox(text)
        else:
            wx.MessageBox('未选择图片')

    def select_image_event(self, event):
        path = self.select_image.GetPath()
        img=Image.open(path)
        (x,y)=img.size
        resize_img=img.resize((600, (int(round(y * 600 / x)))), Image.ANTIALIAS)
        resize_img.save('temp_img.jpg')
        self.image.SetBitmap(wx.Bitmap('temp_img.jpg'))
        self.__imagename = path

    def jpeg_image(self, image_path):
        '压缩图像'
        ori_image = Image.open(image_path)  # cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
        (x, y) = ori_image.size
        if x >= 500 or y >= 500:
            if x > y:
                resize_image = ori_image.resize((500, (int(round(y * 500 / x)))), Image.ANTIALIAS)
            else:
                resize_image = ori_image.resize((int(round(x * 500 / y)), 500), Image.ANTIALIAS)
        else:
            resize_image = ori_image
        # 离散小波变换
        r, g, b = resize_image.convert("RGB").split()  # 分离三通道
        # cA_r, (cH_r, cV_r, cD_r) = dwt2(r, 'haar')
        # cA_g, (cH_g, cV_g, cD_g) = dwt2(g, 'haar')
        # cA_b, (cH_b, cV_b, cD_b) = dwt2(b, 'haar')
        # new_r = idwt2((cA_r, (cH_r, cV_r, cD_r)), 'haar')
        # new_g = idwt2((cA_g, (cH_g, cV_g, cD_g)), 'haar')
        # new_b = idwt2((cA_b, (cH_b, cV_b, cD_b)), 'haar')
        # pic = Image.merge('RGB', (new_r, new_g, new_b))  # 合并三通道
        cA, (cH, cV, cD) = dwt2(r, 'haar')
        img_name = image_path.split('\\')[-1].split('.')
        cprs_image_path = 'cpr_image/' + img_name[0] + '.' + img_name[1]
        cprs1_path = 'cpr_image/' + img_name[0] + '(1).' + img_name[1]
        cprs2_path = 'cpr_image/' + img_name[0] + '(2).' + img_name[1]
        cprs3_path = 'cpr_image/' + img_name[0] + '(3).' + img_name[1]
        cprs4_path = 'cpr_image/' + img_name[0] + '(4).' + img_name[1]
        cprs_path='cpr_image/' + img_name[0] + '(temp).' + img_name[1]
        # 小波变换之后，低频分量对应的图像：
        cv2.imwrite(cprs1_path, np.uint8(cA))
        # 小波变换之后，水平方向高频分量对应的图像：
        cv2.imwrite(cprs2_path, np.uint8(cH))
        # 小波变换之后，垂直平方向高频分量对应的图像：
        cv2.imwrite(cprs3_path, np.uint8(cV))
        # 小波变换之后，对角线方向高频分量对应的图像：
        cv2.imwrite(cprs4_path, np.uint8(cD))
        # 进行压缩处理
        cH_new = self.wave_cpr(cH, max(abs(np.min(cH)), np.max(cH)) * 0.8)
        cV_new = self.wave_cpr(cV, max(abs(np.min(cV)), np.max(cV)) * 0.8)
        cD_new = self.wave_cpr(cD, max(abs(np.min(cD)), np.max(cD)) * 0.8)
        # 根据小波系数重构回去的图像
        rimg = idwt2((cA, (cH_new, cV_new, cD_new)), 'haar')
        cv2.imwrite(cprs_path, np.uint8(rimg))
        new_g=Image.open(self.wavelet(g, 'g'))
        new_b=Image.open(self.wavelet(b, 'b'))
        new_r=Image.open(cprs_path)
        pic=Image.merge('RGB', (new_r, new_g, new_b))
        pic.save(cprs_image_path)
        return cprs_image_path

    def wavelet(self,img,img_name):
        cA, (cH, cV, cD) = dwt2(img, 'haar')
        # 进行压缩处理
        cprs_image_path = 'cpr_image/'+img_name+'.jpg'
        cH_new = self.wave_cpr(cH, max(abs(np.min(cH)), np.max(cH)) * 0.8)
        cV_new = self.wave_cpr(cV, max(abs(np.min(cV)), np.max(cV)) * 0.8)
        cD_new = self.wave_cpr(cD, max(abs(np.min(cD)), np.max(cD)) * 0.8)
        # 根据小波系数重构回去的图像
        rimg = idwt2((cA, (cH_new, cV_new, cD_new)), 'haar')
        cv2.imwrite(cprs_image_path, np.uint8(rimg))
        return cprs_image_path


    def wave_cpr(self, n, threshold):
        ni = 0
        nj = 0
        for i in n:
            for j in i:
                if abs(j) <= threshold:
                    n[ni][nj] = 0
                nj = nj + 1
            ni = ni + 1
            nj = 0
        return n

    pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

    def extract_text_from_image(self, image):
        '提取图像中文字'
        img = Image.open(image)
        re_img = img.convert('RGB')  # 这里也可以尝试使用L
        # enhancer = ImageEnhance.Color(re_img)
        # enhancer = enhancer.enhance(0)
        # enhancer = ImageEnhance.Brightness(enhancer)
        # enhancer = enhancer.enhance(2)
        # enhancer = ImageEnhance.Contrast(enhancer)
        # enhancer = enhancer.enhance(8)
        # enhancer = ImageEnhance.Sharpness(enhancer)
        # ehc_img = enhancer.enhance(20)
        text = pytesseract.image_to_string(re_img, lang='eng+chi_sim+chi_sim_vert')
        if text == '':
            return '[未识别到文字！]'
        else:
            return text


###########################################################################
## Class Output
###########################################################################


class Output(wx.Frame):

    def __init__(self, parent, ori_image_path, cpr_image_path):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1000, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.cpr_image_path = cpr_image_path
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"小波变换后的图像", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        gSizer4.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        ori_img_name = str(os.path.getsize(ori_image_path) / float(1024)).split('.')

        self.ori_image_size = wx.StaticText(self, wx.ID_ANY,
                                            '原图大小：' + ori_img_name[0] + '.' + ori_img_name[1][:2] + 'KB',
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.ori_image_size.Wrap(-1)
        self.ori_image_size.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        gSizer7.Add(self.ori_image_size, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        cpr_img_name = str(os.path.getsize(cpr_image_path) / float(1024)).split('.')

        self.cpr_image_type = wx.StaticText(self, wx.ID_ANY,
                                            '压缩后大小：' + cpr_img_name[0] + '.' + cpr_img_name[1][:2] + 'KB',
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.cpr_image_type.Wrap(-1)
        self.cpr_image_type.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        gSizer7.Add(self.cpr_image_type, 0, wx.ALL, 5)

        gSizer4.Add(gSizer7, 1, wx.EXPAND, 5)

        bSizer7.Add(gSizer4, 0, wx.EXPAND, 5)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        gSizer5 = wx.GridSizer(0, 2, 0, 0)
        dwt_path = cpr_image_path.split('.')

        self.i1 = wx.StaticBitmap(self, wx.ID_ANY,
                                  wx.Bitmap(dwt_path[0] + '(1).' + dwt_path[1], wx.BITMAP_TYPE_ANY),
                                  wx.DefaultPosition, wx.Size(-1, -1), 0)
        gSizer5.Add(self.i1, 1, wx.ALL | wx.EXPAND, 5)

        self.i2 = wx.StaticBitmap(self, wx.ID_ANY,
                                  wx.Bitmap(dwt_path[0] + '(2).' + dwt_path[1], wx.BITMAP_TYPE_ANY),
                                  wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.i2, 1, wx.ALL | wx.EXPAND, 5)

        self.i3 = wx.StaticBitmap(self, wx.ID_ANY,
                                  wx.Bitmap(dwt_path[0] + '(3).' + dwt_path[1], wx.BITMAP_TYPE_ANY),
                                  wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.i3, 1, wx.ALL | wx.EXPAND, 5)

        self.i4 = wx.StaticBitmap(self, wx.ID_ANY,
                                  wx.Bitmap(dwt_path[0] + '(4).' + dwt_path[1], wx.BITMAP_TYPE_ANY),
                                  wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.i4, 1, wx.ALL | wx.EXPAND, 5)

        gSizer6.Add(gSizer5, 1, wx.EXPAND, 5)

        self.m_scrolledWindow3 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow3.SetScrollRate(5, 5)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.image = wx.StaticBitmap(self.m_scrolledWindow3, wx.ID_ANY,
                                     wx.Bitmap(cpr_image_path, wx.BITMAP_TYPE_ANY),
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.image, 1, wx.ALL | wx.EXPAND, 5)

        self.m_scrolledWindow3.SetSizer(bSizer5)
        self.m_scrolledWindow3.Layout()
        bSizer5.Fit(self.m_scrolledWindow3)
        gSizer6.Add(self.m_scrolledWindow3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer7.Add(gSizer6, 1, wx.EXPAND, 5)

        gbSizer7 = wx.GridBagSizer(0, 0)
        gbSizer7.SetFlexibleDirection(wx.BOTH)
        gbSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.cps_image_path = wx.Button(self, wx.ID_ANY, u"压缩图像路径", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.cps_image_path, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.back_to_main = wx.Button(self, wx.ID_ANY, u"返回主界面", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.back_to_main, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.exit = wx.Button(self, wx.ID_ANY, u"退出系统", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.exit, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer7.Add(gbSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.cps_image_path.Bind(wx.EVT_BUTTON, self.image_path_event)
        self.back_to_main.Bind(wx.EVT_BUTTON, self.back_to_main_event)
        self.exit.Bind(wx.EVT_BUTTON, self.exit_event)

    def __del__(self):
        pass

    # Virtual event handlers,  them in your derived class
    def image_path_event(self, event):
        wx.MessageBox('E:/计算机视觉/课程设计/myjob/' + self.cpr_image_path)

    def back_to_main_event(self, event):
        main_fram = Main(parent=None)
        main_fram.Show()
        self.Close()

    def exit_event(self, event):
        sys.exit()


if __name__ == '__main__':
    app = wx.App()  # 初始化
    login = Main(parent=None)  # 实例MyFrame类，并传递参数
    login.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法
