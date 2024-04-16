import pywhatkit

numbers = ["+573137297983"]

for number in numbers:
    try:
        pywhatkit.sendwhatmsg_instantly(
            number, "Buenos días desde el cuarto chatbot que programo esta semana en Python.")

    except:
        print("No se pudo encontrar el número")