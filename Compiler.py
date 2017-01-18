import wx
import os
import gettext
import getpass
import sys


class MainFrame(wx.Frame):
    def __init__(self):
        self.browseico = wx.Button(self, wx.ID_ANY, "Browse")
        self.Bind(wx.EVT_BUTTON, self.browsecomico, self.browseico)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, "Output Type", choices=[("one folder"), ("one file")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, wx.ID_ANY, "GUI or CLI", choices=[('CLI'),("GUI(Qt, Wx etc.)")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, wx.ID_ANY, "GUI or CLI", choices=[("GUI(Qt, Wx etc.)"),("CLI")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.RunButton=wx.Button(self,wx.ID_ANY,'Compile(Build) Program')
        self.Bind(wx.EVT_BUTTON, self.run, self.RunButton)
        self.Quit=wx.Button(self,wx.ID_ANY,'Cancel')
        self.Bind(wx.EVT_BUTTON, self.Exit, self.Quit)
        self.username=getpass.getuser()
        self.__set_properties()
        self.__do_layout()
        self.install()
        self.Update()

    def __set_properties(self):
        self.Layout()
        sizer_1.Clear()

    def install(self):
        os.system('%s\\Scripts\\easy_install.exe pyinstaller' % sys.prefix)
        if os.path.isfile('%s\\Scripts\\pyinstaller.exe'%sys.prefix) == False:
            ErroR=wx.MessageDialog(None, 'You got an error during installing. Retry?', 'Error', wx.YES_NO | wx.ICON_ERROR)
            if ErroR.ShowModal()==wx.ID_YES:
                self.install()
            else:
                self.Exit(event=None)

    def run(self,event):
        global control
        radioget=self.radio_box_1.GetSelection()
        radioget1=self.radio_box_2.GetSelection()
        if radioget==1:
            filetype = '-D'
        elif radioget==0:
            filetype = '-F'
        if radioget1 == 0:
        if radioget==0:
            filetype='-D'
        elif radioget==1:
            filetype='-F'
        if radioget1==1:
            guicli='-w'
        elif radioget1==0:
            guicli='-c'
        if '.py' in self.fileentry.GetValue() or '.spec' in self.fileentry.GetValue():
            try:
                if len(self.IcoDialog.GetFilename()) == 0:
                    control = '%s\\Script\\pyinstaller.exe %s %s %s'%(sys.prefix,filetype,guicli,self.fileentry.GetValue())
                if len(IcoDialog.GetFilename()) == 0:
                    control = 'pyinstaller %s %s %s'%(filetype,guicli,self.fileentry.GetValue())

                else:
                    control = '%s\\Scripts\\pyinstaller.exe %s %s -i="%s" %s'%(sys.prefix,filetype,guicli,self.iconentry.GetValue(),self.fileentry.GetValue())

            except:
                control = '%s\\Scripts\\pyinstaller.exe %s %s %s'%(sys.prefix,filetype,guicli,self.fileentry.GetValue()
            os.system(control)


            if '.py' in self.filename:
                if self.radio_box_1.GetSelection()==1:
                    name = self.filename.replace('.py', '.exe')
                else:
                    name = self.filename.replace('.py', '')

            elif '.spec' in self.filename:
                if self.radio_box_1.GetSelection()==1:
                    name = self.filename.replace('.spec', '.exe')
                else:
                    name = self.filename.replace('.spec', '')
            if name in os.listdir('C:\\Users\\%s\\dist'%getpass.getuser()):
                finishcompile = wx.MessageDialog(None, 'Finish Compiling!', 'Compiled', wx.OK | wx.ICON_INFORMATION)
                finishcompile.ShowModal()
            else:
                ErroR=wx.MessageDialog(None,'You got an error during compiling, you can type %s in shell to see the error'%control,'Error',wx.OK|wx.ICON_ERROR)
            try:
                os.system(control)
                ErroR.ShowModal()

        else:
            select=wx.MessageDialog(None,'Please select a file!','Select',wx.YES_NO|wx.ICON_INFORMATION)
            select=wx.MessageDialog(None,'Please select a file!','Select',wx.YES_NO|wx.ICON_WARNING)
            if select.ShowModal()==wx.ID_YES:
                self.browsecomfile(event=None)


    def browsecomfile(self,event):
        filesFilter = "Python Files( *.py ) |*.py|Spec Files( *.spec)|*.spec"
        fileDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        fileDialog.SetDirectory('C:\\Users\\%s'%self.username)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.file = fileDialog.GetDirectory()+'\\'+fileDialog.GetFilename()
            self.filename=str(fileDialog.GetFilename())
            self.fileentry.SetValue(self.file)

    def browsecomico(self, event):
        filesFilter = "Icon Files( *.ico ) |*.ico"
        self.IcoDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        self.IcoDialog.SetDirectory('C:\\Users\\%s'%self.username)
        if self.IcoDialog.ShowModal()==wx.ID_OK:
            self.ico = self.IcoDialog.GetDirectory() + '\\' + self.IcoDialog.GetFilename()
            self.iconentry.SetValue(self.ico)
