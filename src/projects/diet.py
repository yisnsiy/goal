from projects.abstarct_page import AbstarctPage

class Diet(AbstarctPage):
    def __init__(self, conf, today_mon_day, **kwargs):
        super(Diet, self).__init__(conf, today_mon_day, **kwargs)
    
    # def calculate_progress_of_time(start: date, end: date):
    #     return super().calculate_progress_of_time(end)
    
    # def calculate_progress_of_target(current, target):
    #     return super().calculate_progress_of_target(target)