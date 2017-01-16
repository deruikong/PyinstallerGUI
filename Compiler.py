import wx
import os
import gettext
import sys

os.system('easy_install pyinstaller')


class MainFrame(wx.Frame):
    def __init__(self):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self,None,-1,'MainFrame',size=(1000,1000))
        self.filelabel = wx.StaticText(self, wx.ID_ANY,"        File:")
        self.fileentry = wx.TextCtrl(self, wx.ID_ANY, "")
        self.browsefile = wx.Button(self, wx.ID_ANY, "Browse")
        self.Bind(wx.EVT_BUTTON,self.browsecomfile, self.browsefile)
        self.iconlabel = wx.StaticText(self, wx.ID_ANY, "        Icon:")
        self.iconentry = wx.TextCtrl(self, wx.ID_ANY, "")
        self.browseico = wx.Button(self, wx.ID_ANY, "Browse")
        self.Bind(wx.EVT_BUTTON, self.browsecomico, self.browseico)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, "Output Type", choices=[("one folder"), ("one file")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, wx.ID_ANY, "GUI or CLI", choices=[("GUI(Qt, Wx etc.)"),("CLI")], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.RunButton=wx.Button(self,wx.ID_ANY,'Compile(Build) Program')
        self.Bind(wx.EVT_BUTTON, self.run, self.RunButton)
        self.Quit=wx.Button(self,wx.ID_ANY,'Cancel')
        self.Bind(wx.EVT_BUTTON, self.Exit, self.Quit)
        self.__set_properties()
        self.__do_layout()
        self.Update()

    def __set_properties(self):
        self.SetTitle("Compiler")
        self.radio_box_1.SetSelection(0)
        self.radio_box_2.SetSelection(0)


    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_2=wx.GridSizer(1,3,0,0)
        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_4=wx.GridSizer(1,2,0,0)
        grid_sizer_1.Add(self.filelabel, 0, 0, 0)
        grid_sizer_1.Add(self.fileentry, 0, 0, 0)
        grid_sizer_1.Add(self.browsefile, 0, 0, 0)
        grid_sizer_2.Add(self.iconlabel, 0, 0, 0)
        grid_sizer_2.Add(self.iconentry, 0, 0, 0)
        grid_sizer_2.Add(self.browseico, 0, 0, 0)
        grid_sizer_3.Add(self.radio_box_1, 0, 0, 0)
        grid_sizer_3.Add(self.radio_box_2, 0, 0, 0)
        grid_sizer_4.Add(self.Quit,0,0,0)
        grid_sizer_4.Add(self.RunButton,0,0,0)
        sizer_1.Add(grid_sizer_1,1, 0, 0)
        sizer_1.Add(grid_sizer_2, 1, 0, 0)
        sizer_1.Add(grid_sizer_3,1, 0, 0)
        sizer_1.Add(grid_sizer_4, 1, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        sizer_1.Clear()


    def run(self,event):
        global control
        radioget=self.radio_box_1.GetSelection()
        radioget1=self.radio_box_2.GetSelection()
        if radioget==0:
            filetype='-D'
        elif radioget==1:
            filetype='-F'
        if radioget1==0:
            guicli='-w'
        elif radioget1==1:
            guicli='-c'
        if '.py' in self.fileentry.GetValue() or '.spec' in self.fileentry.GetValue():
            try:
                if len(IcoDialog.GetFilename()) == 0:
                    control = 'pyinstaller %s %s %s'%(filetype,guicli,self.fileentry.GetValue())
                    os.system(control)
                else:
                    control = 'pyinstaller %s %s -i="%s" %s'%(filetype,guicli,self.iconentry.GetValue(),self.fileentry.GetValue())

            except:
                control = 'pyinstaller %s %s %s'%(filetype,guicli,self.fileentry.GetValue())
                os.system(control)
                finishcompile = wx.MessageDialog(None, 'Finish Compiling!', 'Compiled', wx.OK | wx.ICON_INFORMATION)
                finishcompile.ShowModal()
            try:
                os.system(control)
            except:
                ErroR = wx.MessageDialog(None, 'You got an error!', 'Error', wx.OK | wx.ICON_ERROR)
                ErroR.ShowModal()

        else:
            select=wx.MessageDialog(None,'Please select a file!','Select',wx.YES_NO|wx.ICON_WARNING)
            if select.ShowModal()==wx.ID_YES:
                self.browsecomfile(event=None)




    def Exit(self,event):
        sys.exit()


    def browsecomfile(self,event):
        global fileDialog
        filesFilter = "Python Files( *.py ) |*.py|Spec Files( *.spec)|*.spec"
        fileDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        fileDialog.SetDirectory('C:\\Users')
        if fileDialog.ShowModal() == wx.ID_OK:
            self.file = fileDialog.GetDirectory()+'\\'+fileDialog.GetFilename()
            self.fileentry.SetValue(self.file)

    def browsecomico(self, event):
        global IcoDialog
        filesFilter = "Icon Files( *.ico ) |*.ico"
        IcoDialog = wx.FileDialog(self, message="open", wildcard=filesFilter, style=wx.FD_OPEN)
        if IcoDialog.ShowModal()==wx.ID_OK:
            self.ico = IcoDialog.GetDirectory() + '\\' + IcoDialog.GetFilename()
            self.iconentry.SetValue(self.ico)



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
