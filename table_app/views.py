from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'table_app/index.html')

def students_view(request):
    students =[
        {'roll':1,'name':'Atul','marks':90},
        {'roll':2,'name':'Rohit','marks':80},
        {'roll':3,'name':'Raghav','marks':70},
        {'roll':4,'name':'Sonia','marks':60},
        {'roll':5,'name':'Amit','marks':50},
    ]
    context={'data':students}
    return render(request,'table_app/students.html',context)


def player_view(request):
    player=[ {
            'jersey_no': 45,
            'name': 'Rohit Sharma',
            'role': 'Batsman',
            'country': 'India',
            'runs': 6211,
            'matches': 243
        },
        {
            'jersey_no': 63,
            'name': 'Suryakumar Yadav',
            'role': 'Batsman',
            'country': 'India',
            'runs': 3249,
            'matches': 139
        },
        {
            'jersey_no': 93,
            'name': 'Jasprit Bumrah',
            'role': 'Bowler',
            'country': 'India',
            'wickets': 165,
            'matches': 120
        },
        {
            'jersey_no': 33,
            'name': 'Hardik Pandya',
            'role': 'All-rounder',
            'country': 'India',
            'runs': 2309,
            'wickets': 53,
            'matches': 123
        },
        {
            'jersey_no': 99,
            'name': 'Ishan Kishan',
            'role': 'Wicketkeeper-Batsman',
            'country': 'India',
            'runs': 2324,
            'matches': 105
        },
        ]
    context={'players':player}
    return render(request,'table_app/players.html',context)
    
    
