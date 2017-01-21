import wx
import os
import getpass
import sys

def getver():
    global finalver
    fullver=sys.version
    shortver=fullver[0:3]
    finalver=shortver.replace('.','')
getver()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MainFrame', size=(1000, 1000))
        self.Font=wx.Font(13,wx.SWISS,wx.NORMAL,wx.NORMAL)
        self.filelabel = wx.StaticText(self, wx.ID_ANY,"    File:")
        self.filelabel.SetFont(self.Font)
        self.fileentry = wx.TextCtrl(self, wx.ID_ANY, "")
        self.browsefile = wx.Button(self, wx.ID_ANY, "Browse")
        self.Bind(wx.EVT_BUTTON,self.browsecomfile, self.browsefile)
        self.iconlabel = wx.StaticText(self, wx.ID_ANY, "    Icon:")
        self.iconlabel.SetFont(self.Font)
        self.iconentry = wx.TextCtrl(self, wx.ID_ANY, "")
        self.browseico = wx.Button(self, wx.ID_ANY, "Browse")
        self.Bind(wx.EVT_BUTTON, self.browsecomico, self.browseico)
        self.FileType = wx.RadioBox(self, wx.ID_ANY, "Output Type", choices=[("one folder"), ("one file")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.WindowType = wx.RadioBox(self, wx.ID_ANY, "GUI or CLI", choices=[('CLI'),("GUI(Qt, Wx etc.)")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.RunButton=wx.Button(self,wx.ID_ANY,'Compile Program')
        self.Bind(wx.EVT_BUTTON, self.run, self.RunButton)
        self.Quit=wx.Button(self,wx.ID_ANY,'Cancel')
        self.Bind(wx.EVT_BUTTON, self.Exit, self.Quit)
        self.username=getpass.getuser()
        self.__set_properties()
        self.__do_layout()
        self.inPath()
        self.Update()

    def __set_properties(self):
        self.SetTitle("Compiler")
        self.FileType.SetSelection(0)
        self.WindowType.SetSelection(0)

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_2 = wx.GridSizer(1, 3, 0,0)
        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_4 = wx.GridSizer(1, 2, 0,0)
        grid_sizer_1.Add(self.filelabel, 0, 0, 0)
        grid_sizer_1.Add(self.fileentry, 0, 0, 0)
        grid_sizer_1.Add(self.browsefile, 0, 0, 0)
        grid_sizer_2.Add(self.iconlabel, 0, 0, 0)
        grid_sizer_2.Add(self.iconentry, 0, 0, 0)
        grid_sizer_2.Add(self.browseico, 0, 0, 0)
        grid_sizer_3.Add(self.FileType, 0, 0, 0)
        grid_sizer_3.Add(self.WindowType, 0, 0, 0)
        grid_sizer_4.Add(self.Quit, 0, 0, 0)
        grid_sizer_4.Add(self.RunButton, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, 0, 0)
        sizer_1.Add(grid_sizer_2, 1, 0, 0)
        sizer_1.Add(grid_sizer_3, 1, 0, 0)
        sizer_1.Add(grid_sizer_4, 1, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        sizer_1.Clear()

    def Exit(self,event):
        sys.exit()

    def inPath(self):
        if ('Python%s\\Scripts'%finalver in os.environ['path']) == False:
            warn = wx.MessageDialog(None,'Seems you didn\'t Add Python%s\\Scripts to PATH. Please add it then restart'%finalver,'Warning',wx.OK|wx.ICON_WARNING)
            warn.ShowModal()
            self.Exit(event=None)

    def run(self,event):
        radioget = self.FileType.GetSelection()
        radioget1 = self.WindowType.GetSelection()
        filename=str(self.fileentry.GetValue())
        if radioget == 1:
            filetype = '-F'
        elif radioget == 0:
            filetype = '-D'
        if radioget1 == 0:
            guicli = '-c'
        elif radioget1 == 1:
            guicli = '-w'
        if '.py' in filename or '.spec' in filename:
            try:
                if len(self.IcoDialog.GetFilename()) == 0:
                    control = 'pyinstaller %s %s %s'%(filetype,guicli,filename)

                else:
                    control = 'pyinstaller %s %s -i="%s" %s'%(filetype,guicli,self.iconentry.GetValue(),filename)

            except:
                control = 'pyinstaller %s %s %s'%(filetype,guicli,filename)
            os.system(control)


        if '.py' in self.fileentry.GetValue() or '.spec' in self.fileentry.GetValue():
            if '.ico' in self.iconentry.GetValue()==False:
                self.iconentry.Clear()
            else:
                filename.replace('\\',r'\\')
                name=os.path.basename(filename)
                if '.py' in name:
                    if radioget==0:
                        realname=name.replace('.py','')
                    elif radioget==1:
                        realname=name.replace('.py','.exe')
                elif '.spec' in name:
                    if radioget==0:
                        realname=name.replace('.spec','')
                    elif radioget==1:
                       realname=name.replace('.spec','.exe')

                if realname in str(os.listdir('%s\\dist' % os.getcwd())):
                    finishcompile = wx.MessageDialog(None, 'Finish Compiling!', 'Info', wx.OK | wx.ICON_INFORMATION)
                    finishcompile.ShowModal()
                else:

                    ErroR = wx.MessageDialog(None,'You got an error during compiling. Did you install pyinstaller correctly? Command: %s' % control,'Error', wx.OK | wx.ICON_ERROR)
                    ErroR.ShowModal()


        else:
            select=wx.MessageDialog(None, 'Please select a file!','Warning',wx.YES_NO|wx.ICON_INFORMATION)
            if select.ShowModal() == wx.ID_YES:
                self.browsecomfile(event=None)


    def browsecomfile(self,event):
        filesFilter = "Python Files( *.py ) |*.py|Spec Files( *.spec)|*.spec"
        fileDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        fileDialog.SetDirectory('C:\\Users\\%s'%self.username)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.file = fileDialog.GetDirectory()+'\\'+fileDialog.GetFilename()
            self.fileentry.SetValue(self.file)

    def browsecomico(self, event):
        filesFilter = "Icon Files( *.ico ) |*.ico"
        self.IcoDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        self.IcoDialog.SetDirectory('C:\\Users\\%s'%self.username)
        if self.IcoDialog.ShowModal()==wx.ID_OK:
            self.ico = self.IcoDialog.GetDirectory() + '\\' + self.IcoDialog.GetFilename()
            self.iconentry.SetValue(self.ico)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()