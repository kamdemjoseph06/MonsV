from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .models import Vid, img, inscription


@override_settings(ALLOWED_HOSTS=["testserver"])
class PublicPagesTests(TestCase):
    def test_all_public_pages_render_with_shared_navigation_and_footer(self):
        for route in ("accueil", "actualite", "evenement", "historique", "inscription", "connection"):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "Navigation principale")
                self.assertContains(response, "data-nav-toggle")
                self.assertContains(response, "KFTJ")
                self.assertContains(response, "site.css")

    def test_home_carousel_has_previous_next_and_pause_controls(self):
        response = self.client.get(reverse("accueil"))
        self.assertContains(response, "data-carousel-previous")
        self.assertContains(response, "data-carousel-next")
        self.assertContains(response, "data-carousel-pause")
        self.assertContains(response, "photos et vidéos du club apparaîtront ici")

    def test_carousel_renders_published_images_and_videos(self):
        img.objects.create(
            titre="Test carousel",
            description="Photo du club",
            image_choisie="IMG-14-09-2025-WA0000.jpg",
            datePub=timezone.now(),
        )
        Vid.objects.create(
            titre="Test carousel",
            description="Vidéo du club",
            video_choisie="static_Vid.mp4",
            datePub=timezone.now(),
        )
        response = self.client.get(reverse("accueil"))
        self.assertContains(response, "/static/staticImg/IMG-14-09-2025-WA0000.jpg")
        self.assertContains(response, "/static/staticVid/static_Vid.mp4")
        self.assertNotContains(response, "data-carousel-next disabled")

    def test_news_pagination_is_visible_and_paginates_photos_and_videos(self):
        now = timezone.now()
        img.objects.create(titre="Actualité", image_choisie="LOGO.jpg", datePub=now)
        single_page = self.client.get(reverse("actualite"))
        self.assertContains(single_page, "Page 1 sur 1")

        for index in range(6):
            img.objects.create(titre=f"Photo {index}", image_choisie="LOGO.jpg", datePub=now)
        for index in range(5):
            Vid.objects.create(titre=f"Vidéo {index}", video_choisie="static_Vid.mp4", datePub=now)

        response = self.client.get(reverse("actualite"), {"pageimGs": "2", "page": "2"})
        self.assertContains(response, "Page 2 sur 2", count=2)
        self.assertContains(response, "pageimGs=1#images")
        self.assertContains(response, "page=1#videos")

    def test_event_pagination_is_restored_for_each_media_type(self):
        now = timezone.now()
        for index in range(4):
            img.objects.create(titre="MPVE", image_choisie="LOGO.jpg", datePub=now)
        for index in range(3):
            Vid.objects.create(titre="MPVE", video_choisie="static_Vid.mp4", datePub=now)

        response = self.client.get(reverse("evenement"), {
            "pageimgsMPVE": "2",
            "pagevidsMPVE": "2",
        })
        self.assertContains(response, "Page 2 sur 2", count=2)
        self.assertContains(response, "pageimgsMPVE=1#mpve-images")
        self.assertContains(response, "pagevidsMPVE=1#mpve-videos")

    def test_empty_news_and_gallery_pages_are_safe(self):
        news = self.client.get(reverse("actualite"))
        events = self.client.get(reverse("evenement"))
        self.assertEqual(news.status_code, 200)
        self.assertEqual(events.status_code, 200)
        self.assertContains(news, "Aucune vidéo récente")
        self.assertContains(events, "MPVE")
        self.assertContains(events, "Soirée Culturelle")

    def test_history_sections_are_filled_and_anchored(self):
        response = self.client.get(reverse("historique"))
        self.assertContains(response, 'id="creation"')
        self.assertContains(response, 'id="statut"')
        self.assertContains(response, 'id="histoire"')
        self.assertContains(response, "La mémoire du Club Mons se construit")
        self.assertContains(response, "Poppins")

    def test_successful_registration_returns_the_correct_template(self):
        response = self.client.post(reverse("inscription"), {
            "Noms": "Essai",
            "Prenom": "Membre",
            "dateBirth": "1980-01-02",
            "Code": "TEST-CODE-001",
            "MotPasse": "TEST-PASS-001",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inscription réussie")
        self.assertEqual(inscription.objects.filter(noms="Essai").count(), 1)
