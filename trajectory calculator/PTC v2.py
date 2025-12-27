import ttkbootstrap as tb
from math import *
import parabolaCalc as PC
from parabolaCalc import g
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# --- Setup main window ---
app = tb.Window(themename="flatly")
app.title("Projectile Trajectory Calculator")
app.geometry("500x550")

# Grid configuration for resizing
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)

# --- Title ---
h1 = tb.Label(
    app,
    text="Projectile Trajectory Calculator",
    font=("Helvetica", 18, "bold"),
    bootstyle="secondary"
)
h1.grid(row=0, column=0, columnspan=2, pady=10)

# --- Input: Velocity ---
entryL1 = tb.Label(
    app, text="Initial Velocity (v₀) (m/s):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL1.grid(row=1, column=0, sticky='w', padx=10, pady=5)

entryVel = tb.Entry(app, width=25)
entryVel.grid(row=1, column=1, sticky='ew', padx=10, pady=5)

# --- Input: Angle ---
meterAng = tb.Meter(
    app,
    bootstyle="info",
    subtext="Launch Angle (θ)",
    interactive=True,
    textright="°",
    metertype="full",
    amountused=45,
    amounttotal=90,
    stripethickness=0,
    metersize=150,
)
meterAng.grid(row=2, column=0, columnspan=2, pady=10)

# --- Results Labels ---
results_frame = tb.Labelframe(app, text="Results", bootstyle="secondary")
results_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

lbl_range = tb.Label(results_frame, text="Range (R): -- m", font=("Helvetica", 11))
lbl_range.pack(anchor='w', padx=10, pady=5)

lbl_height = tb.Label(results_frame, text="Max Height (Hmax): -- m", font=("Helvetica", 11))
lbl_height.pack(anchor='w', padx=10, pady=5)

lbl_time = tb.Label(results_frame, text="Time of Flight (T): -- s", font=("Helvetica", 11))
lbl_time.pack(anchor='w', padx=10, pady=5)

# --- Action Function ---
def on_click():
    try:
        v0 = float(entryVel.get())
        angle_deg = float(meterAng.amountusedvar.get())

        # --- Calculations ---
        angle_rad = radians(angle_deg)
        v0x = v0 * cos(angle_rad)
        v0y = v0 * sin(angle_rad)
        T = (2 * v0y) / g
        R = v0x * T
        Hmax = (v0y ** 2) / (2 * g)

        # --- Update Labels ---
        lbl_range.config(text=f"Range (R): {R:.2f} m")
        lbl_height.config(text=f"Max Height (Hmax): {Hmax:.2f} m")
        lbl_time.config(text=f"Time of Flight (T): {T:.2f} s")

        # --- Draw parabola ---
        PC.draw_parabola(angle_deg, v0)

    except ValueError:
        Messagebox.show_error("Please enter valid numeric values.", title="Input Error")

# --- Button ---
enterbut = tb.Button(app, text="Calculate & Draw", bootstyle="success", command=on_click)
enterbut.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

app.mainloop()
