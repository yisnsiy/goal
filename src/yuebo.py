from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

class ClassMate(MDCard):
    def __init__(self, name, **kwargs):
        super(ClassMate, self).__init__(**kwargs)

        self.name = name
        self.add_widget(
            MDLabel(
                text=f'Phd. {self.name}, when will I be as outstanding as you (the software does not support Chinese yet in current version)\n' + \
f'{self.name} bo, wo shen mei shi hou neng xiang nin zhe mei you xiu:)',
                halign='center',
                # theme_text_color='Primary',
                font_style='H4',
                #rgb 红色
                text_color=(1, 1, 0, 1),
                pos_hint={'center_y': 0.7, 'center_x': 0.5}
            ),
        )