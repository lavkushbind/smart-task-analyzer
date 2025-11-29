from datetime import date, datetime

def calculate_priority_score(task_data):
    """
    Returns: (score, explanation_text)
    """
    today = date.today()
    reasons = []
    
    # 1. Parse Due Date
    try:
        due_date = datetime.strptime(task_data['due_date'], '%Y-%m-%d').date()
        days_left = (due_date - today).days
    except:
        return 0, "Invalid Date"
        
    # 2. Urgency Score
    if days_left < 0:
        urgency_score = 100
        reasons.append(f"🔥 Overdue by {abs(days_left)} days")
    elif days_left == 0:
        urgency_score = 50
        reasons.append("🚨 Due Today")
    elif days_left <= 3:
        urgency_score = 30
        reasons.append("⏰ Due soon")
    else:
        urgency_score = max(0, 20 - days_left)

    # 3. Importance Score (Weight: 3x)
    importance = task_data.get('importance', 1)
    importance_score = importance * 3
    if importance >= 8:
        reasons.append("⭐ High Value")

    # 4. Effort Score (Quick Wins)
    effort = task_data.get('estimated_hours', 1)
    if effort <= 2:
        effort_score = 20
        reasons.append("⚡ Quick Win (< 2h)")
    else:
        effort_score = 10 / max(effort, 1)

    # Total Formula
    total_score = urgency_score + importance_score + effort_score
    
    # Generate Explanation
    explanation = " | ".join(reasons) if reasons else "Routine Task"
    
    return round(total_score, 2), explanation