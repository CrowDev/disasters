from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions, KeywordsOptions

def send_request(texto):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2018-11-16',
		iam_apikey='VUJWvResSognuEFqEu3GAi_mBcR1fmFvrce-5JRWLhqr',
		url='https://gateway.watsonplatform.net/natural-language-understanding/api'
		)
	print(texto)
	response = natural_language_understanding.analyze(
					text=texto,
					features=Features(concepts=ConceptsOptions(limit=100),keywords=KeywordsOptions(limit=10))).get_result()

	return response