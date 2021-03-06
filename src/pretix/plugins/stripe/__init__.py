from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pretix.base.plugins import PluginType


class StripeApp(AppConfig):
    name = 'pretix.plugins.stripe'
    verbose_name = _("Stripe")

    class PretixPluginMeta:
        type = PluginType.PAYMENT
        name = _("Stripe")
        author = _("the pretix team")
        version = '1.0.0'
        description = _("This plugin allows you to receive credit card payments " +
                        "via Stripe")

    def ready(self):
        from . import signals  # NOQA

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import stripe  # NOQA
        except ImportError:
            errs.append("Python package 'stripe' is not installed.")
        return errs


default_app_config = 'pretix.plugins.stripe.StripeApp'
