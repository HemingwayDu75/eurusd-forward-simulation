import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

import tkinter as tk
from tkinter import filedialog

# Paramètres initiaux
taux_eur = 4.00  # taux d'intérêt EUR actuel
taux_us_initial = 3.00  #  taux d'intérêt USD actuel
spot_eurusd = 1.11667  # le spot EUR/USD actuel
start_date = datetime(2024, 8, 27)  # Date de départ

# Fonction pour charger les données avec une boîte de dialogue de sélection de fichier
def load_data():
    # Ouvrir la boîte de dialogue pour sélectionner le fichier CSV
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale de Tkinter
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier CSV",
                                           filetypes=[("Fichiers CSV", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path, sep=';', parse_dates=['date'], dayfirst=False)
        return df
    else:
        print("Aucun fichier sélectionné.")
        return None

# Calculer le nouveau cours à terme avec une baisse des taux aux US
def calculate_forward_rate(spot, taux_eur, taux_us, df, start_date):
    df['cours_a_terme_calculated'] = spot * ((1 + (taux_eur / 100) * (df['date'] - start_date).dt.days / 360) /
                                             (1 + (taux_us / 100) * (df['date'] - start_date).dt.days / 360))
    return df

# Tracer les graphes
def plot_graphs(df, spot, taux_us_baisse_points, start_date):
    plt.figure(figsize=(12, 6))

    # Tracer le spot actuel
    plt.axhline(y=spot, color='blue', linestyle='--', label='Spot EUR/USD actuel')

    # Tracer le cours à terme calculé initial
    df_calculated = calculate_forward_rate(spot, taux_eur, taux_us_initial, df.copy(), start_date)
    plt.plot(df_calculated['date'], df_calculated['cours_a_terme_calculated'], color='orange', label='Cours à terme calculé (initial)')

    # Tracer les cours à terme avec une baisse des taux US
    for baisse in taux_us_baisse_points:
        taux_us_nouveau = taux_us_initial - baisse
        df_baisse = calculate_forward_rate(spot, taux_eur, taux_us_nouveau, df.copy(), start_date)
        plt.plot(df_baisse['date'], df_baisse['cours_a_terme_calculated'],
                 label=f'Cours à terme avec US baisse de {baisse} points')

    # Configurer le graphique
    plt.xlabel('Date')
    plt.ylabel('Cours EUR/USD')
    plt.title('Projection du cours EUR/USD avec hypothèse de baisse des taux US')
    plt.legend()
    plt.grid(True)
    plt.show()

# Points de baisse des taux US à simuler (par exemple 0.25, 0.50, 1.00)
taux_us_baisse_points = [0.25, 0.50, 1.00]

# Charger les données
df = load_data()

# Vérifier si un fichier a été chargé avant de tracer les graphes
if df is not None:
    # Tracer les graphes
    plot_graphs(df, spot_eurusd, taux_us_baisse_points, start_date)
