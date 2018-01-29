# encoding: utf-8
from __future__ import unicode_literals

# Smartphone attributes
DISPLAY_DIAGONAL = 'Display Diagonal in cm'
DISPLAY_TYPE = 'Display Type'
FINGERPRINT_SENSOR = 'Fingerprint sensor'
SIM_FORMAT = 'Format SIM card slot'
MANUFACTURER = 'Manufacturer / Supplier'
RAM = 'Memory (RAM) in GB'
OS = 'Preinstalled operating system'
PROCESSOR = 'Processor performance in GHz'
STANDBY_TIME = 'Stand-by time in Hrs'
TALK_TIME = 'Talk time in Hrs'
COLOR = 'Color'
ITEM_NUMBER = 'Item number'
DATA_STORAGE = 'Data storage in MB'

# Router attributes
DECT = 'DECT base integrated'
DSL = 'DSL modem'
DSL_TELEPHONY = 'DSL telephony (IP-capable)'
#'IP-based connection'
#'IPv6'
#'Internal SO bus'
#'LED-Codes'
NUM_ETHERNET = 'Number of Ethernet ports'
NUM_USB = 'Number of USB ports'
REPEATER = 'Repeater-Mode'
SIZE = 'Size in mm (L x W x H)'
#'Suitable for connection type'
USB_TYPE = 'USB-Type'
#'Universal / ISDN capability'
VDSL = 'VDSL compatible in MBit/s'
NUM_VOICE_CHANNELS = 'Voice channels'
WIFI_STD = 'WiFi standard'
WIFI_ENCRYPTION = 'Wifi-Encryption'



colors = ['schwarz', 'weiss', 'gold']

# iunits of metric attributes, e.g. ARbeits
units = ['cm', 'inch', 'MB', 'GB', 'MBit/s', 'g', 'Hz', 'kHz', 'MHz', 'GHz',
         'minutes', 'hours', 'days']

makes = ['Apple', 'Samsung', 'Sony', 'Google', 'Huawei']

os = ['iOS', 'Android' 'Windows', 'Windows Phone']

sim_formats = ['micro', 'nano']

display_type = ['retina', 'fullHD', 'full-HD', 'full HD']

usb_types = ['USB 2', 'USB 2.0', 'USB 3', 'miniUSB', 'mini-USB', 'mini USB',
             'microUSB', 'micro-USB', 'micro USB']

wifi_std = ['802.11', '802.11a', '802.11ac', '802.11b', '802.11g', '802.11n',
            '802.11 a', '802.11 ac', '802.11 b', '802.11 g', '802.11 n']

wifi_encryption = ['wep', 'wpa', 'wpa2', 'wpa 2']

smartphone_attributes = {
    DISPLAY_DIAGONAL: ['Bildschirmdiagonale', 'Bildschirmgrößen', 'Display-Größen'],
    RAM: ['Arbeitsspeicher', 'RAM'],
    MANUFACTURER: ['Hersteller', 'Herstellern'],
    ITEM_NUMBER: ['Artikelnummer'],
    DATA_STORAGE: ['Speichergröße', 'Speichergrößen', 'Speicher'],
    OS: ['Betriebssystem', 'Betriebssystemen'],
    COLOR: ['Farbe', 'Farben'],
    SIM_FORMAT: ['Sim-Format', 'SIM-Formaten'],
    DISPLAY_TYPE: ['Bildschirm-Typ', 'Display', 'Bildschirm', 'Display-Typ', 'Bildschirm-Typen', 'Display-Typen'],
    PROCESSOR: ['Prozessorleistung', 'Prozessorgeschwindigkeit'],
    TALK_TIME: ['Sprechzeit', 'Sprechdauer'],
    STANDBY_TIME: ['Standby-Zeit'],
    FINGERPRINT_SENSOR: ['Fingerabdrucksensor', 'Fingerabdruckerkennung', 'Einloggen über Fingerabdruck']
}

router_attributes = {
    DECT: ['integrierte DECT-Basis'],
    DSL: ['integriertes DSL Modem'],
    DSL_TELEPHONY: ['DSL-Telefonie'],
    NUM_ETHERNET: ['Anzahl Ethernet-Anschlüsse', 'Ethernet-Anschlüsse', 'Anzahl LAN-Anschlüsse', 'LAN-Anschlüsse',
                   'Anzahl LAN-Buchsen', 'LAN-Buchsen'],
    NUM_USB: ['Anzahl USB-Anschlüsse', 'USB-Anschlüsse', 'Anzahl USB-Buchsen', 'USB-Buchsen'],
    REPEATER: ['Repeater-Mode'],
    SIZE: ['Größe'],
    USB_TYPE: ['USB-Typ', 'USB-Arten', 'USB-Anschlüsse'],
    VDSL: ['VDSL-kompatibel'],
    NUM_VOICE_CHANNELS: ['Anzahl Sprachkanäle', 'Sprachkanäle'],
    WIFI_STD: ['WLAN-Standards', 'WLAN-Standard'],
    WIFI_ENCRYPTION: ['WLAN-Verschlüsselungen', 'WLAN-Verschlüsselung']
}

phone_plurals = {
    'Apple iPhone': ['iPhones'],
    'Samsung Galaxy': ['Galaxies', 'Galaxys']
    # we assume people don't make plurals of other phones...
}

general_device_concepts = {
    'Smartphone': ['Smartphones', 'Smartphone'],
    'Router': ['Router'],
    'Media Receiver': ['Media-Receiver', 'Media Receiver']
}

