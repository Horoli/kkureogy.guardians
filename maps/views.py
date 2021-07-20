from django.shortcuts import render
import json
from . import models


def maps(request):
    locations = models.Position.objects.all()
    for position in locations.values():
        if position.get("id") == 1:
            content = {
                "position1_1": position.get("position1_1"),
                "position1_2": position.get("position1_2")
            }
        else:
            pass
    positionJson = json.dumps(content)
    return render(request, "maps/maps.html", {"positionJson":positionJson})
