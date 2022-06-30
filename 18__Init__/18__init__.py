class peliculas():
    def __init__(self,titulo,rating,idioma,trailer):
        self.titulo=titulo
        self.rating=rating
        self.idioma=idioma
        self.trailerURL=trailer

toy_story=peliculas("Toy Story",8.9,"Español","https://fokfoekfeo")
print(toy_story.idioma)