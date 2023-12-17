from typing import Union

percentage : Union[float, int] = 88
grade : Union[str, None] = None

if percentage >= 88:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
elif percentage >= 33:
    grade = "E"
else:
    grade = "Fail"

    
    