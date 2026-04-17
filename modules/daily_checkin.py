from datetime import datetime, timedelta

class DailyCheckin:
    def __init__(self):
        self.last_checkin = None

    def check_in(self):
        now = datetime.utcnow()
        # Check-in logic
        if self.last_checkin and now - self.last_checkin < timedelta(days=1):
            return "You can only check in once every 24 hours."
        self.last_checkin = now
        return f"Checked in at {now.strftime('%Y-%m-%d %H:%M:%S')} UTC"

    def get_last_checkin(self):
        return self.last_checkin.strftime('%Y-%m-%d %H:%M:%S') if self.last_checkin else "No check-ins yet"
