from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string


class BaseMail(EmailMultiAlternatives):
    """If you want to customize functions and attributes, you
    should to inherit this class.
    """
    html_template = "sendermail/mail.html"
    txt_template = "sendermail/mail.txt"
    subject = ""
    context = {}

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(subject=self.get_subject(), *args, **kwargs)

    @property
    def _html_message(self):
        return render_to_string(
            template_name=self.get_html_template(),
            context=self.get_context(),
        )

    @property
    def _txt_message(self):
        return render_to_string(
            template_name=self.get_txt_template(),
            context=self.get_context(),
        )

    def get_context(self):
        self.context['subject'] = self.get_subject()
        return self.context

    def get_subject(self):
        return self.subject

    def get_html_template(self):
        return self.html_template

    def get_txt_template(self):
        return self.txt_template

    def send_alternative(self, fail_silently=False):
        send_mail(
            self.get_subject(),
            self._txt_message,
            self.from_email,
            self.to,
            html_message=self._html_message,
            fail_silently=fail_silently,
        )


class SenderMail(BaseMail):
    """If you want to send mail or pass parameters in __init__,
    you should use this class.
    """

    def __init__(
        self,
        context=None,
        subject="",
        html_template="",
        txt_template="",
        *args,
        **kwargs
    ):
        self.subject = subject
        super().__init__(*args, **kwargs)
        self.context = context if context else self.context
        self.html_template = html_template if html_template else self.html_template
        self.txt_template = txt_template if txt_template else self.txt_template
