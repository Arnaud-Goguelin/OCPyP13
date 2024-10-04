from django.shortcuts import render

from profile_app.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):
    """
    Renders the profiles index page displaying a list of all user profiles.

    Args:
        request (HttpRequest): The request object containing metadata about the request.

    Returns:
        HttpResponse: A response object with the rendered HTML template for the profiles index.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profile_app/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Renders the profile page for a specific user based on their username.

    Args:
        request (HttpRequest): The request object containing metadata about the request.
        username (str): The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: A response object with the rendered HTML template for the profile page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile_app/profile.html", context)
