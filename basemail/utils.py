from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string


class BaseMail(EmailMultiAlternatives):
    context = {}
    html_template = ""
    txt_template = ""

    def __init__(
        self,
        context=None,
        html_template="basemail/mail.html",
        txt_template="basemail/mail.txt",
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.context = context
        self.html_template = html_template
        self.txt_template = txt_template

    @property
    def _html_message(self):
        return render_to_string(
            template_name=self.html_template,
            context=self.context,
        )

    @property
    def _txt_message(self):
        return render_to_string(
            template_name=self.txt_template,
            context=self.context,
        )

    def send_alternative(self, fail_silently=False):
        send_mail(
            self.subject,
            self._txt_message,
            self.from_email,
            self.to,
            html_message=self._html_message,
            fail_silently=fail_silently,
        )
