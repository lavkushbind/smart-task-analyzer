from django.test import TestCase
from .scoring import calculate_priority_score
from datetime import date, timedelta

class ScoringAlgorithmTests(TestCase):
    
    def test_overdue_task_high_score(self):
        """Test 1: Agar date nikal gayi hai, toh score high hona chahiye"""
        past_date = str(date.today() - timedelta(days=5))
        task = {
            'due_date': past_date,
            'importance': 5,
            'estimated_hours': 2
        }
        score = calculate_priority_score(task)
        self.assertGreater(score, 100, "Overdue task ka score 100 se zyada hona chahiye")

    def test_future_task_lower_score(self):
        """Test 2: Agar date next year hai, toh score kam hona chahiye"""
        future_date = str(date.today() + timedelta(days=365))
        task = {
            'due_date': future_date,
            'importance': 5,
            'estimated_hours': 2
        }
        score = calculate_priority_score(task)
        self.assertLess(score, 50, "Future task ka score kam hona chahiye")

    def test_high_importance_boost(self):
        """Test 3: High importance task ka score zyada hona chahiye"""
        today = str(date.today())
        
        task_important = {'due_date': today, 'importance': 10, 'estimated_hours': 1}
        task_normal = {'due_date': today, 'importance': 1, 'estimated_hours': 1}
        
        score_imp = calculate_priority_score(task_important)
        score_norm = calculate_priority_score(task_normal)
        
        self.assertGreater(score_imp, score_norm, "Importance badhane se score badhna chahiye")