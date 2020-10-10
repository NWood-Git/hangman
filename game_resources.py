animals = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat',
            'clam', 'cobra', 'cougar','coyote', 'crow', 'deer', 'dog', 'donkey',
            'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose hawk',
            'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse',
            'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon',
            'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon',
            'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider ',
            'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle',
            'weasel', 'whale', 'wolf', 'wombat', 'zebra']

tech_companies = ['Amazon', 'Google', 'Facebook', 'Apple', 'Twitter', 'Paypal',
                  'Microsoft', 'Oracle', 'Uber', 'Lyft', 'Spotify', 'Netflix',
                  'Hulu', 'Cisco', 'Salesforce']

fast_food_resturants = ["Burger King", "Taco Bell", "McDonald's", 'Starbucks',
                          "Subway", "Chick-Fil-A", "Wendy's", "Dunkin'", 
                          "Dominos", "Panera Bread", "Pizza Hut", "Chipotle",
                          "KFC", "Sonic", "Arby's", "Dairy Queen", "Popeyes",
                          "Papa John's", "Tim Hortons", "Dos Toros", "Moe's",
                          "White Castle", "Boston Market", "In-N-Out-Burger"]

categories = {'Animal': animals, 'Tech Company' : tech_companies,
                'Fast Food Resturants' :  fast_food_resturants}

hangman_pics= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Animals List and Hangman Drawings:
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Longer List of animals:
# https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a
