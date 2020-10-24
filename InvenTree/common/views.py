"""
Django views for interacting with common models
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from InvenTree.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView

from . import models
from . import forms


class CurrencyCreate(AjaxCreateView):
    """ View for creating a new Currency object """

    model = models.Currency
    form_class = forms.CurrencyEditForm
    ajax_form_title = _('Create new Currency')


class CurrencyEdit(AjaxUpdateView):
    """ View for editing an existing Currency object """

    model = models.Currency
    form_class = forms.CurrencyEditForm
    ajax_form_title = _('Edit Currency')


class CurrencyDelete(AjaxDeleteView):
    """ View for deleting an existing Currency object """

    model = models.Currency
    ajax_form_title = _('Delete Currency')
    ajax_template_name = "common/delete_currency.html"


class SettingEdit(AjaxUpdateView):
    """
    View for editing an InvenTree key:value settings object,
    (or creating it if the key does not already exist)
    """

    model = models.InvenTreeSetting
    ajax_form_title = _('Change Setting')
    form_class = forms.SettingEditForm
    ajax_template_name = "common/edit_setting.html"

    def get_context_data(self, **kwargs):
        """
        Add extra context information about the particular setting object.
        """

        ctx = super().get_context_data(**kwargs)

        setting = self.get_object()

        ctx['key'] = setting.key
        ctx['value'] = setting.value
        ctx['name'] = models.InvenTreeSetting.get_setting_name(setting.key)
        ctx['description'] = models.InvenTreeSetting.get_setting_description(setting.key)

        return ctx
