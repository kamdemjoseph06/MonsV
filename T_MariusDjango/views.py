from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q,F
from ClubFoot.models import inscription,img,Vid,imgVidUser,Infomedia,Doc
from django.core.paginator import Paginator
from datetime import date,time,timezone,datetime

#help(date)

# Create your views here.

def accueil(request):
    imGs=img.objects.all().order_by('-datePub')[:2]
    vids=Vid.objects.all().order_by('-datePub')[:2]
    infos=Infomedia.objects.all().order_by('-datePub')
    context={
        'imGs':imGs,
        'vids':vids,
        'infos':infos,
    }
    return render(request,'Accueil.html',context)

def Inscription(request):
    if request.method == "POST":
        nomsInscrii=request.POST.get('Noms')
        prenomInscrii=request.POST.get('Prenom')
        dateInscrii=request.POST.get('dateBirth')
        codeInscrii=request.POST.get('Code')
        MotPasseInscrii=request.POST.get('MotPasse')

        if (not nomsInscrii or not prenomInscrii or not dateInscrii or not codeInscrii or not MotPasseInscrii):  #nomsInscrii=='' or nomsInscrii==None and prenomInscrii=='' or prenomInscrii==None and dateInscrii=='' or dateInscrii==None and codeInscrii=='' or codeInscrii==None and MotPasseInscrii=='' or MotPasseInscrii==None
            # msg='Veuillez remplir tous les champs'
            return render(request, "inscription.html", {"msg": msg})
        elif inscription.objects.filter(noms=nomsInscrii,prenoms=prenomInscrii,dateBirth=dateInscrii,codeClub=codeInscrii,pwdClub=MotPasseInscrii).exists():
            msg="L'utilisateur existe dejà"
            return render(request, "inscription.html", {"msg": msg})
        elif inscription.objects.filter( (Q(codeClub=codeInscrii) & Q(pwdClub=MotPasseInscrii)) ).exists():
            msg="Ses identifiants existent dejà"
            return render(request, "inscription.html", {"msg": msg})
        else:
            inscription.objects.create(noms=nomsInscrii,prenoms=prenomInscrii,dateBirth=dateInscrii,codeClub=codeInscrii,pwdClub=MotPasseInscrii)
            msg = "Inscription réussie"
            return render(request, "inscription.html", {"msg": msg})
    return render(request,'Inscription.html')  #,context


def Connection(request):
    NomUserr=request.POST.get('NomUsers')
    PassUserr=request.POST.get('PassUsers')

    if NomUserr=='' or PassUserr=='' and NomUserr==None  or PassUserr==None:
        # msg="Identifiants incorrects"
        # return render(request,'Connection.html',{"msg": msg})
        pass 
    requestNomUser=inscription.objects.filter( (Q(noms=NomUserr) & Q(codeClub=PassUserr)) |
    (Q(noms=NomUserr) & Q(pwdClub=PassUserr)) |
    (Q(prenoms=NomUserr) & Q(codeClub=PassUserr)) |
    (Q(prenoms=NomUserr) & Q(pwdClub=PassUserr)))
    if requestNomUser.exists():
        return redirect('/Actualite/')#render(request,'Actualite.html')
    else:
        msg="Veuillez-vous inscrire si pas encore fait..."
        return render(request,'../templates/Connection.html',{"msg": msg})
    #return render(request,'../templates/Connection.html')
   

def Evenement(request):
    #################################IMAGES
    # Images MPVE
    imgsMPVE=img.objects.filter(titre__iexact="MPVE").order_by('-datePub')  #.all() 
    #Paginator
    paginator=Paginator(imgsMPVE,3)
    page_number=request.GET.get('pageimgsMPVE')
    page_objImgMPVE=paginator.get_page(page_number)

    # Images Footing
    imgsFooting=img.objects.filter(titre__iexact="Footing").order_by('-datePub')  #.all() 
    #Paginator
    paginator=Paginator(imgsFooting,3)
    page_number=request.GET.get('pageimgsFooting')
    page_objImgFooting=paginator.get_page(page_number)

    # Images Soirée Culturel
    imgsSoireeCulturel=img.objects.filter(titre__iexact="Soirée Culturel").order_by('-datePub')  #.all() 
    #Paginator
    paginator=Paginator(imgsSoireeCulturel,3)
    page_number=request.GET.get('pageimgsSC')
    page_objImgSoireeCulturel=paginator.get_page(page_number)

    #################################VIDEOS
    # videos MPVE
    vids=Vid.objects.filter(titre__iexact="MPVE").order_by('-datePub')   #.all()
    #Paginator
    paginator=Paginator(vids,2)
    page_number=request.GET.get('pagevidsMPVE')
    page_obj=paginator.get_page(page_number)

    # videos Footing
    vidsFooting=Vid.objects.filter(titre__iexact="Footing").order_by('-datePub')   #.all()
    #Paginator
    paginator=Paginator(vidsFooting,2)
    page_number=request.GET.get('pagevidsFooting')
    page_objFooting=paginator.get_page(page_number)

    # videos Soirée Culturel
    vidsSoireeCulturel=Vid.objects.filter(titre__iexact="Soirée Culturel").order_by('-datePub')   #.all()
    #Paginator
    paginator=Paginator(vidsSoireeCulturel,2)
    page_number=request.GET.get('pagevidsSC')
    page_objSoireeCulturel=paginator.get_page(page_number)

    # Rapport d Activité
    documents=Doc.objects.order_by('-datePub')
    #################################

    context={
        #'imgs':imgs,
        'page_objImgMPVE':page_objImgMPVE,
        'page_objImgFooting':page_objImgFooting,
        'page_objImgSoireeCulturel':page_objImgSoireeCulturel,
        'page_obj':page_obj,
        'page_objFooting':page_objFooting,
        'page_objSoireeCulturel':page_objSoireeCulturel,
        'documents':documents,
        #'vids':vids,
    }
    return render(request,'Evenement.html',context)   

def Actualite(request):
    imG=img.objects.all().order_by('-datePub')
    imGGs=imG[0]
    x=imGGs.datePub.date()
    imGs=img.objects.filter(datePub__contains=x)
    #Paginator
    paginator=Paginator(imGs,3)
    page_number=request.GET.get('pageimGs')
    page_objImg=paginator.get_page(page_number)
    
    #############
    vid=Vid.objects.all().order_by('-datePub')#
    vidds=vid[0]
    x=vidds.datePub.date()
    vids=Vid.objects.filter(datePub__contains=x)
    #Paginator
    paginator=Paginator(vids,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    #############
    
    info=Infomedia.objects.all().order_by('-datePub')
    infoos=info[0]
    x=infoos.datePub.date()
    infos=Infomedia.objects.filter(datePub__contains=x)
    
    context={
        'imGs':imGs,
        'vids':vids,
        'page_objImg':page_objImg,
        'page_obj':page_obj,
        'infos':infos,
    }
    return render(request,'Actualite.html',context)     

def historique(request):
    uzer=inscription.objects.all().order_by('-datePub')
    documents=Doc.objects.all().order_by('-datePub')
    context={
        'uzer':uzer,
        'documents':documents,
    } 
    return render(request,'Historique.html',context)     