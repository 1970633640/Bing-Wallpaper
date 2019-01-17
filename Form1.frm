VERSION 5.00
Object = "{48E59290-9880-11CF-9754-00AA00C00908}#1.0#0"; "MSINET.OCX"
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   1980
   ClientLeft      =   40
   ClientTop       =   380
   ClientWidth     =   3120
   LinkTopic       =   "Form1"
   ScaleHeight     =   1980
   ScaleWidth      =   3120
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin InetCtlsObjects.Inet Inet1 
      Left            =   240
      Top             =   960
      _ExtentX        =   953
      _ExtentY        =   953
      _Version        =   393216
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Declare Function URLDownloadToFile Lib "urlmon" Alias "URLDownloadToFileA" (ByVal pCaller As Integer, ByVal szURL As String, ByVal szFileName As String, ByVal dwReserved As Integer, ByVal lpfnCB As Integer) As Long
Private Declare Function SystemParametersInfoByVal& Lib "user32" Alias "SystemParametersInfoA" (ByVal uAction As Long, ByVal uParam As Long, ByVal lpvParam As Any, ByVal fuWinIni As Long)
Const SPI_SETDESKWALLPAPER = 20
Const SPIF_UPDATEINIFILE = &H1


Private Sub Form_Load()
On Error Resume Next
Dim s As String
s = Inet1.OpenURL("http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")
s = Mid(s, InStr(1, s, "url"":""") + 6, InStr(1, s, """,""urlbase") - InStr(1, s, "url"":""") - 6)
Kill App.Path & "\1.jpg"
s = "http://cn.bing.com" + s
Call URLDownloadToFile(0, s, App.Path & "\1.jpg", 0, 0)
Call SystemParametersInfoByVal&(SPI_SETDESKWALLPAPER, 0, ByVal App.Path & "\1.jpg", SPIF_UPDATEINIFILE)
End
End Sub
