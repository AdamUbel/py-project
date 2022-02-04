from flask import Flask
import stripe

stripe_keys = {
    'secret_key': "sk_test_51KPD3KKwBoDQzGPJKz2mcLOsgE2yS5IQnYgK879LhPlVK4gEZAtUlB7xKOkyhTrdOrcLWjfdFN4QDdoC6QnVeQ2Y00ptBDUeRt",
    'publishable_key': "pk_test_51KPD3KKwBoDQzGPJWasRBxvXtaBUsh8ffFMIEVQb63tmMVM9uVsIM5W5CQpUIAEewhVq8zDQuMp0yAdRV8lN6NgZ00apZNxLjR"
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.secret_key = "Super Secret Key"
