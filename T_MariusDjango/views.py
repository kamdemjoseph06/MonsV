from datetime import date

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse

from ClubFoot.models import Doc, Infomedia, Vid, img, inscription


def accueil(request):
    images = img.objects.all().order_by("-datePub")[:4]
    videos = Vid.objects.all().order_by("-datePub")[:4]
    carousel_items = []

    for image in images:
        if image.image_choisie:
            carousel_items.append({
                "kind": "image",
                "image_choisie": image.image_choisie,
                "caption": image.description or "Photo du Club Mons",
                "date_pub": image.datePub,
            })

    for video in videos:
        if video.video_choisie:
            carousel_items.append({
                "kind": "video",
                "video_choisie": video.video_choisie,
                "caption": video.description or "Vidéo du Club Mons",
                "date_pub": video.datePub,
            })

    carousel_items.sort(key=lambda item: item["date_pub"], reverse=True)
    return render(request, "Accueil.html", {
        "carousel_items": carousel_items,
        "infos": Infomedia.objects.all().order_by("-datePub"),
    })


def Inscription(request):
    message = None
    if request.method == "POST":
        noms = (request.POST.get("Noms") or "").strip()
        prenoms = (request.POST.get("Prenom") or "").strip()
        date_naissance = (request.POST.get("dateBirth") or "").strip()
        code = (request.POST.get("Code") or "").strip()
        mot_de_passe = request.POST.get("MotPasse") or ""

        if not all((noms, prenoms, date_naissance, code, mot_de_passe)):
            message = "Veuillez remplir tous les champs."
        else:
            try:
                naissance = date.fromisoformat(date_naissance)
            except ValueError:
                message = "Veuillez saisir une date de naissance valide."
            else:
                if inscription.objects.filter(
                    noms=noms,
                    prenoms=prenoms,
                    dateBirth=naissance,
                    codeClub=code,
                    pwdClub=mot_de_passe,
                ).exists():
                    message = "L’utilisateur existe déjà."
                elif inscription.objects.filter(codeClub=code, pwdClub=mot_de_passe).exists():
                    message = "Ces identifiants existent déjà."
                else:
                    inscription.objects.create(
                        noms=noms,
                        prenoms=prenoms,
                        dateBirth=naissance,
                        codeClub=code,
                        pwdClub=mot_de_passe,
                    )
                    message = "Inscription réussie. Vous pouvez maintenant vous connecter."

    return render(request, "Inscription.html", {"msg": message})


def Connection(request):
    message = None
    if request.method == "POST":
        nom = (request.POST.get("NomUsers") or "").strip()
        mot_de_passe = request.POST.get("PassUsers") or ""
        if not nom or not mot_de_passe:
            message = "Veuillez saisir votre nom et votre mot de passe."
        else:
            membre = inscription.objects.filter(
                (Q(noms=nom) | Q(prenoms=nom))
                & (Q(codeClub=mot_de_passe) | Q(pwdClub=mot_de_passe))
            ).exists()
            if membre:
                return redirect(reverse("actualite"))
            message = "Identifiants introuvables. Vérifiez vos informations ou inscrivez-vous."

    return render(request, "Connection.html", {"msg": message})


def Evenement(request):
    categories = [
        ("MPVE", "MPVE", "pageimgsMPVE", "pagevidsMPVE"),
        ("Footing", "Footing", "pageimgsFooting", "pagevidsFooting"),
        ("Soirée Culturelle", "Soirée Culturel", "pageimgsSC", "pagevidsSC"),
    ]
    galleries = []
    for title, model_title, image_param, video_param in categories:
        slug = "soiree-culturelle" if model_title.startswith("Soirée") else model_title.lower()
        image_query = img.objects.filter(titre__iexact=model_title).order_by("-datePub")
        video_query = Vid.objects.filter(titre__iexact=model_title).order_by("-datePub")
        image_page = Paginator(image_query, 3).get_page(request.GET.get(image_param))
        video_page = Paginator(video_query, 2).get_page(request.GET.get(video_param))
        galleries.append({
            "title": title,
            "slug": slug,
            "image_page": image_page,
            "video_page": video_page,
            "image_param": image_param,
            "video_param": video_param,
        })

    return render(request, "Evenement.html", {
        "galleries": galleries,
        "documents": Doc.objects.all().order_by("-datePub"),
    })


def Actualite(request):
    latest_image = img.objects.order_by("-datePub").first()
    images = img.objects.none()
    if latest_image:
        images = img.objects.filter(datePub__date=latest_image.datePub.date()).order_by("-datePub")

    latest_video = Vid.objects.order_by("-datePub").first()
    videos = Vid.objects.none()
    if latest_video:
        videos = Vid.objects.filter(datePub__date=latest_video.datePub.date()).order_by("-datePub")

    image_page = Paginator(images, 6).get_page(request.GET.get("pageimGs"))
    video_page = Paginator(videos, 4).get_page(request.GET.get("page"))
    return render(request, "Actualite.html", {
        "page_objImg": image_page,
        "page_obj": video_page,
        "infos": Infomedia.objects.all().order_by("-datePub")[:10],
    })


def historique(request):
    return render(request, "Historique.html", {
        "uzer": inscription.objects.all().order_by("-datePub"),
        "documents": Doc.objects.all().order_by("-datePub"),
    })
