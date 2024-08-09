def diagnose():
    while True:
        print("What is your primary symptom?")
        symptom = input("Please enter one of following: fever, cough, headache: ").lower()

        if symptom == "exit":
            print("Thank you for using virtual doctor.")
            break

        if symptom == "fever":
            duration = int(input("How many days have you had the fever? "))
            if duration > 3:
                print("You might have a viral infection, therefore it is best to consult a doctor.\n")
            elif duration < 3:
                print("Stay at home, make sure to stay hydrated and monitor your temperature.\n")
            else:
                print("I'm not sure what to do. Please consult a doctor.\n")  

        elif symptom == "cough":
            type_of_cough = input("Is your cough dry or productive? ")
            if type_of_cough == "dry":
                print("You may have a cold. Stay warm and hydrated.\n")
            elif type_of_cough == "productive":
                print("A productive cough is a sign of infection. Consider seeing a doctor.\n")
            else:
                print("I'm not sure what to do. Please consult a doctor.\n")

        elif symptom == "headache":
            headache_type = input("Is is a localized or a general headache? ")
            if headache_type == "localized":
                print("You may have a tension headache. Try to relax and take a pain reliever.\n")
            elif headache_type == "general":
                print("A general headache can be a sign of a more serious condition. Consult a doctor.\n")
            else:
                print("I'm not sure what to do. Please consult a doctor.\n")
        else:
            print("Sorry, I don't know what to do with that symptom. Please consult a doctor for further information.\n")

diagnose()