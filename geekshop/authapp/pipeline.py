import requests
from social_core.exceptions import AuthForbidden
from django.db import transaction


@transaction.atomic
def get_user_location_and_bio(backend, user, response, *args, **kwargs):
    resp = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": "token %s" % response["access_token"]},
    )
    json = resp.json()

    if not json['location']:
        raise AuthForbidden("social_core.backends.github.GithubOAuth2")

    user.city = json['location']
    user.shopuserprofile.about = json['bio']
    user.save()
