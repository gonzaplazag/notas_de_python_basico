from A11_01_auxiliar_testeo_1 import AnonimousSurvey

# Define a question and make a survey
question = "¿Cuantos hijos tiene?"
my_survey = AnonimousSurvey(question)

my_survey.show_question()

print('Introducir "q" para detener el proceso\n.')
while True:
    response = input('Respuesta : ')
    if response == 'q':
        break
    my_survey.store_response(response)


print("\n Gracias!!)")
my_survey.show_results()
