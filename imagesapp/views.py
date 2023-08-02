from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from actionsapp.utils import create_action
from imagesapp.forms import ImageCreateForm
from imagesapp.models import Image


@login_required
def image_create(request):
    if request.method == "POST":
        # форма отправлена
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # Назначить текущего пользователя элементу
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Image added successfully!")
            create_action(request.user, "bookmarked image", new_image)

            # Перенаправить к представлению детальной
            # информации о только, что созданном элементе
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными, предоставленными букмарком методом GET
        form = ImageCreateForm(data=request.GET)

    return render(request, "imagesapp/image/create.html", {"section": "images", "form": form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, "imagesapp/image/detail.html", {"section": "images", "image": image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.user_like.add(request.user)
                create_action(request.user, "likes", image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Image.DoesNotExist:
            pass
    return JsonResponse({"status": "error"})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get("page")
    images_only = request.GET.get("images_only")
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse("")
        images = paginator.page(paginator.num_pages)

    if images_only:
        return render(request, "imagesapp/image/list_images.html", {"section": "images", "images": images})

    return render(request, "imagesapp/image/list.html", {"section": "images", "images": images})
