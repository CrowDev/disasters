from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
import json
import requests
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1


class Analize(View):
	def get_concept(request):
		natural_language_understanding = NaturalLanguageUnderstandingV1(
    		version='2018-11-16',
    		iam_apikey='VUJWvResSognuEFqEu3GAi_mBcR1fmFvrce-5JRWLhqr',
    		url='https://gateway.watsonplatform.net/natural-language-understanding/api'
			)

		response = natural_language_understanding.analyze(
    	url='https://docs.djangoproject.com/en/2.2/topics/db/queries/',
    	features=Features(concepts=ConceptsOptions(limit=20))).get_result()
		data = json.dumps(response, indent=2)
		print(json.dumps(response, indent=2))
		return JsonResponse(json.loads(data), safe=False)
		#return HttpResponse(json.dumps(response, indent=2))

	def get_data(request):
		#url = 'https://api.twitter.com/1.1/search/tweets.json?q=earthquakeLA&count=100'
		disasters = ['earthquake', 'volcano', 'hurricane', 'wildfire', 'storm', 'flood', 'tsunami', 'seaquake', 'asap', 'epstein', 'marreta', '#七夕の願い事']
		url = 'https://api.twitter.com/1.1/trends/place.json?id=1'

		# Using OAuth1Session
		oauth = OAuth1('g63VYD1tcsKrRDK681Zm9oYxe',
                          client_secret='AJVqXo9jhGqhBgRVGvF7WEFkIC0TDQ043jVCkJawAwQ6wfmjaZ',
                          resource_owner_key='1147227417238310912-8Tnh5yLnESeBEScwUPWZ5WRbDDKz7S',
                          resource_owner_secret='7AunyrMGGmBe0jO8Xji8IPPUdHaMqVevdsw9NLV36gWzU')


		# Using OAuth1 auth helper
		#obtener trends globales
		r = requests.get(url=url, auth=oauth)
		trends = r.json()
		for disaster in disasters:
			for trend in trends[0]['trends']:
				search = trend['url']
				search_params = search.split('?')
				params = search_params[1].lower()
				if disaster in params:
					print("holi")
					print(params)
					search_url = 'https://api.twitter.com/1.1/search/tweets.json?'+params
					r = requests.get(url=search_url, auth=oauth)
		search = trends[0]['trends'][0]['url']
		#obtener parametros de busqueda de tweets
		search_params = search.split('?')
		search_url = 'https://api.twitter.com/1.1/search/tweets.json?'+search_params[1]
		r = requests.get(url=search_url, auth=oauth)
		twits = r.json()
		texto = ''
		for twit in twits['statuses']:
			texto = texto + twit['text']
		data = json.dumps(twits, indent=2)

		natural_language_understanding = NaturalLanguageUnderstandingV1(
    		version='2018-11-16',
    		iam_apikey='VUJWvResSognuEFqEu3GAi_mBcR1fmFvrce-5JRWLhqr',
    		url='https://gateway.watsonplatform.net/natural-language-understanding/api'
			)

		response = natural_language_understanding.analyze(
    	text=texto,
    	features=Features(concepts=ConceptsOptions(limit=20))).get_result()
		data = json.dumps(response, indent=2)
		print(json.dumps(response, indent=2))
		return JsonResponse(json.loads(data), safe=False)







































		return JsonResponse(json.loads(data), safe=False)
    	