import string


class stringVar():
    def __init__(self,rating):
        self.rating=rating

    def start(self):
        toy_story=stringVar(8.9)
        bee_movie=stringVar(5.4)
        print(bee_movie.rating)
        print(toy_story.rating)
        
v_ins=stringVar(8)
v_ins.start()