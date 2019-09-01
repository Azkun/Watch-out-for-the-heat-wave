Option Explicit
Dim Msg,Question,PathSound
Msg = "It's time to drink water !"
PathSound = "./notif.mp3" 'Relative Path
Call Play(PathSound)
msgbox("This is the drink water's hour !")
Call Play(PathSound)
Call Play(PathSound)
'**********************************************************
Sub Play(SoundFile)
Dim Sound
Set Sound = CreateObject("WMPlayer.OCX")
Sound.URL = SoundFile
Sound.settings.volume = 100
Sound.Controls.play
do while Sound.currentmedia.duration = 0
    wscript.sleep 100
loop
wscript.sleep(int(Sound.currentmedia.duration)+1)*1000
End Sub
'**********************************************************
