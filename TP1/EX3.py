Distance=float(input("donner la distance en en kilomètre :"))
Temps=float(input("donner le temps en minute :"))
Distancem=float(Distance*1000)
Tempss=float(Temps*60)
vitesse = float(Distancem/Tempss)
print(f"la vitesse est donc {vitesse}m/s")