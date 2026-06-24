from survey import AnonymousSurvey

question = "What lenguages do you know?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' when you want to quit.")

while True:
    response = input()
    if response == "q":
        break
    else:
        language_survey.store_response(response)
print("\nThank you for participation in the survey!")
language_survey.show_results()
