
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# PROJECT_DIR = os.path.join(BASE_DIR, "hackershack_website")

class ProfileView(LoginRequiredMixin, TemplateView):
    # template_name = PROJECT_DIR + "/templates/accounts/profile.html"
    template_name = "accounts/profile.html"
