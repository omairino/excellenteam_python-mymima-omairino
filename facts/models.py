from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} :{self.title }"


class Fact(models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content } :{self.song}"

# import pickle

# dna = pickle.load(open("diname.p", "rb"))
# son = pickle.load(open("disong.p", "rb"))
# for i,x in dna.items():
#     s =  Artist(name=i)
#     s.save()
#     for k in x:
#      m = Song(title=k,artist = s)
#      m.save()
#      t = Fact(content=son[k],song = m)
#      t.save()
# from facts.models import son,Song,Fact,Artist
