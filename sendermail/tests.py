from django.core import mail
from django.template.loader import render_to_string
from django.test import TestCase

from sendermail.base import BaseMail


class BaseMailTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.context = {
            "body_message": "Body Message 1",
            "footer_message": "Footer Message 1",
            "recipient": "Recipient 1",
        }
        cls.base_mail = BaseMail(
            subject="Subject Test", to=["test@com.br"], context=cls.context
        )

    def setUp(self) -> None:
        super().setUp()
        self.base_mail.send_alternative()

    def test_should_return_one_mail(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subject_should_be_configured_correctly(self):
        self.assertEqual("Subject Test", mail.outbox[0].subject)

    def test_should_return_one_alternative(self):
        self.assertEqual(1, len(mail.outbox[0].alternatives))

    def test_body_message_should_be_in_body_html(self):
        self.assertIn("Body Message 1", mail.outbox[0].alternatives[0][0])

    def test_subject_should_be_in_body_html(self):
        self.assertIn("Subject Test", mail.outbox[0].alternatives[0][0])

    def test_body_message_should_be_in_body_text(self):
        self.assertIn("Body Message 1", mail.outbox[0].body)

    def test_footer_message_should_be_in_body_html(self):
        self.assertIn("Footer Message 1", mail.outbox[0].alternatives[0][0])

    def test_footer_message_should_be_in_body_text(self):
        self.assertIn("Footer Message 1", mail.outbox[0].body)

    def test_recipient_should_be_in_body_html(self):
        self.assertIn("Recipient 1", mail.outbox[0].alternatives[0][0])

    def test_recipient_should_be_in_body_text(self):
        self.assertIn("Recipient 1", mail.outbox[0].body)

    def test_body_html_should_return_correctly(self):
        expected = render_to_string("sendermail/mail.html", self.context)
        self.assertEqual(expected, mail.outbox[0].alternatives[0][0])

    def test_body_text_should_return_correctly(self):
        expected = render_to_string("sendermail/mail.txt", self.context)
        self.assertEqual(expected, mail.outbox[0].body)
