import pywhatkit

numbers = ["+573137297983"]

for number in numbers:
    try:
        pywhatkit.sendwhatmsg_instantly(
            number, "Buenos días, esta es una prueba del chatbot")

    except:
        print("No se pudo encontrar el número")