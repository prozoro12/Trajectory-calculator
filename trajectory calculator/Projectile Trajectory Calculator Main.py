import ttkbootstrap as tb
from math import *
import parabolaCalc as PC
from parabolaCalc import g
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs import Messagebox

#PC.draw_parabola(45, 45, 100, 100)

# Create the main window
app = tb.Window(themename="flatly")  # Try "flatly", "darkly", "solar", etc.
app.title("Prjectile Trajectory Calculator")
app.geometry("500x500")

# Configure grid columns to resize nicely
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)  # make entry side expand more

h1 = tb.Label(app, text="Prjectile Trajectory Calculator", font=("Helvetica", 20), bootstyle="secondary")
h1.grid(row=0, column=0, sticky='w', padx=3, pady=5)

entryL1 = tb.Label(app, text="Intitial Velocity(v0)(m/s): ", font=("Helvetica", 12), bootstyle="success")
entryL1.grid(row=1, column=0, sticky='w', padx=3, pady=5)

entryVel = tb.Entry(app, width=23)
entryVel.grid(row=1, column=0, sticky='e', padx=3, pady=5)

meterAng = tb.Meter(
    app,
    bootstyle="info",
    subtext="Launch Angle(θ)",
    interactive=True,
    textright="DEG",
    metertype="full", #try full
    #startangle=20,
    #endangle=45,
    amountused=30,
    amounttotal=90,
    stripethickness=0, # try 0 not 1
    metersize=150,

)
meterAng.grid(row=2, column=0, sticky='ew', padx=3, pady=5)

def on_click():

    if entryVel.get() != '' or meterAng.amountusedvar.get() != '':
        
        try: 
            angle_deg = float(meterAng.amountusedvar.get())
            v0 = float(entryVel.get())

            # === Calculations ===
            angle_rad = radians(angle_deg)
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)

            T = (2 * v0y) / g
            R = v0x * T
            Hmax = (v0y ** 2) / (2 * g)

            PC.draw_parabola(angle_deg, v0)

        except ValueError:
            Messagebox.show_info('Values entered are empty or incorrect! Please enter Values and try angain', title='ERROR!')

        

    else:
        Messagebox.show_info('Values entered are empty! Please enter Values and try angain', title='ERROR!')
    

enterbut = tb.Button(app, text="Enter", bootstyle="success", command=on_click)
enterbut.grid(row=3, column=0, sticky='ew', padx=10, pady=5)
