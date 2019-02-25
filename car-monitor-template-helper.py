#Import the needed libaries
import pyperclip
import re

#Create main program
def main():

  #Create the data structure for the template
  car_monitor = {
    'Typ': '',
    'Display': '',
    'Auflösung': '',
    'Touchscreen': '',
    'Kontrast': '',
    'Helligkeit': '',
    'Anschlüsse': '',
    'Medien': '',
    'Audio-Formate': '',
    'Video-Formate': '',
    'Bild-Formate': '',
    'Kopfstützen-Material': '',
    'Farbe': '',
    'Betriebsspannung': '',
    'Stromaufnahme': '',
    'Abmessungen': '',
    'Besonderheiten': '',
                 }
  

  #Create all regex patterns for the keywords
  display = re.compile('\d"|\d\d"|\d\d?\.\d"|\d\d?\.\d? Zoll|\d\d?\.\d? Inche?s?|\d\d?\.\d?-Zoll')
  aufloesung = re.compile('\d\d\d\d?x\d\d\d\d?|\d\d\d\d?.?x.?\d\d\d.?Pixel|\d\d\d\d?.{0,10}?H.{0,10}?\d\d\d\d?.{0,10}?V')
  touchscreen = re.compile('touchscreen|Touchscreen|Touch-Screen|touch-screen')
  kontrast = re.compile('\d\d\d\d?:1')
  helligkeit = re.compile('\d\d\d?\d?cd|\d\d\d\d?.nits?')

    #Interfaces
  vga = re.compile('vga|Vga|VGA')
  hdmi = re.compile('hdmi|HDMI')
  av_in = re.compile('av in|AV In| AV IN|AV-In|AV-IN|A/V Eing|A/V-Eing|AV \(In\)')
  av_out = re.compile('av out|AV Out|AV OUT|AV-Out|AV-OUT|A/V-Ausg|A/V Ausg')
  video_in = re.compile('video in|Video In|Video IN|video-in|Video-In|Video-IN|Video Eing')
  video_out = re.compile('video out|Video Out|Video OUT|video-out|Video-Out|Video-OUT')
  audio_in = re.compile('audio in|Audio In|audio-in|Audio-In|Audio IN|Audio-IN|Audio Eing|audio eing')
  audio_out = re.compile('audio out|Audio Out|audio-out|Audio-Out|Audio OUT|Audio-OUT|Audio Ausg|audio ausg')
  kopfhoerer = re.compile('kopfhörer|Kopfhörer|headset|Headset|earphones|Earphones')
  bluetooth = re.compile('bluetooth|Bluetooth|BT \d\.\d|bt \d\.\d|A2DP')
  infrarot = re.compile('infrarot|Infrarot|IR')
  usb = re.compile('usb|USB')
  cardreader = re.compile('cardreader|Cardreader|card reader|Card Reader|SDHC|SDXC|microSD|microSDHC|microSDXC')

    #Medien
  medien_cd = re.compile(r'CD-R|\bCD')
  medien_dvd = re.compile('DVD')
  
    #Audio Formate
  audio_format_mp3 = re.compile('MP3')
  audio_format_alac = re.compile('ALAC')
  audio_format_flac = re.compile('FLAC')
  audio_format_aac = re.compile('AAC')
  audio_format_ogg = re.compile('OGG')
  audio_format_aiff = re.compile('AIFF')
  audio_format_wav = re.compile('WAV')
  audio_format_dsd = re.compile('DSD')

    #Video Formate
  video_format_divx = re.compile('DivX|Divx|DIVX|divx')
  video_format_xvid = re.compile('XviD|Xvid|XVID|xvid')
  video_format_flv = re.compile('FLV|flv|Flv')
  video_format_mov = re.compile('MOV|Mov|mov')
  video_format_mpeg = re.compile('MPEG|Mpeg|mpeg|MP4')
  video_format_wmv = re.compile('WMV|Wmv|wmv')
  video_format_mkv = re.compile('MKV|Mkv|mkv')
  video_format_rm = re.compile('\brm,?\b', flags=re.IGNORECASE)
  video_format_rmvb = re.compile('rmvb', flags=re.IGNORECASE)
  video_format_mjpeg = re.compile('mjpeg', flags=re.IGNORECASE)

    #Picture Formate
  bild_format_bmp = re.compile('BMP|Bmp|bmp')
  bild_format_gif = re.compile('GIF|Gif|gif')
  bild_format_jpg = re.compile('JPG|JPEG|Jpg|jpg')
  bild_format_png = re.compile('PNG|Png|png')
  bild_format_tiff = re.compile('TIFF|Tiff|tiff')

    #...Intefaces
  kopfstuetzen_material_leder = re.compile('Leder|leder|leather|Leather')

    #Measures
  abmessungen = re.compile('\d\d\d?x\d\d\d?x\d\d\d?mm')
    
    #Specifics
  besonderheiten_akku = re.compile('Akku|AKKU')
  besonderheiten_fernbedienung = re.compile('Fernbedienung|remote control|Remote control|fernbedienung|Remote Control')
  besonderheiten_lichtschutzblende = re.compile('Lichtschutzblende')
  besonderheiten_lautsprecher = re.compile('Lautsprecher')
  besonderheiten_non_glare = re.compile('non glare|non-glare|Non Glare|Non glare|Non-glare')
  besonderheiten_usb_ladefunktion = re.compile('USB Ladefunktion|USB Charging')
  
  


  #Take the text from the ram
  text = pyperclip.paste()


  #Search the string with the re patterns
  
  found_display = display.search(text)
  found_aufloesung = aufloesung.search(text)
  found_touchscreen = bool(touchscreen.search(text))
  found_kontrast = kontrast.search(text)
  found_helligkeit = helligkeit.search(text)

    #Searching for Interfaces
  found_vga = bool(vga.search(text))
  found_hdmi = bool(hdmi.search(text))
  found_av_in = bool(av_in.search(text))
  found_av_out = bool(av_out.search(text))
  found_video_in = bool(video_in.search(text))
  found_video_out = bool(video_out.search(text))
  found_audio_in = bool(audio_in.search(text))
  found_audio_out = bool(audio_out.search(text))
  found_kopfhoerer = bool(kopfhoerer.search(text))
  found_bluetooth = bool(bluetooth.search(text))
  found_infrarot = bool(infrarot.search(text))
  found_usb = bool(usb.search(text))
  found_cardreader = bool(cardreader.search(text))
  found_medien_cd = bool(medien_cd.search(text))
  found_medien_dvd = bool(medien_dvd.search(text))

    #Searching for Audio Formates
  found_audio_format_mp3 = bool(audio_format_mp3.search(text))
  found_audio_format_alac = bool(audio_format_alac.search(text))
  found_audio_format_flac = bool(audio_format_flac.search(text))
  found_audio_format_aac = bool(audio_format_aac.search(text))
  found_audio_format_ogg = bool(audio_format_ogg.search(text))
  found_audio_format_aiff = bool(audio_format_aiff.search(text))
  found_audio_format_wav = bool(audio_format_wav.search(text))
  found_audio_format_dsd = bool(audio_format_dsd.search(text))

    #Searching for Video Formates
  found_video_format_divx = bool(video_format_divx.search(text))
  found_video_format_xvid = bool(video_format_xvid.search(text))
  found_video_format_flv = bool(video_format_flv.search(text))
  found_video_format_mov = bool(video_format_mov.search(text))
  found_video_format_mpeg = bool(video_format_mpeg.search(text))
  found_video_format_wmv = bool(video_format_wmv.search(text))
  found_video_format_mkv = bool(video_format_mkv.search(text))
  found_video_format_rm = bool(video_format_rm.search(text))
  found_video_format_rmvb = bool(video_format_rmvb.search(text))
  found_video_format_mjpeg = bool(video_format_mjpeg.search(text))

    #Searching for Picture Formates
  found_bild_format_bmp = bool(bild_format_bmp.search(text))
  found_bild_format_gif = bool(bild_format_gif.search(text))
  found_bild_format_jpg = bool(bild_format_jpg.search(text))
  found_bild_format_png = bool(bild_format_png.search(text))
  found_bild_format_tiff = bool(bild_format_tiff.search(text))

     #...Searching Interfaces again
  found_kopfstuetzen_material_leder = bool(kopfstuetzen_material_leder.search(text))
  found_abmessungen = abmessungen.search(text)

    #Searching the specifics
  found_besonderheiten_akku = bool(besonderheiten_akku.search(text))
  found_besonderheiten_fernbedienung = bool(besonderheiten_fernbedienung.search(text))
  found_besonderheiten_lichtschutzblende = bool(besonderheiten_lichtschutzblende.search(text))
  found_besonderheiten_lautsprecher = bool(besonderheiten_lautsprecher.search(text))
  found_besonderheiten_non_glare = bool(besonderheiten_non_glare.search(text))
  found_besonderheiten_usb_ladefunktion = bool(besonderheiten_usb_ladefunktion.search(text))
  
  
  

  #Append all found keywords to my template string
  if found_display is not None:
    begin = found_display.regs[0][0]
    end = found_display.regs[0][1]
    result = found_display.string[begin:end]
    car_monitor['Display'] += str(result) + ' LCD'
  else:
    car_monitor['Display'] += 'keine Angabe'

  if found_aufloesung is not None:
    begin = found_aufloesung.regs[0][0]
    end = found_aufloesung.regs[0][1]
    result = found_aufloesung.string[begin:end]
    car_monitor['Auflösung'] += str(result)
  else:
    car_monitor['Auflösung'] += 'keine Angabe'

  if found_touchscreen is True:
    car_monitor['Touchscreen'] += 'ja'
  else:
    car_monitor['Touchscreen'] += 'keine Angabe'

  if found_kontrast is not None:
    begin = found_kontrast.regs[0][0]
    end = found_kontrast.regs[0][1]
    result = found_kontrast.string[begin:end]
    car_monitor['Kontrast'] += str(result)
  else:
    car_monitor['Kontrast'] += 'keine Angabe'

  if found_helligkeit is not None:
    begin = found_helligkeit.regs[0][0]
    end = found_helligkeit.regs[0][1]
    result = found_helligkeit.string[begin:end]
    car_monitor['Helligkeit'] += str(result) + '/m²'
  else:
    car_monitor['Helligkeit'] += 'keine Angabe'

    #If Statements for the Interfaces
  if found_vga is True:
    car_monitor['Anschlüsse'] += 'VGA'
  
  if found_hdmi is True:
    car_monitor['Anschlüsse'] += ', HDMI'

  if found_av_in is True:
    car_monitor['Anschlüsse'] += ', AV In'

  if found_av_out is True:
    car_monitor['Anschlüsse'] += ', AV Out'

  if found_video_in is True:
    car_monitor['Anschlüsse'] += ', Video In'

  if found_video_out is True:
    car_monitor['Anschlüsse'] += ', Video Out'

  if found_audio_in is True:
    car_monitor['Anschlüsse'] += ', Audio In'

  if found_audio_out is True:
    car_monitor['Anschlüsse'] += ', Audio Out'

  if found_kopfhoerer is True:
    car_monitor['Anschlüsse'] += ', Kopfhörer (3.5mm)'

  if found_bluetooth is True:
    car_monitor['Anschlüsse'] += ', Bluetooth'

  if found_infrarot is True:
    car_monitor['Anschlüsse'] += ', Infrarot'

  if found_usb is True:
    car_monitor['Anschlüsse'] += ', USB'

  if found_cardreader is True:
    car_monitor['Anschlüsse'] += ', Cardreader'

    #Medien
  if found_medien_cd is True:
    car_monitor['Medien'] += 'CD-R(W)'

  if found_medien_dvd is True:
    car_monitor['Medien'] += ', DVD-R(W)'

    #Audio Formates
  if found_audio_format_mp3 is True:
    car_monitor['Audio-Formate'] += 'MP3'

  if found_audio_format_alac is True:
    car_monitor['Audio-Formate'] += ', ALAC'

  if found_audio_format_flac is True:
    car_monitor['Audio-Formate'] += ', FLAC'

  if found_audio_format_aac is True:
    car_monitor['Audio-Formate'] += ', AAC'

  if found_audio_format_ogg is True:
    car_monitor['Audio-Formate'] += ', OGG'

  if found_audio_format_aiff is True:
    car_monitor['Audio-Formate'] += ', AIFF'

  if found_audio_format_wav is True:
    car_monitor['Audio-Formate'] += ', WAV'

  if found_audio_format_dsd is True:
    car_monitor['Audio-Formate'] += ', DSD'

    #Video Formate
  if found_video_format_divx is True:
    car_monitor['Video-Formate'] += 'DivX'

  if found_video_format_xvid is True:
    car_monitor['Video-Formate'] += ', XviD'

  if found_video_format_flv is True:
    car_monitor['Video-Formate'] += ', FLV'

  if found_video_format_mov is True:
    car_monitor['Video-Formate'] += ', MOV'

  if found_video_format_mpeg is True:
    car_monitor['Video-Formate'] += ', MPEG'

  if found_video_format_wmv is True:
    car_monitor['Video-Formate'] += ', WMV'

  if found_video_format_mkv is True:
    car_monitor['Video-Formate'] += ', MKV'

  if found_video_format_rm is True:
    car_monitor['Video-Formate'] += ', RM'
    
  if found_video_format_rmvb is True:
    car_monitor['Video-Formate'] += ', RMVB'
    
  if found_video_format_mjpeg is True:
    car_monitor['Video-Formate'] += ', MJPEG'
    

    #Picture Formates
  if found_bild_format_bmp is True:
    car_monitor['Bild-Formate'] += 'BMP'

  if found_bild_format_gif is True:
    car_monitor['Bild-Formate'] += ', GIF'

  if found_bild_format_jpg is True:
    car_monitor['Bild-Formate'] += ', JPG'

  if found_bild_format_png is True:
    car_monitor['Bild-Formate'] += ', PNG'

  if found_bild_format_tiff is True:
    car_monitor['Bild-Formate'] += ', TIFF'

    #...
  if found_kopfstuetzen_material_leder is True:
    car_monitor['Kopfstützen-Material'] += 'Leder'

  if found_abmessungen is not None:
    begin = found_abmessungen.regs[0][0]
    end = found_abmessungen.regs[0][1]
    result = found_abmessungen.string[begin:end]
    car_monitor['Abmessungen'] += str(result)

    #Specifics
  if found_besonderheiten_akku is True:
    car_monitor['Besonderheiten'] += 'Akku'

  if found_besonderheiten_fernbedienung is True:
    car_monitor['Besonderheiten'] += ', Fernbedienung'

  if found_besonderheiten_lichtschutzblende is True:
    car_monitor['Besonderheiten'] += ', Lichtschutzblende'

  if found_besonderheiten_lautsprecher is True:
    car_monitor['Besonderheiten'] += ', Lautsprecher'

  if found_besonderheiten_non_glare is True:
    car_monitor['Besonderheiten'] += 'non-glare'

  if found_besonderheiten_usb_ladefunktion is True:
    car_monitor['Besonderheiten'] += ', USB-Ladefunktion'
  

  #Add keine Angabe to empty strings
  for key in car_monitor:
    if car_monitor[key] == '':
      car_monitor[key] += 'keine Angabe'
    else:
      continue
  

  #Values from Dictionary to a string for pyperclip
  template_string = """
Typ: {}
Display: {}
Auflösung: {}
Touchscreen: {}
Kontrast: {}
Helligkeit: {}
Anschlüsse: {}
Medien: {}
Audio-Formate: {}
Video-Formate: {}
Bild-Formate: {}
Kopfstützen-Material: {}
Farbe: {}
Betriebsspannung: {}
Stromaufnahme: {}
Abmessungen (BxHxT): {}
Besonderheiten: {}
  """.format(car_monitor['Typ'],
             car_monitor['Display'],
             car_monitor['Auflösung'],
             car_monitor['Touchscreen'],
             car_monitor['Kontrast'],
             car_monitor['Helligkeit'],
             car_monitor['Anschlüsse'],
             car_monitor['Medien'],
             car_monitor['Audio-Formate'],
             car_monitor['Video-Formate'],
             car_monitor['Bild-Formate'],
             car_monitor['Kopfstützen-Material'],
             car_monitor['Farbe'],
             car_monitor['Betriebsspannung'],
             car_monitor['Stromaufnahme'],
             car_monitor['Abmessungen'],
             car_monitor['Besonderheiten']
             )
  
  #Copy my template string into ram.
  try:
    pyperclip.copy(template_string)
  except NameError as ne:
    print('Ops, you got a {} error.'.format(ne))

if __name__ == '__main__': main()



#Weitere mögliche Implementierungen

  #Abmessungen cm in mm umwandeln
##  for i in range(len(c)):
##	if '.' in c[i]:
##		c[i] = c[i].replace('.', '')
##	elif 'cm' in c[i]:
##		c[i] = c[i].replace('cm', '')
##	else:
##		continue
