import matplotlib.pyplot as plt


class PIRegler:
    def __init__(self, kp, ki, ti, grundlast, pwm_max_ueber):
        self.kp = kp  # Proportionalfaktor
        self.ki = ki  # Integralanteil
        self.ti = ti  # Integralzeitkonstante
        self.integral = 0
        self.grundlast = grundlast  # Nötige konstante Heizleistung
        self.pwm_max = grundlast + pwm_max_ueber  # Begrenzung: Grundlast + 20 PWM-Einheiten

    def regeln(self, sollwert, istwert, dt):
        fehler = sollwert - istwert
        self.integral += (fehler / self.ti) * dt  # Integrieren mit Zeitkonstante

        # PI-Regelung berechnen
        pwm = self.kp * fehler + self.ki * self.integral

        # Begrenzung der PWM-Leistung
        pwm = max(self.grundlast, min(self.pwm_max, pwm))

        return pwm


# Beispielwerte basierend auf dem Modell
kp = 17.423  # Proportionalverstärkung
ki = 1  # Integralfaktor (angenommen, nicht explizit gegeben)
ti = 10.932 * 6  # Integralzeitkonstante
grundlast = 50  # Heizleistung zur Aufrechterhaltung der Solltemperatur
pwm_max_ueber = 20  # Maximal 20 PWM-Einheiten

# Erstelle Regler
regler = PIRegler(kp, ki, ti, grundlast, pwm_max_ueber)

# Beispiel: Temperaturregelung mit Simulation
solltemperatur = 25  # z. B. 25°C
isttemperatur = 20  # Startwert
dt = 1  # Zeitschritt (1 Sekunde)

zeiten = []
temperaturen = []
pwm_werte = []

for i in range(30):  # 30 Zeitschritte simulieren
    pwm = regler.regeln(solltemperatur, isttemperatur, dt)

    # Daten speichern
    zeiten.append(i)
    temperaturen.append(isttemperatur)
    pwm_werte.append(pwm)

    # Simulierte Temperaturänderung durch Heizleistung
    isttemperatur += (pwm - grundlast) * 12 / 50 * 0.1  # Modellierung mit PT1-Glied

# Diagramme erstellen
plt.figure(figsize=(10, 5))

# Temperaturverlauf
plt.subplot(2, 1, 1)
plt.plot(zeiten, temperaturen, label='Ist-Temperatur', color='r')
plt.axhline(y=solltemperatur, color='b', linestyle='--', label='Soll-Temperatur')
plt.xlabel('Zeit (s)')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.title('Temperaturverlauf')

# PWM-Signalverlauf
plt.subplot(2, 1, 2)
plt.plot(zeiten, pwm_werte, label='PWM-Leistung', color='g')
plt.xlabel('Zeit (s)')
plt.ylabel('PWM-Wert')
plt.legend()
plt.title('PWM-Signal')

plt.tight_layout()
plt.show()
