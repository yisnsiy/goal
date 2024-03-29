from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.progressbar import MDProgressBar


MIN_DISPLAY_DISTANT = 0.25

def find_ProgressBarFlow(widget):
    if isinstance(widget, ProgressBarFlow) and widget.flag != 'Time':
        return widget
    elif hasattr(widget, 'children'):
        for child in widget.children:
            result = find_ProgressBarFlow(child)
            if result is not None:
                return result
    return None

class ProgressBarFlow(MDProgressBar):
    def __init__(self, target_value, flag, **kwargs):
        super(ProgressBarFlow, self).__init__(**kwargs)
        self.value = 0 # initial value
        self.target = target_value # target value
        self.max = 100
        self.flag = flag # time progress or metric progress

        self.update_event = Clock.schedule_interval(self.update_progress, 0.08)
    
    def update_progress(self, time_interval):
        if abs(self.target - self.value) > 1e-3:
            dt = pow(self.target - self.value, 1.02) * 0.04 # dynamicly increate
            # print(f"dt: {dt} target: {self.target} value:{self.value} {abs(self.target - self.value)}")
            self.value += dt
        else:
            self.value = self.target
            self.update_event.cancel()

class ProgressBarwithScale(MDCard):
    def __init__(self, progress, current: str, flag: str):
        super(ProgressBarwithScale, self).__init__()
        
        self.size_hint_x=0.5
        self.orientation='vertical'
        # top_progress_value = max(progress / 100, MIN_DISPLAY_DISTANT)

        print(f"progress: {progress}, current: {current}")
        top_progress = MDBoxLayout(
            MDLabel(
                text=f"{round(progress, 1)}%",
                halign='right',
                # size_hint_x=NumericProperty(max(progress / 100, MIN_DISPLAY_DISTANT)),
                size_hint_x=0.5
                # size_hint_x=top_progress_value
            ),
            orientation='vertical'
        )
        self.add_widget(top_progress)

        middle_bar = MDBoxLayout(
            # MDProgressBar(
            #     value=progress,
            #     color="yellow",
            #     pos_hint={'center_y': 0.5},
            # ),
            ProgressBarFlow(
                target_value=progress,
                flag=flag,
                color="yellow",
                pos_hint={'center_y':0.5},
            ),
            size_hint_x=0.95
        )
        self.add_widget(middle_bar)

        bottom_context = MDBoxLayout(
            MDLabel(
                text=current,
                halign='right',
                # size_hint_x=max(progress / 100, MIN_DISPLAY_DISTANT),
                size_hint_x=0.5
                # size_hint_x=top_progress_value
            ),
            orientation='vertical'
        )
        self.add_widget(bottom_context)

        # MDCard( # progress bar with scale
        #     MDCard(
        #         MDLabel(
        #             text=f"{round(time_progress, 1)}%",
        #             halign='right',
        #             size_hint_x=time_progress / 100,
        #         ),
        #         orientation='vertical',
        #     ),
        #     MDCard(
        #         MDProgressBar(
        #             value=time_progress,
        #             color="yellow",
        #             pos_hint={'center_y': 0.5},
        #         ),
        #         size_hint_x=0.9
        #     ),
        #     MDCard(
        #         MDLabel(
        #             text=date_mon_day,
        #             halign='right',
        #             size_hint_x=time_progress / 100,
        #         ),
        #         orientation='vertical'
        #     ),
            
        #     size_hint_x=0.5,
        #     md_bg_color='orange',
        #     orientation= 'vertical',
        # ),