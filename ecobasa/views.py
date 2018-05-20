# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import RedirectView, View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)
from django.views.generic.list import ListView
