
from django.contrib.auth.models import User
from rest_framework import serializers
from planets.models import Planet, LANGUAGE_CHOICES, STYLE_CHOICES

class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="planet-highlight", format="html"
    )


    class Meta:
        model = Planet
        fields = (
            "url",
            "id",
            "highlight",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    planets = serializers.HyperlinkedRelatedField(
        many=True, view_name="planet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ("url","id","username","planets")