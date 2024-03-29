import os
from datetime import date

from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel

from src.progress_bar import ProgressBarwithScale

class AbstarctPage(MDCard):
    def __init__(self, conf, today_mon_day, **kwargs):
        super(AbstarctPage, self).__init__(**kwargs)

        # self.size_hint=(0.95, 0.95)
        self.size_hint=(0.95, 0.93)
        self.radius=36
        self.pos_hint={"center_x": .5, "center_y": .52}
        self.elevation=4.5

        self.today_mon_day = today_mon_day
        self.calculate_progress_of_time(
            conf['start_time'],
            conf['end_time'],
        )
        self.calculate_progress_of_target(
            conf['start_value'],
            conf['current_value'],
            conf['target_value'],
        )
        # self.time_progress = None
        # self.target_progress = None
        
        figure_dir = os.path.join(os.getcwd(), 'figure')
        left_picture = FitImage(
            source=os.path.join(figure_dir, conf['left_picture']),
            pos_hint={"left": 1},
            size_hint=(0.4, 1),
            radius=(36, 0, 0, 36),
        )
        self.add_widget(left_picture)

        middle_progress = MDCard(
            MDCard(
                MDLabel( # Title
                    text = conf['project'], 
                    halign = 'center',
                    theme_text_color = 'Primary',
                    font_style = 'H4',
                    pos_hint = {'center_y':0.7} 
                ),
                size_hint_y = 0.5,
            ),
            MDCard(
                MDCard(
                    MDLabel( # Label about target progress
                        text=f"{conf['metric']}",
                        halign = 'center',
                    ),
                    size_hint_x = 0.2
                ),
                ProgressBarwithScale(self.target_progress, str(conf['current_value']), conf['metric']),
                MDCard(
                    MDLabel(
                        text=f"{conf['target_value']}{conf['unit']}",
                        halign = 'center',
                    ),
                    size_hint_x = 0.2
                ),
                size_hint_y = 0.25,
            ),
            MDCard(
                MDCard(
                    MDLabel( # Label about time progress
                        text='Time',
                        halign = 'center',
                    ),
                    size_hint_x = 0.2
                ),
                ProgressBarwithScale(self.time_progress, self.today_mon_day, 'Time'),
                MDCard(
                    MDLabel(
                        text=f"{conf['end_time']}",
                        halign = 'center',
                    ),
                    size_hint_x = 0.2
                ),
                size_hint_y = 0.25,
            ),
            orientation= 'vertical',
            # md_bg_color='blue',
        )
        self.add_widget(middle_progress)

        right_picture = FitImage(
            source=os.path.join(figure_dir, conf['right_picture']),
            size_hint=(0.4, 1),
            pos_hint={"right": 1},
            radius=(0, 36, 36, 0),
        )
        self.add_widget(right_picture)

    def calculate_progress_of_time(self, start: date, end: date):
        total_days = (end - start).days
        elasped_days = (date.today() - start).days
        self.time_progress = elasped_days / total_days * 100

    def calculate_progress_of_target(self, start, current, target):
        self.target_progress = (current - start) / (target - start) * 100


# def food_page(conf):
#     time_progress = calculate_progress_of_time(
#         conf['start_time'],
#         conf['end_time']
#     )
#     now = date.today()
#     date_mon_day = str(now.month) + '-' + str(now.day)

#     target_progress = calculate_progress_of_target(
#         conf['current_value'],
#         conf['target_value'],
#     )


#     return MDScreen(
#         MDCard(
#             FitImage(
#                 source='../figure/body.png',
#                 pos_hint={"left": 1},
#                 size_hint=(0.4, 1),
#                 radius=(36, 0, 0, 36),
#             ),
#             MDCard(
#                 MDCard(
#                     MDLabel( # Title
#                         text = 'Health', 
#                         halign = 'center',
#                         theme_text_color = 'Primary',
#                         font_style = 'H4',
#                         pos_hint = {'center_y':0.7} 
#                     ),
#                     size_hint_y = 0.5,
#                 ),
#                 MDCard(
#                     MDCard(
#                         MDLabel( # Label about target progress
#                             text=f"{conf['metric']}",
#                             halign = 'center',
#                         ),
#                         size_hint_x = 0.2
#                     ),
#                     ProgressBarwithScale(target_progress, str(conf['current_value'])),
#                     MDCard(
#                         MDLabel(
#                             text=f"{conf['target_value']}",
#                             halign = 'center',
#                         ),
#                         size_hint_x = 0.2
#                     ),
#                     size_hint_y = 0.25,
#                 ),
#                 MDCard(
#                     MDCard(
#                         MDLabel( # Label about time progress
#                             text='Time',
#                             halign = 'center',
#                         ),
#                         size_hint_x = 0.2
#                     ),
#                     ProgressBarwithScale(time_progress, date_mon_day),
#                     MDCard(
#                         MDLabel(
#                             text=f"{conf['end_time']}",
#                             halign = 'center',
#                         ),
#                         size_hint_x = 0.2
#                     ),
#                     size_hint_y = 0.25,
#                 ),
#                 orientation= 'vertical',
#                 md_bg_color='blue',
#             ),
#             FitImage(
#                 source='../figure/body.png',
#                 size_hint=(0.4, 1),
#                 pos_hint={"right": 1},
#                 radius=(0, 36, 36, 0),
#             ),
#             size_hint=(0.95, 0.95),
#             radius=36,
#             pos_hint={"center_x": .5, "center_y": .52},
#             elevation=4.5,
#             # focus_behavior=True,
#             # focus_color='grey',
#         ),
#     )