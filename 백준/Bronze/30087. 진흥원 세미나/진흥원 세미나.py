import sys

class_rooms = {
    'Algorithm': '204',
    'DataAnalysis': '207',
    'ArtificialIntelligence': '302',
    'CyberSecurity': 'B101',
    'Network': '303',
    'Startup': '501',
    'TestStrategy': '105'
}

n = int(sys.stdin.readline())
for _ in range(n):
    print(class_rooms[sys.stdin.readline().rstrip()])
