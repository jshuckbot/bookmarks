from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from imagesapp.forms import ImageCreateForm


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

            # Перенаправить к представлению детальной
            # информации о только, что созданном элементе
            return redirect(new_image.get_absolute_url())
        else:
            # скомпоновать форму с данными, предоставленными букмарком методом GET
            form = ImageCreateForm(data=request.GET)

        return render(request, "images/image/create.html", {"section": "images", "form": form})
