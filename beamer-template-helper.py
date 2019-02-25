import pyperclip
import re


#Text von der Zwischenablage in Variable speichern
text = pyperclip.paste()



#Template Dictionary

beamer_template = {
	'Typ': '',
	'Chips': '',
	'Auflösung': '',
	'Helligkeit': '',
	'Kontrast': '',
	'Bildverhältnis': '',
	'Bilddiagonale': '',
	'Projektionsabstand': '',
	'Projektionsverhältnis': '',
	'Lampenlebensdauer': '',
	'Geräuschentwicklung': '',
	'Lens-Shift': '',
	'Anschlüsse': '',
	'Stromverbrauch': '',
	'Abmessungen': '',
	'Gewicht': '',
	'Besonderheiten': '',
	'Herstellergarantie': ''
	}


#Regex Objekte

	#Typ
dlp = re.compile('dlp', flags=re.IGNORECASE)
lcd = re.compile('lcd', flags=re.IGNORECASE)
lcos = re.compile('lcos', flags=re.IGNORECASE)
aufloesung = re.compile('\d\d\d\d?x\d\d\d\d?')
helligkeit = re.compile('\d\d\d\d?.{0,20}?lumen', flags=re.IGNORECASE)
kontrast = re.compile('\d\d\d|\d\d?\.\d\d\d')

	#Lens-Shift
lens_shift = re.compile('lens shift', flags=re.IGNORECASE)

	#Anschlüsse
vga_in = re.compile('vga in', flags=re.IGNORECASE)
vga_out = re.compile('vga out', flags=re.IGNORECASE)
vga = re.compile('vga', flags=re.IGNORECASE)
hdmi = re.compile('hdmi', flags=re.IGNORECASE)
dvi = re.compile('dvi', flags=re.IGNORECASE)
displayport = re.compile('displayport', flags=re.IGNORECASE)
composite_video = re.compile('composite video|\bfbas\b|\bbas\b|\bcvbs\b', flags=re.IGNORECASE)
s_video = re.compile('s.video', flags=re.IGNORECASE)
komponenten_in = re.compile('komponenten.in', flags=re.IGNORECASE)
komponenten_out = re.compile('komponenten.out', flags=re.IGNORECASE)
komponenten = re.compile('komponenten', flags=re.IGNORECASE)
sdi_3g = re.compile('3g.sdi', flags=re.IGNORECASE)
sdi_hd = re.compile('hd.sdi', flags=re.IGNORECASE)
sdi_sd = re.compile('sd.sdi', flags=re.IGNORECASE)
sdi = re.compile('sdi', flags=re.IGNORECASE)
stereo_line_in = re.compile('stereo line in', flags=re.IGNORECASE)
stereo_line_out = re.compile('stereo line out', flags=re.IGNORECASE)
digital_audio_in = re.compile('digital audio in', flags=re.IGNORECASE)
digital_audio_out = re.compile('digital audio out', flags=re.IGNORECASE)
klinke_audio_in = re.compile('klinke audio in', flags=re.IGNORECASE)
klinke_audio_out = re.compile('klinke audio out' , flags=re.IGNORECASE)
lan = re.compile('\blan\b|rj45', flags=re.IGNORECASE)
usb = re.compile('usb.?\d\.?\d?', flags=re.IGNORECASE)
rs_232 = re.compile('rs.232', flags=re.IGNORECASE)
wlan_integriert = re.compile('wlan.{0,15}?integriert', flags=re.IGNORECASE)
bluetooth = re.compile('bluetooth.{0,5}?\d?\.?\d?', flags=re.IGNORECASE)
wireless_hd = re.compile('wireless hd', flags=re.IGNORECASE)

	#Abmessungen

abmessungen = re.compile('\d\d\d\.?\d?x\d\d\d?\.?\d?x\d\d\d\.?\d?mm')

	#Gewicht

gewicht = re.compile('\d\d?\.?\d?\d?kg')

	#Besonderheiten

ready_3d = re.compile('\b3D')
upscaling_4k = re.compile('4k upscaling', flags=re.IGNORECASE)
akku = re.compile('akku', flags=re.IGNORECASE)
cardreader = re.compile('cardreader|sdhc|sdxc|\bsd\b|microsd([hx])?c?', flags=re.IGNORECASE)
hdbaset = re.compile('hdbaset', flags=re.IGNORECASE)
hdr = re.compile('hdr\d?\d?', flags=re.IGNORECASE)
hlg = re.compile('\bhlg\b', flags=re.IGNORECASE)
integrierte_lautsprecher = re.compile('lautsprecher', flags=re.IGNORECASE)
intel_wireless_display = re.compile('intels wireless display', flags=re.IGNORECASE)
miracast = re.compile('miracast', flags=re.IGNORECASE)
airplay = re.compile('airplay', flags=re.IGNORECASE)
nfc = re.compile('\bNFC\b')
mediaplayer = re.compile('mediaplayer', flags=re.IGNORECASE)
rec_709_2020 = re.compile('rec.? 709|rec.? 2020', flags=re.IGNORECASE)


#Gefundene Einträge in das beamer_template  einfügen

if dlp is not None:
	beamer_template['Typ'] = 'DLP'
elif lcd is not None:
	beamer_template['Typ'] = 'LCD'
elif lcos is not None:
	beamer_template['Typ'] = 'LCOS'
else:
	beamer_template['Typ'] = 'keine Angabe'













#Template für die Zwischenablage
beamer_template_fertig = '''
Typ: {0}
Chips: {1}
Auflösung (darstellbar): {2}
Auflösung (nativ): {2}
Helligkeit: {3}
Kontrast: {4}
Bildverhältnis: {5}
Bilddiagonale: {6}
Projektionsabstand: {7}
Projektionsverhältnis: {8}
Lampenlebensdauer: {9}
Geräuschentwicklung: {10}
Lens-Shift: {11}
Anschlüsse: {12}
Stromverbrauch: {13}
Abmessungen (BxHxT): {14}
Gewicht: {15}
Besonderheiten: {16}
Herstellergarantie: {17}
'''.format(beamer_template['Typ'], beamer_template['Chips'], beamer_template['Auflösung'], beamer_template['Helligkeit'], beamer_template['Kontrast'], beamer_template['Bildverhältnis'], beamer_template['Bilddiagonale'], beamer_template['Projektionsabstand'], beamer_template['Projektionsverhältnis'], beamer_template['Lampenlebensdauer'], beamer_template['Geräuschentwicklung'], beamer_template['Lens-Shift'], beamer_template['Anschlüsse'], beamer_template['Stromverbrauch'], beamer_template['Abmessungen'], beamer_template['Gewicht'], beamer_template['Besonderheiten'], beamer_template['Herstellergarantie'])

#Kopiert das beamer_template_fertig in die Zwichenablage
pyperclip.copy(beamer_template_fertig)

