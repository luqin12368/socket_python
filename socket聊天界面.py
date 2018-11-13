# -*- coding: utf-8 -*-

'''
作者：路钦
功能：socket网络聊天
日期：2018-8-23
    Python code generated with wxFormBuilder (version Jun 17 2015)
    http://www.wxformbuilder.org/
    PLEASE DO "NOT" EDIT THIS FILE!
'''

import wx
import wx.xrc
import sys
import socket
from threading import Thread


###########################################################################
## def send_data
###########################################################################

def send_data(ip, data):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.sendto(data.encode('utf-8'), ip)
            s.close()
        except:
            pass

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(600, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(600, 400), wx.Size(600, 400))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"在线且60008端口开发的IP主机：", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        bSizer2.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, 400),
                                        wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY)

        bSizer2.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"IP：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(248, -1),
                                       wx.TE_LEFT)
        bSizer4.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"聊天记录：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer5.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 190),
                                       wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer5.Add(self.m_textCtrl4, 1, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"我说：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer5.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, -1),
                                       wx.TE_LEFT)
        bSizer5.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"聊天记录", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer6.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer5.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_textCtrl5.Bind(wx.EVT_TEXT_ENTER, self.send)
        self.m_button1.Bind(wx.EVT_BUTTON, self.send)
        self.m_button2.Bind(wx.EVT_BUTTON, self.jilu)
        self.m_button3.Bind(wx.EVT_BUTTON, self.close)

    def rec(self, s):
        self.s = s
        data = self.s.recvfrom(1024)
        data = data.decode('utf08')
        self.m_textCtrl4.WriteText(data)

    def __del__(self):
        self.s.close()

    # Virtual event handlers, overide them in your derived class
    def send(self, event):
        data = 'DonCharles says: ' + self.m_textCtrl5.GetValue()
        host = self.m_textCtrl2.GetValue()
        ip = (host, 60008)
        if host != '' and data != 'DonCharles says: ':
            send_data(ip, data)
            self.m_textCtrl4.WriteText(data + '\n')
            self.m_textCtrl5.Clear()
        self.m_textCtrl5.Clear()

    def jilu(self, event):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('172.25.9.200', 60008))
        # t = Thread(target=self.rec, args=(s,))
        # t.start()
        # t.join()
        self.rec(s)

    def close(self, event):
        sys.exit()


def main():
    app = wx.App()
    f1 = MyFrame2(None)
    f1.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
