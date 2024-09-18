import re
from datetime import datetime, timedelta

class Calculator:
    def is_valid_time_format(self, time):
        return re.match(r'^\d{2}:\d{2}$', time) is not None

    def format_time(self, time):
        if re.match(r'^\d{4}$', time):
            return f"{time[:2]}:{time[2:]}"
        return time

    def calculate_hours(self, start_time, end_time, break_time='00:00'):
        start_time = self.format_time(start_time)
        end_time = self.format_time(end_time)
        break_time = self.format_time(break_time)

        if not (self.is_valid_time_format(start_time) and self.is_valid_time_format(end_time) and self.is_valid_time_format(break_time)):
            raise ValueError("Formato de horário inválido.")

        fmt = '%H:%M'
        start = datetime.strptime(start_time, fmt)
        end = datetime.strptime(end_time, fmt)
        break_duration = datetime.strptime(break_time, fmt)

        if end < start:
            end += timedelta(days=1)

        worked = end - start
        break_duration = timedelta(hours=break_duration.hour, minutes=break_duration.minute)
        worked -= break_duration

        total_hours = worked.seconds // 3600
        total_minutes = (worked.seconds // 60) % 60

        return f"{total_hours} horas {total_minutes} minutos"
