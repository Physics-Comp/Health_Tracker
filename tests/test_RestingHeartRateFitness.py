import pytest
from features.hs_resting_heart import health_status_resting_heart_rate

class restingHeartTests:
    """
    Testing the core functionality of the resting heart rate class. Determine the health 
    status given an age and resting heartrate
    """
    def test_athlete_one(self):
        athlete = health_status_resting_heart_rate(18,49)
        assert athlete == "Athlete"
    
    def test_excellent_one(self):
        excellent = health_status_resting_heart_rate(36,57)
        assert excellent == "Excellent"
    
    def test_good_one(self):
        good = health_status_resting_heart_rate(56,62)
        assert good == "Good"

    def test_above_avg_one(self):
        above_avg = health_status_resting_heart_rate(26,66)
        assert above_avg == "Above Average"

    def test_avg_one(self):
        avg = health_status_resting_heart_rate(57,73)
        assert avg == "Average"
    
    def test_below_avg_one(self):
        below_avg = health_status_resting_heart_rate(36,77)
        assert below_avg == "Below Average"
    
    def test_poor_one(self):
        poor_health = health_status_resting_heart_rate(18,90)
        assert poor_health == "Poor"
