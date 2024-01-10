from django.shortcuts import render
finches = [
    {'name': 'House Finch', 'description': 'colorful and social', 'habitat': 'urban and suburban areas', 'age': 2},
    {'name': 'Goldfinch', 'description': 'bright yellow plumage', 'habitat': 'open fields and gardens', 'age': 1},
    {'name': 'Zebra Finch', 'description': 'small and active', 'habitat': 'grasslands and open forests', 'age': 3},
    {'name': 'Canary', 'description': 'known for singing', 'habitat': 'captivity, originally from Macaronesian islands', 'age': 2},
    {'name': 'Purple Finch', 'description': 'rich plumage with raspberry color', 'habitat': 'forests and woodlands', 'age': 1},
    {'name': 'Society Finch', 'description': 'sociable and good for aviaries', 'habitat': 'captivity, originally from Asia', 'age': 4},
    {'name': 'Gouldian Finch', 'description': 'vibrantly colored with distinct head colors', 'habitat': 'northern Australia', 'age': 2},
    {'name': 'Java Sparrow', 'description': 'bold black and white markings', 'habitat': 'Java and Bali', 'age': 1},
    {'name': 'Chaffinch', 'description': 'common in Europe', 'habitat': 'forests and gardens', 'age': 3},
    {'name': 'Redpoll Finch', 'description': 'small with red crown and black bib', 'habitat': 'northern regions', 'age': 2},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })