
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ToneAnalyzerV3
import json

from ibm_watson import ApiException
ibm_api_key = "LQFVBrfyfeRF3XidkesTSpuX9wiR7FUUfHKM5M9pk4Cd"


authenticator = IAMAuthenticator(ibm_api_key)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url(
    'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/06c8a17c-56c5-4900-ae17-6bc504f919ae')

# Pottentially need this if it requires the server to do this (no clue tbh)
# tone_analyzer.set_disable_ssl_verification(True)


def get_text_sentiment(text):
    try:
        tone_analysis = tone_analyzer.tone(
            {'text': text},
            content_type='application/json'
        ).get_result()

        return tone_analysis

        # Invoke a Tone Analyzer method
    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
