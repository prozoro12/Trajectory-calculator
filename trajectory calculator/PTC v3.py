import ttkbootstrap as tb
from math import *
import parabolaCalc as PC
#from parabolaCalc import g
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# --- Setup main window ---
app = tb.Window(themename="solar")
app.title("Projectile Trajectory Calculator")
#app.geometry("500x550")

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

notebook = tb.Notebook(app)
t1 = tb.Frame(notebook)
t2 = tb.Frame(notebook)
t3 = tb.Frame(notebook)
notebook.add(t1, text="Parabola")
notebook.add(t2, text="Values")
notebook.add(t3, text="Numerics")
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

# --- Input: Acceleration due to gravity
entrygL2 = tb.Label(
    t1, text="Acceleration due to gravity (g) (m/s²):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entrygL2.grid(row=3, column=0, sticky='w', padx=10, pady=5)

entryg = tb.Entry(t1, width=25, bootstyle='danger')
entryg.grid(row=3, column=1, sticky='ew', padx=10, pady=5)
entryg.insert(0, '9.80665')

# --- Input: Angle ---
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

# --- Results Labels ---
results_frame = tb.Labelframe(t2, text="Results", bootstyle="secondary")
results_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

lbl_range = tb.Label(results_frame, text="Range (R): -- m", font=("Helvetica", 11))
lbl_range.pack(anchor='w', padx=10, pady=5)

lbl_height = tb.Label(results_frame, text="Max Height (Hmax): -- m", font=("Helvetica", 11))
lbl_height.pack(anchor='w', padx=10, pady=5)

lbl_time = tb.Label(results_frame, text="Time of Flight (T): -- s", font=("Helvetica", 11))
lbl_time.pack(anchor='w', padx=10, pady=5)

# --- Numerics results
entryL2 = tb.Label(
    t3, text="Initial Velocity (v₀) (m/s):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL2.grid(row=2, column=0, sticky='w', padx=10, pady=5)

entryVel2 = tb.Entry(t3, width=25, bootstyle='danger')
entryVel2.grid(row=2, column=1, sticky='ew', padx=10, pady=5)
entryVel2.insert(0, '--')

entryL3 = tb.Label(
    t3, text="Launch Angle (θ) (°):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL3.grid(row=3, column=0, sticky='w', padx=10, pady=5)

entryAngle = tb.Entry(t3, width=25, bootstyle='danger')
entryAngle.grid(row=3, column=1, sticky='ew', padx=10, pady=5)
entryAngle.insert(0, '--')

entryL4 = tb.Label(
    t3, text="Range (R) (m):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL4.grid(row=4, column=0, sticky='w', padx=10, pady=5)

entryRange = tb.Entry(t3, width=25, bootstyle='danger')
entryRange.grid(row=4, column=1, sticky='ew', padx=10, pady=5)
entryRange.insert(0, '--')

entryL5 = tb.Label(
    t3, text="Max Height (Hmax) (m):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL5.grid(row=5, column=0, sticky='w', padx=10, pady=5)

entryH = tb.Entry(t3, width=25, bootstyle='danger')
entryH.grid(row=5, column=1, sticky='ew', padx=10, pady=5)
entryH.insert(0, '--')

entryL6 = tb.Label(
    t3, text="Time of Flight (T) (s):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL6.grid(row=6, column=0, sticky='w', padx=10, pady=5)

entryT = tb.Entry(t3, width=25, bootstyle='danger')
entryT.grid(row=6, column=1, sticky='ew', padx=10, pady=5)
entryT.insert(0, '--')

entryL7 = tb.Label(
    t3, text="Acceleration due to Gravity (g) (m/s²):",
    font=("Helvetica", 12),
    bootstyle="success"
)
entryL7.grid(row=6, column=0, sticky='w', padx=10, pady=5)

entryg2 = tb.Entry(t3, width=25, bootstyle='danger')
entryg2.grid(row=6, column=1, sticky='ew', padx=10, pady=5)
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

        # --- Update Labels ---
        lbl_range.config(text=f"Range (R): {R:.2f} m")
        lbl_height.config(text=f"Max Height (Hmax): {Hmax:.2f} m")
        lbl_time.config(text=f"Time of Flight (T): {T:.2f} s")

        # --- Draw parabola ---
        PC.draw_parabola(angle_deg, v0, g)

        # --- Open Values Tab ---
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
        # Get gravity safely from entryg2 or fallback to entryg
        try:
            g_text = entryg2.get().strip()
            if g_text == '':
                g = float(entryg.get())
                entryg2.delete(0, 'end')
                entryg2.insert(0, g)
            else:
                g = float(g_text)
        except ValueError:
            # If user typed something invalid (like letters), fall back to main g
            g = float(entryg.get())
            entryg2.delete(0, 'end')
            entryg2.insert(0, g)

        
        # Convert to floats if provided, else None
        v0 = float(v0_text) if v0_text and v0_text != '--' else None
        angle_deg = float(angle_text) if angle_text and angle_text != '--' else None
        R = float(range_text) if range_text and range_text != '--' else None
        Hmax = float(h_text) if h_text and h_text != '--' else None
        T = float(t_text) if t_text and t_text != '--' else None

        # --- Start solving ---
        known_count = sum(x is not None for x in [v0, angle_deg, R, Hmax, T])
        if known_count < 2:
            Messagebox.show_info(
                "Please fill at least two known values to calculate the others.",
                title="Not Enough Data"
            )
            return

        # --- Solve Step by Step ---
        # 1 If v0 and angle known
        if v0 and angle_deg:
            angle_rad = radians(angle_deg)
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            R = v0x * T
            Hmax = (v0y ** 2) / (2 * g)

        # 2 If range and angle known
        elif R and angle_deg:
            angle_rad = radians(angle_deg)
            v0 = sqrt((R * g) / sin(2 * angle_rad))
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            Hmax = (v0y ** 2) / (2 * g)

        # 3 If range and v0 known
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

        # 4 If Hmax and angle known
        elif Hmax and angle_deg:
            angle_rad = radians(angle_deg)
            v0 = sqrt((2 * g * Hmax) / (sin(angle_rad) ** 2))
            v0x = v0 * cos(angle_rad)
            v0y = v0 * sin(angle_rad)
            T = (2 * v0y) / g
            R = v0x * T

        # 5 If Hmax and v0 known
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

        # 6 If T and v0 known
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

        # --- Update entry boxes ---
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

        # --- Update "Values" tab too ---
        lbl_range.config(text=f"Range (R): {R:.2f} m")
        lbl_height.config(text=f"Max Height (Hmax): {Hmax:.2f} m")
        lbl_time.config(text=f"Time of Flight (T): {T:.2f} s")

        #notebook.select(t2)

        # --- Draw Graph ---
        PC.draw_parabola(angle_deg, v0, g)

        # --- Update Labels ---
        lbl_range.config(text=f"Range (R): {R:.2f} m")
        lbl_height.config(text=f"Max Height (Hmax): {Hmax:.2f} m")
        lbl_time.config(text=f"Time of Flight (T): {T:.2f} s")

        # --- Update Inputs ---
        entryVel.delete(0, 'end')
        entryVel.insert(0, v0)
        entryg.delete(0, 'end')
        entryg.insert(0, g)
        meterAng.configure(amountused=round(angle_deg))
        
    except ValueError:
        Messagebox.show_error("Please enter valid numeric values.", title="Input Error")
    except Exception as e:
        Messagebox.show_error(f"Unexpected error: {e}", title="Error")


# --- Button 2 ---
calcbut = tb.Button(t3, text="Calculate and Draw", bootstyle="success", command=on_click2)
calcbut.grid(row=7, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

app.mainloop()
