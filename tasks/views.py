from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scoring import calculate_priority_score

@api_view(['POST'])
def analyze_tasks(request):
    tasks_data = request.data
    if not isinstance(tasks_data, list):
        tasks_data = [tasks_data]

    processed_tasks = []
    
    for task in tasks_data:
        # Score aur Reason dono unpack karo
        score, explanation = calculate_priority_score(task)
        task['score'] = score
        task['explanation'] = explanation
        processed_tasks.append(task)
    
    # Default Sort: Highest Score First
    processed_tasks.sort(key=lambda x: x['score'], reverse=True)
    
    return Response(processed_tasks)

@api_view(['POST'])
def suggest_tasks(request):
    """
    Returns only the Top 3 tasks for 'Today'
    """
    tasks_data = request.data
    if not isinstance(tasks_data, list):
        tasks_data = [tasks_data]

    processed_tasks = []
    for task in tasks_data:
        score, explanation = calculate_priority_score(task)
        task['score'] = score
        task['explanation'] = explanation
        processed_tasks.append(task)

    # Sort and take top 3
    processed_tasks.sort(key=lambda x: x['score'], reverse=True)
    top_3 = processed_tasks[:3]
    
    return Response(top_3)