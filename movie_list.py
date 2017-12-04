import movie
import great_movies

# data for each movie stored in objects of the Movie class

blazing_saddles = movie.Movie(
    "Blazing Saddles",
    "In order to ruin a western town, a corrupt politician appoints a black "
    "sheriff, who promptly becomes his most formidable adversary.",
    "https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=VKayG1TrfuE")

braveheart = movie.Movie(
    "Braveheart",
    "When his secret bride is executed for assaulting an English soldier who "
    "tried to rape her, Sir William Wallace begins a revolt against King "
    "Edward I of England.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=nMft5QDOHek")

coco = movie.Movie(
    "Coco",
    "Aspiring musician Miguel, confronted with his family's ancestral ban on "
    "music, enters the Land of the Dead to work out the mystery.",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xlnPHQ3TLX8")

potter3 = movie.Movie(
    "Harry Potter and the Prisoner of Azkaban",
    "It's Harry's third year at Hogwarts; not only does he have a new 'Defense"
    " Against the Dark Arts' teacher, but there is also trouble brewing. "
    "Convicted murderer Sirius Black has escaped the Wizards' Prison and is "
    "coming after Harry.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=lAxgztbYDbs")

star_trek = movie.Movie(
    "Star Trek",
    "The brash James T. Kirk tries to live up to his father's legacy with Mr. "
    "Spock keeping him in check as a vengeful Romulan from the future creates "
    "black holes to destroy the Federation one planet at a time.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
    "https://www.youtube.com/watch?v=SyJszxnJydA")

strangelove = movie.Movie(
    "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
    "An insane general triggers a path to nuclear holocaust that a war room "
    "full of politicians and generals frantically tries to stop.",
    "https://upload.wikimedia.org/wikipedia/en/e/e6/Dr._Strangelove_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1gXY3kuDvSU")

# list of movie objects to populate the movie tiles on the webpage
movies = [blazing_saddles, braveheart, coco, potter3, star_trek, strangelove]

# generates and opens the webpage via scripts in great_movies.py
great_movies.open_movies_page(movies)
