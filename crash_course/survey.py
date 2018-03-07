class AnonymousSurvey():
	def __init__(self, question):
		self.question = question
		self.responses = []
		self.results = {}
		
	def show_question(self):
		print (self.question)
		
	def store_responses (self, new_response):
		self.responses.append(new_response)
		
	def show_results(self):
		print ("Survey Results: ")
		self.tally_results()
		values = sorted(self.results, key=self.results.__getitem__, reverse=True)
		for language in values:
			print ("- " + language + "\t" + str(self.results[language]))
	
	def tally_results(self):
		for x in self.responses:
			if x in self.results.keys():
				self.results[x] += 1
			else:
				self.results[x] = 1
