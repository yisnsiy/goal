# height 162.3mm
# width 77.2mm
# resolution 1080*2340 recommend 270:585
# buildozer -v android debug
import os
from datetime import date, datetime

import pandas as pd
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.fitimage import FitImage

from src.config import MyConfig
from src.data_table import MyDataTable, NewDataScreen
from src.progress_bar import find_ProgressBarFlow
from src.projects.abstarct_page import AbstarctPage
from src.yuebo import ClassMate

def csv2dict(df):
    projects = {}
    for i in range(df.shape[0]):
        key = f"{df.loc[i, 'project']}"
        projects[key] = df.iloc[i].to_dict()
        # change tiem's format
        projects[key]['start_time'] = datetime.strptime(
            projects[key]['start_time'],
            "%Y/%m/%d"
        ).date()
        projects[key]['end_time'] = datetime.strptime(
            projects[key]['end_time'],
            "%Y/%m/%d"
        ).date()

    return projects

class MyApp(MDApp):
    def __init__(self, data):
        super(MyApp, self).__init__()
        self.conf = data

    def on_swip(self, swiper):
        current_swiper_item = swiper.get_current_item()
        print(f'on {current_swiper_item}')
        widget = find_ProgressBarFlow(current_swiper_item)
        if widget is not None:
            print("test on_swip in")
            widget.value = 0
            Clock.schedule_interval(widget.update_progress, 0.08)

    def build(self):
        # Window.size = [77.2 * 5, 162.3 * 5]
        Window.size = [162.3 * 5, 77.2 * 5]
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        now = date.today()
        date_mon_day = str(now.month) + '-' + str(now.day)

        sm = MDScreenManager()
        sm.data = self.conf

        

        my_swiper = MDSwiper(
            size_hint=(1, 1),
            items_spacing='10dp',
            on_swipe=self.on_swip,
        )

        # for fun-----------------
        # my_swiper.add_widget(
        #     MDSwiperItem(
        #         ClassMate('Yue')
        #     )
        # )
        # ------------------------

        for key, value in self.conf.items():
            my_swiper.add_widget(
                MDSwiperItem(
                    AbstarctPage(self.conf[key], date_mon_day)
                )
            )
        my_swiper.add_widget(
            MDSwiperItem(
                MyDataTable(self.conf)
            )
        )

        main = MDScreen(
            my_swiper,
            MDLabel(
                text='[color=#CCCCCC][i][size=18]Annual Goals in 2024[/size][/i][/color]',
                markup=True,
                halign='center',
                theme_text_color='Secondary',
                pos_hint={'center_y':0.02}
            ),
            name='main'
        )
        sm.add_widget(main)

        new_data_screen = NewDataScreen(
            name='new_data'
        )
        sm.add_widget(new_data_screen)

        sm.current = 'main'

        return sm


if __name__ == '__main__':
    cur_dir = os.path.join(os.getcwd(), 'src')
    projects = pd.read_csv(os.path.join(cur_dir, 'data.csv'), sep=',')
    data = csv2dict(projects)
    # # data =MyConfig().projects
    app = MyApp(data)
    app.run()
