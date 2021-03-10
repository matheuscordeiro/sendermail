# Sender Mail

    This package allows to send emails using templates of Django easier. Some Email Services 
    does not format html in body emails. So, in Django, it is necessary to send message 
    in html format and text plain format both. With sender_mail, you can do that with 
    a little code.

## Requirements

    Python = [3.6, 3.7, 3.8, 3.9]
    Django = 3.0.8

## Installation

```
pip install git+https://github.com/matheuscordeiro/sendermail.git@master#egg=sendermail
```

## Usage
```
sender = SenderMail(
    subject="Subject Test",
    to=["test@com.br"],
    context={
        "body_message": "Body Message",
        "footer_message" "Footer Message"
        "recipient": "Recipient",
    }
)
sender.send()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
