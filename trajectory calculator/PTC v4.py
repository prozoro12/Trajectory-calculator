import ttkbootstrap as tb
from math import *
import parabolaCalc as PC
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# --- Setup main window ---
app = tb.Window(themename="solar")   
app.title("Projectile Trajectory Calculator")

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
#h1.grid(row=0, column=0, columnspan=2, pady=10)

# --- Draw Graph Option ---
check_var = tb.BooleanVar()
check_var.set(True)
check = tb.Checkbutton(app, text="Generate Graph", variable=check_var, bootstyle="dark-round-toggle")
check.grid(row=100, column=1, sticky='e', padx=10, pady=10)

# --- Notebook Setup ---
notebook = tb.Notebook(app)
t1 = tb.Frame(notebook)
t2 = tb.Frame(notebook)
notebook.add(t1, text="Parabola")
notebook.add(t2, text="Values")
notebook.grid(row=1, column=0, columnspan=2, pady=10, padx=5)

# --- Input: Velocity ---
entryL1 = tb.Label(
    t1, text="Initial Velocity (v₀) (m/s):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL1.grid(row=2, column=0, sticky='w', padx=10, pady=5)

entryVel = tb.Entry(t1, width=25, bootstyle='danger')
entryVel.grid(row=2, column=1, sticky='ew', padx=10, pady=5)
entryVel.insert(0, '10')

# --- Input: Acceleration due to gravity ---
entrygL2 = tb.Label(
    t1, text="Acceleration due to gravity (g) (m/s²):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entrygL2.grid(row=3, column=0, sticky='w', padx=10, pady=5)

entryg = tb.Entry(t1, width=25, bootstyle='danger')
entryg.grid(row=3, column=1, sticky='ew', padx=10, pady=5)
entryg.insert(0, '9.80665')

# --- Input: Angle (Meter) ---
meterAng = tb.Meter(
    t1,
    bootstyle="primary",
    subtext="Launch Angle (θ)",
    interactive=True,
    textright="°",
    metertype="full",
    amountused=45,
    amounttotal=90,
    stripethickness=0,
    metersize=150,
)
meterAng.grid(row=4, column=0, columnspan=2, pady=10)

# --- Numerics / Values tab ---
entryL2 = tb.Label(t2, text="Initial Velocity (v₀) (m/s):", font=("Helvetica", 12), bootstyle="success")
entryL2.grid(row=2, column=0, sticky='w', padx=10, pady=5)

entryVel2 = tb.Entry(t2, width=25, bootstyle='danger')
entryVel2.grid(row=2, column=1, sticky='ew', padx=10, pady=5)
entryVel2.insert(0, '--')

entryL3 = tb.Label(t2, text="Launch Angle (θ) (°):", font=("Helvetica", 12), bootstyle="success")
entryL3.grid(row=3, column=0, sticky='w', padx=10, pady=5)

entryAngle = tb.Entry(t2, width=25, bootstyle='danger')
entryAngle.grid(row=3, column=1, sticky='ew', padx=10, pady=5)
entryAngle.insert(0, '--')

entryL4 = tb.Label(t2, text="Range (R) (m):", font=("Helvetica", 12), bootstyle="success")
entryL4.grid(row=4, column=0, sticky='w', padx=10, pady=5)

entryRange = tb.Entry(t2, width=25, bootstyle='danger')
entryRange.grid(row=4, column=1, sticky='ew', padx=10, pady=5)
entryRange.insert(0, '--')

entryL5 = tb.Label(t2, text="Max Height (Hmax) (m):", font=("Helvetica", 12), bootstyle="success")
entryL5.grid(row=5, column=0, sticky='w', padx=10, pady=5)

entryH = tb.Entry(t2, width=25, bootstyle='danger')
entryH.grid(row=5, column=1, sticky='ew', padx=10, pady=5)
entryH.insert(0, '--')

entryL6 = tb.Label(t2, text="Time of Flight (T) (s):", font=("Helvetica", 12), bootstyle="success")
entryL6.grid(row=6, column=0, sticky='w', padx=10, pady=5)

entryT = tb.Entry(t2, width=25, bootstyle='danger')
entryT.grid(row=6, column=1, sticky='ew', padx=10, pady=5)
entryT.insert(0, '--')

entryL7 = tb.Label(t2, text="Acceleration due to Gravity (g) (m/s²):", font=("Helvetica", 12), bootstyle="success")
entryL7.grid(row=7, column=0, sticky='w', padx=10, pady=5)

entryg2 = tb.Entry(t2, width=25, bootstyle='danger')
entryg2.grid(row=7, column=1, sticky='ew', padx=10, pady=5)
entryg2.insert(0, '9.80665')

# --- Action Function 1 ---
def on_click1():
    try:
        v0 = float(entryVel.get())
        angle_deg = float(meterAng.amountusedvar.get())
        g = float(entryg.get())

        # --- Calculations ---
        angle_rad = radians(angle_deg)
        v0x = v0 * cos(angle_rad)
        v0y = v0 * sin(angle_rad)
        T = (2 * v0y) / g
        R = v0x * T
        Hmax = (v0y ** 2) / (2 * g)

        # --- Update Numerics tab ---
        entryVel2.delete(0, END)
        entryVel2.insert(0, f"{v0:.3f}")

        entryAngle.delete(0, END)
        entryAngle.insert(0, f"{angle_deg:.3f}")

        entryRange.delete(0, END)
        entryRange.insert(0, f"{R:.3f}")

        entryH.delete(0, END)
        entryH.insert(0, f"{Hmax:.3f}")

        entryT.delete(0, END)
        entryT.insert(0, f"{T:.3f}")

        entryg2.delete(0, END)
        entryg2.insert(0, f"{g:.5f}")

        # --- Update the Meter visually ---
        meterAng.configure(amountused=round(angle_deg))

        # --- Draw parabola ---
        if check_var.get():
            PC.draw_parabola(angle_deg, v0, g)

        # --- Switch to Values tab ---
        notebook.select(t2)

    except ValueError:
        Messagebox.show_error("Please enter valid numeric values.", title="Input Error")

# --- Button 1 ---
enterbut1 = tb.Button(t1, text="Calculate & Draw", bootstyle="success", command=on_click1)
enterbut1.grid(row=5, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

# --- Action Function 2 ---
def on_click2():
    try:
        # Read input values
        v0_text = entryVel2.get().strip()
        angle_text = entryAngle.get().strip()
        range_text = entryRange.get().strip()
        h_text = entryH.get().strip()
        t_text = entryT.get().strip()

        try:
            g_text = entryg2.get().strip()
            if g_text == '':
                g = float(entryg.get())
                entryg2.delete(0, 'end')
                entryg2.insert(0, g)
            else:
                g = float(g_text)
        except ValueError:
            g = float(entryg.get())
            entryg2.delete(0, 'end')
            entryg2.insert(0, g)

        # Convert to floats if provided
        v0 = float(v0_text) if v0_text and v0_text != '--' else None
        angle_deg = float(angle_text) if angle_text and angle_text != '--' else None
        R = float(range_text) if range_text and range_text != '--' else None
        Hmax = float(h_text) if h_text and h_text != '--' else None
        T = float(t_text) if t_text and t_text != '--' else None

        known_count = sum(x is not None for x in [v0, angle_deg, R, Hmax, T])
        if known_count < 2:
            Messagebox.show_info("Please fill at least two known values to calculate the others.", title="Not Enough Data")
            return

        # --- Solve Step by Step ---
        if v0 and angle_deg:
            angle_rad = radians(angle_deg)
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            R = v0x * T
            Hmax = (v0y ** 2) / (2 * g)
        elif R and angle_deg:
            angle_rad = radians(angle_deg)
            v0 = sqrt((R * g) / sin(2 * angle_rad))
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            Hmax = (v0y ** 2) / (2 * g)
        elif R and v0:
            sin2θ = (R * g) / (v0 ** 2)
            if -1 <= sin2θ <= 1:
                angle_rad = 0.5 * asin(sin2θ)
                angle_deg = degrees(angle_rad)
                v0x = v0 * cos(angle_rad)
                v0y = v0 * sin(angle_rad)
                T = (2 * v0y) / g
                Hmax = (v0y ** 2) / (2 * g)
            else:
                Messagebox.show_error("Invalid combination of Range, v₀, and g.", title="Error")
                return
        elif Hmax and angle_deg:
            angle_rad = radians(angle_deg)
            v0 = sqrt((2 * g * Hmax) / (sin(angle_rad) ** 2))
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            R = v0x * T
        elif Hmax and v0:
            sinθ = sqrt((2 * g * Hmax) / (v0 ** 2))
            if -1 <= sinθ <= 1:
                angle_rad = asin(sinθ)
                angle_deg = degrees(angle_rad)
                v0x = v0 * cos(angle_rad)
                v0y = v0 * sin(angle_rad)
                T = (2 * v0y) / g
                R = v0x * T
            else:
                Messagebox.show_error("Invalid combination of Hmax, v₀, and g.", title="Error")
                return
        elif T and v0:
            v0y = (g * T) / 2
            angle_rad = atan(v0y / sqrt(v0 ** 2 - v0y ** 2))
            angle_deg = degrees(angle_rad)
            v0x = v0 * cos(angle_rad)
            R = v0x * T
            Hmax = (v0y ** 2) / (2 * g)
        else:
            Messagebox.show_info("This combination of knowns is not supported yet.", title="Info")
            return

        # --- Update entries ---
        entryVel2.delete(0, END)
        entryVel2.insert(0, f"{v0:.3f}")

        entryAngle.delete(0, END)
        entryAngle.insert(0, f"{angle_deg:.3f}")

        entryRange.delete(0, END)
        entryRange.insert(0, f"{R:.3f}")

        entryH.delete(0, END)
        entryH.insert(0, f"{Hmax:.3f}")

        entryT.delete(0, END)
        entryT.insert(0, f"{T:.3f}")

        # --- Update parabola inputs ---
        entryVel.delete(0, END)
        entryVel.insert(0, f"{v0:.3f}")

        entryg.delete(0, END)
        entryg.insert(0, f"{g:.3f}")

        meterAng.configure(amountused=round(angle_deg))

        # --- Draw Graph ---
        if check_var.get():
            PC.draw_parabola(angle_deg, v0, g)

    except ValueError:
        Messagebox.show_error("Please enter valid numeric values.", title="Input Error")
    except Exception as e:
        Messagebox.show_error(f"Unexpected error: {e}", title="Error")

# --- Reset Values Action ---
def on_click3():
    # --- Update entries ---
        entryVel2.delete(0, END)
        entryVel2.insert(0, "--")

        entryAngle.delete(0, END)
        entryAngle.insert(0, "--")

        entryRange.delete(0, END)
        entryRange.insert(0, "--")

        entryH.delete(0, END)
        entryH.insert(0, "--")

        entryT.delete(0, END)
        entryT.insert(0, "--")

        entryg2.delete(0, END)
        entryg2.insert(0, "9.80665")

        # --- Update parabola inputs ---
        entryVel.delete(0, END)
        entryVel.insert(0, "--")

        entryg.delete(0, END)
        entryg.insert(0, "9.80665")

        meterAng.configure(amountused=45)

# --- Button 2 ---
calcbut = tb.Button(t2, text="Calculate and Draw", bootstyle="success", command=on_click2)
calcbut.grid(row=8, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

# --- Button 3 ---
resetbut = tb.Button(t2, text="Reset Values", bootstyle="warning", command=on_click3)
resetbut.grid(row=9, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

# --- Mainloop ---
app.mainloop()
