from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string


class BaseMail(EmailMultiAlternatives):
    """If you want to customize functions and attributes, you
    should inherit this class.
    """
    html_template = "sendermail/mail.html"
    txt_template = "sendermail/mail.txt"
    context = {}

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.body = self.body if self.body else self.get_txt_message()
        self.subject = self.get_subject()

    def get_html_message(self):
        return render_to_string(
            template_name=self.get_html_template(),
            context=self.get_context(),
        )

    def get_txt_message(self):
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

    def send(self, fail_silently=False):
        if self.get_html_message():
            self.attach_alternative(self.get_html_message(), 'text/html')

        return super().send(fail_silently)


class SenderMail(BaseMail):
    """If you want to send mail or pass parameters in __init__,
    you should use this class.
    """

    def __init__(
        self,
        context=None,
        html_template="",
        txt_template="",
        *args,
        **kwargs
    ):
        self.context = context if context else self.context
        self.html_template = html_template if html_template else self.html_template
        self.txt_template = txt_template if txt_template else self.txt_template
        super().__init__(*args, **kwargs)
