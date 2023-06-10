import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
	print("listning ...")
	recognizer.adjust_for_ambient_noise(source)
	audio = recognizer.listen(source)
	try:
		print("Recognizing...")
		data = recognizer.recognize_google(audio)
		print(data)

	except sr.UnknownValueError:
		print("Not Understand ")
