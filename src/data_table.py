import os
from datetime import date, datetime

import pandas as pd
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.gridlayout import MDGridLayout

is_add = False

def get_sm(widget):
    while not isinstance(widget, MDScreenManager):
        widget = widget.parent
    return widget

class NewDataScreen(MDScreen):
    def __init__(self, **kwargs):
        super(NewDataScreen, self).__init__(**kwargs)
        self.dialog = None
        input_infor = MDBoxLayout(
            MDGridLayout(
                MDTextField(
                    id='project',
                    hint_text="project e.g., Read",
                    mode='rectangle',
                    # size_hint_x = 0.4,
                    # pos_hint = {'left':1},
                ),
                MDTextField(
                    id='left_picture', 
                    hint_text="left_picture e.g., 2.png",
                    mode='rectangle',
                ),
                MDTextField(
                    id='right_picture', 
                    hint_text="right_picture e.g., 1.png",
                    mode='rectangle',
                ),
                cols=3,
                spacing=20,
            ),
            MDGridLayout(
                MDTextField(
                    id='start_time',
                    hint_text="start_time e.g., 2024-2-18",
                    mode='rectangle',
                ),
                MDTextField(
                    id='end_time',
                    hint_text="end_time e.g., 2024-12-30",
                    mode='rectangle',
                ),
                MDTextField(
                    id='start_value',
                    hint_text="start_value e.g., 0",
                    mode='rectangle',
                ),
                cols=3,
                spacing=20,
            ),
            MDGridLayout(
                MDTextField(
                    id='current_value',
                    hint_text="current_value e.g., 3",
                    mode='rectangle',
                ),
                MDTextField(
                    id='target_value',
                    hint_text="target_value e.g., 24",
                    mode='rectangle',
                ),
                MDTextField(
                    id='metric',
                    hint_text="metric e.g., Amount",
                    mode='rectangle',
                ),
                cols=3,
                spacing=20,
            ),
            MDGridLayout(
                MDBoxLayout(
                    MDFlatButton(
                        text="Cancel",
                        size_hint=(0.4,0.4),
                        md_bg_color='gray',
                        on_release=self.switch_main,
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                    ),
                    size_hint_x=0.3
                ),
                MDTextField(
                    id='unit',
                    hint_text="unit e.g., Books",
                    mode='rectangle',
                ),
                MDBoxLayout(
                    MDFlatButton(
                        text="New",
                        size_hint=(0.4,0.4),
                        md_bg_color='gray',
                        on_release=self.new_data
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                    ),
                    size_hint_x=0.3
                ),
                cols=3,
                spacing=20,
            ),
            orientation="vertical",
        )
        self.add_widget(input_infor)
    
    def switch_main(self, instance):
        parent = instance.parent
        while parent and not isinstance(parent, MDScreenManager):
            parent = parent.parent
        parent.current = 'main'
    
    def new_data(self, instance):

        def find_text_filed(widget):
            if isinstance(widget, MDTextField):
                return {widget.id: widget.text}
            elif hasattr(widget, 'children'):
                result = {}
                for child in widget.children:
                    result.update(find_text_filed(child))
                return result

        data = find_text_filed(self)
        if '' in data.values() or self.not_vaild(data):
            self.complete_data()
        else:
            sm = get_sm(self)
            sm.data.update(  # all data
                {data['project']: data}
            )
            self.switch_main(instance)
            global is_add
            is_add = True
    def not_vaild(self, data):
        try:
            start_time = datetime.strptime(data['start_time'],"%Y/%m/%d").date()
            end_time = datetime.strptime(data['end_time'],"%Y/%m/%d").date()

            if start_time >= end_time:
                return True
            figure_dir = os.path.join(os.getcwd(), 'figure')
            left_fig = os.path.join(figure_dir, data['left_picture'])
            right_fig = os.path.join(figure_dir, data['right_picture'])
            if not os.path.exists(left_fig):
                return True
            if not os.path.exists(right_fig):
                return True
        except:
            return True
        return False

    def complete_data(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Please supplement data of each field or Data is unvalid",
                # text=
            )
        self.dialog.open()

class MyDataTable(MDCard):
    def __init__(self, data, *args, **kwargs):
        super(MyDataTable, self).__init__(*args, **kwargs)
        self.orientation='vertical'

        # columns = [(column_name, dp(20)) for column_name in data.columns]
        # rows = [tuple(data.loc[i]) for i in range(len(data))]

        columns = [(column_name, dp(25)) for column_name in next(iter(data.values())).keys()]
        rows = []
        for element in data.values():
            rows.append(tuple(element.values()))

        self.save_dialog = None

        # 创建数据表格
        self.data_table = MDDataTable(
            # size_hint=(1, 1),
            # pos_hint={"center_y": 0.5, "center_x": 0.5},
            column_data=columns,
            rows_num=10,
            row_data=rows,
            use_pagination=True
        )
        self.add_widget(self.data_table)

        buttons = MDGridLayout(
            MDRoundFlatIconButton(
                text="Add Row",
                line_color="orange",
                icon_color="white",
                text_color="white",
                md_bg_color="orange",
                on_release=self.switch_new_data,
            ),
            MDRoundFlatIconButton(
                text="Save",
                line_color="orange",
                icon_color="white",
                text_color="white",
                md_bg_color="orange",
                on_release=self.save_data,
            ),
            MDRoundFlatIconButton(
                text="Remove Row",
                line_color="orange",
                icon_color="white",
                text_color="white",
                md_bg_color="orange",
                on_release=self.remove_row,
            ),
            size_hint_y = 0.12,
            spacing=20,
            cols=3
        )
        self.add_widget(buttons)

    def save_data(self, instance):

        # 获取数据表格的列和行数据
        data = get_sm(instance).data
        columns = next(iter(data.values())).keys()
        rows = []
        for element in data.values():
            rows.append(list(element.values()))
        rows = self.data_table.row_data

        # 创建 DataFrame 对象
        data = pd.DataFrame(rows, columns=columns)

        # 保存数据到 data.csv 文件
        dir = os.path.join(os.getcwd(), 'src')
        data.to_csv(os.path.join(dir, 'data.csv'), index=False)
        self.finshi_saving(instance)

    def finshi_saving(self, instance):
        if not self.save_dialog:
            self.save_dialog = MDDialog(
                title="Finish saving",
                # text=
            )
        self.save_dialog.open()
    
    def switch_new_data(self, instance):
        parent = instance.parent
        while parent and not isinstance(parent, MDScreenManager):
            parent = parent.parent
        parent.current = 'new_data'
        global is_add
        is_add = False
        self.add_event = Clock.schedule_interval(self.add_row, 1)
        
    def add_row(self, instance):
        global is_add
        if is_add is True:
            sm = get_sm(self)
            data = sm.data
            print(f"add row after: {data}")
            last_row_data = list(data.values())[-1]
            specified_keys = [
                'project',
                'left_picture',
                'right_picture',
                'start_time',
                'end_time',
                'start_value',
                'current_value',
                'target_value',
                'metric',
                'unit'
            ]
            self.data_table.add_row(
                tuple(
                    last_row_data[key] for key in specified_keys
                )
            )

            is_add = False
            self.add_event.cancel()

    def remove_row(self, instance):
        if len(self.data_table.row_data) > 1:
            key = self.data_table.row_data[-1][0]
            self.data_table.remove_row(self.data_table.row_data[-1])
            del get_sm(instance).data[key]
            print("remove_row")