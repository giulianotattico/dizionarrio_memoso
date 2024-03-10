dizionario_memoso = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
            
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola.upper() in dizionario_memoso.keys():
    print(parola.upper(), dizionario_memoso[parola.upper()])
