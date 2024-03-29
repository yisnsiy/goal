from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock

from kivymd.uix.textfield import MDTextField

from kivymd.uix.button import MDFlatButton

from datetime import datetime
import os
import pandas as pd

from config import MyConfig


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp





projects = {
    "a" : {
        "a1":1
    },
    "b" : {
        "b1":2
    }
}


if __name__ == '__main__':
    for key, value in projects.items():
        print(projects[key])

