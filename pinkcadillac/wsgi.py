"""
WSGI config for pinkcadillac project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinkcadillac.settings')

application = get_wsgi_application()

# <div class="movie-details">
#     <h1>{{ movie.name }}</h1>