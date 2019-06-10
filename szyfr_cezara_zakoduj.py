d = "Potrzeba pasji i zaangażowania, żeby naprawdę dogłębnie coś zrozumieć, przeżuć, a nie tylko szybko przełknąć. Większość ludzi nie poświęca na to czasu"

kod = d.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")

print (d.translate(kod))