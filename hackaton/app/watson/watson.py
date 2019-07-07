from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions

def send_request(texto):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2018-11-16',
		iam_apikey='VUJWvResSognuEFqEu3GAi_mBcR1fmFvrce-5JRWLhqr',
		url='https://gateway.watsonplatform.net/natural-language-understanding/api'
		)

	response = natural_language_understanding.analyze(
					text=texto,
					features=Features(concepts=ConceptsOptions(limit=20))).get_result()

	return response