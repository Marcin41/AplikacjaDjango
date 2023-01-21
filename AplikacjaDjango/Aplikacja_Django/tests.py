from django.test import TestCase
from .models import Actor, Movie, Rating



class ActorORMTest(TestCase):
    def setUp(self):
        Actor.objects.create(name="Damian", surname="Abram")

    def test_created_category(self):
        actor = Actor.objects.get(name="Damian", surname="Abram")
        self.assertEqual(actor.name, "Damian")
        self.assertEqual(actor.surname, "Abram")

    def test_update_category(self):
        actor = Actor.objects.get(name="Damian")
        actor.name = "Marek"
        actor.save()
        actor_updated = Actor.objects.get(name="Marek")
        self.assertEqual(actor_updated.name, "Marek")



all = Movie.objects.all()

get_filter = Movie.objects.get(title="Top Gun: Maverick")

order_by = Rating.objects.order_by('stars')