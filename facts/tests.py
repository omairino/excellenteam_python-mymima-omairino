from django.test import TestCase
from facts.models import Artist, Song, Fact


class ArtistTestCase(TestCase):
   def test_Arist(self):
       self.assertEqual(Artist.objects.count(), 0)

       a = Artist(
           artist_letter="omair"
       )
       a.save()

       self.assertEqual(Artist.objects.count(), 1)


class SongTestCase(TestCase):
   def test_Song(self):
       self.assertEqual(Artist.objects.count(), 0)

       a = Artist(
           artist_letter="issa"
       )
       a.save()

       self.assertEqual(Artist.objects.count(), 1)

       s1 = Song(
           artist=a,
           song_letter="lovely bird flying"
       )
       s2 = Song(
           artist=a,
           song_letter="lovely bird flying2"
       )
       s1.save()
       s2.save()

       self.assertEqual(Song.objects.count(), 2)
       self.assertEqual(Fact.objects.count(), 0)
       f1 = Fact(fact_letter="this is the first fact",song=s1)

       f2 = Fact(fact_letter="this is the second fact",song=s2)

       f1.save()

       f2.save()
       self.assertEqual(Fact.objects.count(), 2)