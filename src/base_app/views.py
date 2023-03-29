from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib import messages

from base_app.forms import UploadMT940Form
from base_app.utils import MT940DBParser


def index(request):
    return HttpResponseRedirect("/mt940/upload/")


@login_required
def upload_file(request):
    # Check if the user is a treasurer or a superuser
    if not request.user.is_treasurer and not request.user.is_superuser:
        raise PermissionDenied("You are not authorized to view this page.")
    
    if request.POST:
        # Feed the form with the POST data
        form = UploadMT940Form(request.POST, request.FILES)
        if form.is_valid():
            # Get all the files from the form
            files = request.FILES.getlist("file")
            for file in files:
                # Checking if the file is not too big (more than 2.5 MB)
                if not file.multiple_chunks():
                    try:
                        handler = MT940DBParser(file)
                        handler.save_to_sql_db()
                        handler.save_to_nosql_db()
                        # Add a success message
                        messages.success(request, f"File \"{file.name}\" uploaded successfully.")
                    except Exception as e:
                        # Add an error message if something goes wrong
                        messages.error(request, f"File \"{file.name}\" could not be uploaded. Error: {e}")
                else:
                    # Add an error message if the file is too big
                    messages.error(request, f"File \"{file.name}\" is too big.")
    else:
        # If GET method or any other method called, return an empty form
        form = UploadMT940Form()
    
    return render(request, "base_app/upload_transaction.html", {"form": form})
