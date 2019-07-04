#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   UI_Send.py    
@Contact :   gdeichenshilin@gmail.com
@License :   (C)Copyright 2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/21 13:10   gxrao      1.0         None
'''

# import lib
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import socket
import rsa
import hashlib
import json
import struct
import os
import sys
##########################################################################
def rsa_decrypt(crypto,pubkey):
    """

    :param crypto:
    :param pubkey:
    :return:
    """
    content = rsa.decrypt(crypto,pubkey)
    content = content.decode('utf-8')
    print("结果：" + content)
    return content


def rsa_encrypt(d_str,privkey):
    """

    :param d_str: string , in this function  this string is md5
    :return: crypto ,pubkey
    """
    # build pubkey and privkey

    # 字符串进行编码
    content = d_str.encode('utf-8')
    print("编码结果：")
    print(content)
    # 私钥加密
    crypto = rsa.encrypt(content, privkey)
    print("私钥加密结果：")
    print(crypto)
    return crypto
###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"发送方", pos=wx.DefaultPosition, size=wx.Size(722, 585),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"通信"), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText9 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"本机IP", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        fgSizer3.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_textCtrl8 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        fgSizer3.Add(self.m_textCtrl8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer5.Add(fgSizer3, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"本机端口", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        fgSizer4.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        fgSizer4.Add(self.m_textCtrl9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer5.Add(fgSizer4, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer2.Add(bSizer5, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer3.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText15 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"目标IP", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        fgSizer8.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrl13, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"目标端口", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        fgSizer8.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrl16, 0, wx.ALL, 5)

        sbSizer3.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText16 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"连接状态", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        fgSizer9.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer9.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"程序状态", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        fgSizer9.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer9.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        sbSizer3.Add(fgSizer9, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_button5 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"连接", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"断开", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button6, 0, wx.ALL, 5)

        sbSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer4.Add(sbSizer3, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        gSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"内容"), wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        fgSizer12 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer12.SetFlexibleDirection(wx.BOTH)
        fgSizer12.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer8.Add(fgSizer12, 1, wx.EXPAND, 5)

        fgSizer121 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer121.SetFlexibleDirection(wx.BOTH)
        fgSizer121.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText13 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"提示行", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        fgSizer121.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer121.Add(self.m_textCtrl18, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText21 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"文件地址", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        fgSizer14.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_textCtrl20 = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer14.Add(self.m_textCtrl20, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer14, 1, wx.EXPAND, 5)

        fgSizer15 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText22 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"公钥地址", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        fgSizer15.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_textCtrl21 = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fgSizer15.Add(self.m_textCtrl21, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer15, 1, wx.EXPAND, 5)

        fgSizer16 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer16.SetFlexibleDirection(wx.BOTH)
        fgSizer16.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button17 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"产生密钥", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer16.Add(self.m_button17, 0, wx.ALL, 5)

        self.m_button21 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"发送文件", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer16.Add(self.m_button21, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer16, 1, wx.EXPAND, 5)

        fgSizer18 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button23 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"发送公钥", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer18.Add(self.m_button23, 0, wx.ALL, 5)

        self.m_button24 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"重置密钥", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer18.Add(self.m_button24, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer18, 1, wx.EXPAND, 5)

        fgSizer19 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button25 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer19.Add(self.m_button25, 0, wx.ALL, 5)

        bSizer9.Add(fgSizer19, 1, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        fgSizer121.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer8.Add(fgSizer121, 1, wx.EXPAND, 5)

        sbSizer5.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer5, 1, wx.EXPAND, 5)

        gSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button5.Bind(wx.EVT_BUTTON, self.connect_aim)
        self.m_button6.Bind(wx.EVT_BUTTON, self.disconnect_aim)
        self.m_button17.Bind(wx.EVT_BUTTON, self.createPrime)
        self.m_button21.Bind(wx.EVT_BUTTON, self.SendFile)
        self.m_button23.Bind(wx.EVT_BUTTON, self.SendPrime)
        self.m_button24.Bind(wx.EVT_BUTTON, self.rebuildPrime)
        self.m_button25.Bind(wx.EVT_BUTTON, self.exit)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def connect_aim(self, event):
        a = socket.gethostname()
        IPinfo = socket.gethostbyname_ex(a)
        self.m_textCtrl8.SetLabel(IPinfo[2][0])
        IP = self.m_textCtrl13.GetValue()
        PORT = self.m_textCtrl16.GetValue()
        print("IP:" + IP)
        print("PORT: " + PORT)
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, int(PORT)))
        self.m_textCtrl14.SetLabel("连接成功")

        # 检查公钥是否存在
        path = "./Key"
        for file in os.listdir(path):
            if file == "rsa_public_key.pem":
                self.m_textCtrl21.SetLabel(path + "/" + file)
                break
        print("进入下一环节")

    def disconnect_aim(self, event):
        self.m_textCtrl14.SetLabel("断开连接")
        client.close()

    def createPrime(self, event):
        print("创建密钥按钮")
        for i in os.listdir("./Key"):
            global public_key,private_key
            public_key, private_key = rsa.newkeys(1024)
            if i != "rsa_public_key.pem" or i !="rsa_private_key":
                print("生成密钥对")
                self.m_textCtrl15.SetLabel("生成密钥对")
                pubkey = rsa.PublicKey.save_pkcs1(public_key)
                pubfile = open("./Key/rsa_public_key.pem", "w+")
                pubfile.write(pubkey.decode("utf8"))
                pubfile.close()
                privkey = rsa.PrivateKey.save_pkcs1(private_key)
                privfile = open("./Key/rsa_private_key.pem","w+")
                privfile.write(privkey.decode('utf8'))
                privfile.close()
                self.m_textCtrl15.SetLabel("密钥对生成完毕")
                break
            else:
                self.m_textCtrl15.SetLabel("已有密钥对")
                print("已经有密钥对，无需再次生成")
                break

    def SendFile(self, event):
        print("发送文件按钮")
        # cmd = input("请输入命令：")  # put 111.jpg
        cmd = self.m_textCtrl21.GetValue()
        print(cmd)
        cmd = cmd.strip().split("./")
        action, filename = str(cmd[1]).split("/", 1)
        filesize = os.path.getsize(str(cmd[1]))

        file_info = {
            "action": action,
            "filename": filename,
            "filesize": filesize,
        }
        file_info_json = json.dumps(file_info).encode("utf8")

        ret = struct.pack("i", len(file_info_json))
        # 发送 file_info_json的打包长度
        client.send(ret)
        # 发送 file_info_json字节串
        client.send(file_info_json)
        # 发送 文件数据
        # md5 对象
        md5 = hashlib.md5()

        with open(filename, "rb") as f:
            for line in f:
                client.send(line)
                md5.update(line)

        data = client.recv(1024)
        print(md5.hexdigest())
        #md5 摘要
        md5_val = md5.hexdigest()
        #加密MD5 摘要公钥
        # md5_Crypto = rsa_encrypt(md5_val,public_key)
        # md5_val = md5_Crypto
        #发送加密MD5摘要
        client.send(md5_val.encode("utf8"))
        is_valid = client.recv(1024).decode('utf8')
        if is_valid == "203":
            print("文件完整！")
        else:
            print("文件上传失败！")

    def SendPrime(self, event):
        print("发送密钥按钮")
        # cmd = input("请输入命令：")  # put 111.jpg
        cmd = self.m_textCtrl21.GetValue()
        print(cmd)
        cmd = cmd.strip().split("./")
        action ,filename= str(cmd[1]).split("/",1)
        filesize = os.path.getsize(str(cmd[1]))

        file_info = {
            "action": action,
            "filename": filename,
            "filesize": filesize,
        }
        file_info_json = json.dumps(file_info).encode("utf8")

        ret = struct.pack("i", len(file_info_json))
        print('ret-----',ret)
        # 发送 file_info_json的打包长度
        client.send(ret)
        # 发送 file_info_json字节串
        client.send(file_info_json)
        # 发送 文件数据
        md5 = hashlib.md5()
        with open(str(cmd[1]), "rb") as f:
            for line in f:
                client.send(line)
                md5.update(line)
        data = client.recv(1024)
        print(md5.hexdigest())
        md5_val = md5.hexdigest()
        print("9")
        client.send(md5_val.encode("utf8"))
        is_valid = client.recv(1024).decode('utf8')
        if is_valid == "203":
            print("文件完整！")
        else:
            print("文件上传失败！")

    def rebuildPrime(self, event):
        public_key, private_key = rsa.newkeys(1024)
        self.m_textCtrl15.SetLabel("重新生成密钥对")
        print("重置密钥对")
        pubkey = rsa.PublicKey.save_pkcs1(public_key)
        pubfile = open("./Key/rsa_public_key.pem", "w+")
        pubfile.write(pubkey.decode("utf8"))
        pubfile.close()
        privkey = rsa.PrivateKey.save_pkcs1(private_key)
        privfile = open("./Key/rsa_private_key.pem", "w+")
        privfile.write(privkey.decode("utf8"))
        privfile.close()
        self.m_textCtrl15.SetLabel("密钥对生成完毕")

    def exit(self, event):
        sys.exit(1)


app = wx.App()
win = MyFrame1(None)
win.Show()
app.MainLoop()