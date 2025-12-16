import glob

# List your data files here
files = ["incident.dat", "transmited.dat", "absorbed.dat", "LiF/optical_EXC.dat", "LiF/optical_Im.dat", "LiF/optical_exp_Im.dat", "MgO/optical_EXC.dat", "MgO/optical_Im.dat", "MgO/optical_exp_Im.dat", "CaO/optical_EXC.dat", "CaO/optical_Im.dat", "CaO/optical_exp_Im.dat", "ZnO/optical_EXC_xy.dat", "ZnO/optical_Im_xy.dat", "ZnO/optical_exp_Im_xy.dat", "ZnO/optical_EXC_z.dat", "ZnO/optical_Im_z.dat", "ZnO/optical_exp_Im_z.dat", "LiF/optical_Re.dat", "LiF/optical_exp_Re.dat", "MgO/optical_Re.dat", "MgO/optical_exp_Re.dat", "CaO/optical_Re.dat", "CaO/optical_exp_Re.dat", "ZnO/optical_Re_xy.dat", "ZnO/optical_exp_Re_xy.dat", "ZnO/optical_Re_z.dat", "ZnO/optical_exp_Re_z.dat", "LiF/XANES_Li_K_EXC.dat", "LiF/XANES_Li_K_Im.dat", "LiF/XANES_Li_K_exp1.dat", "LiF/XANES_Li_K_exp2.dat", "LiF/XANES_F_K_EXC.dat", "LiF/XANES_F_K_Im.dat", "LiF/XANES_F_K_exp1.dat", "MgO/XANES_Mg_L23_EXC.dat", "MgO/XANES_Mg_L23_Im.dat", "MgO/XANES_Mg_L23_exp1.dat", "MgO/XANES_Mg_L23_exp2.dat", "MgO/XANES_O_K_EXC.dat", "MgO/XANES_O_K_Im.dat", "MgO/XANES_O_K_exp1.dat", "MgO/XANES_O_K_exp2.dat", "MgO/XANES_Mg_K_EXC.dat", "MgO/XANES_Mg_K_Im.dat", "MgO/XANES_Mg_K_exp1.dat", "MgO/XANES_Mg_K_exp2.dat", "MgO/XANES_Mg_K_exp3.dat", "CaO/XANES_Ca_L23_EXC.dat", "CaO/XANES_Ca_L23_Im.dat", "CaO/XANES_Ca_L23_exp1.dat", "CaO/XANES_O_K_EXC.dat", "CaO/XANES_O_K_Im.dat", "CaO/XANES_O_K_exp1.dat", "CaO/XANES_O_K_exp2.dat", "CaO/XANES_Ca_K_EXC.dat", "CaO/XANES_Ca_K_Im.dat", "CaO/XANES_Ca_K_exp1.dat", "ZnO/XANES_O_K_EXC_xy.dat", "ZnO/XANES_O_K_Im_xy.dat", "ZnO/XANES_O_K_exp1.dat", "ZnO/XANES_O_K_exp2.dat", "ZnO/XANES_O_K_EXC_z.dat", "ZnO/XANES_O_K_Im_z.dat", "ZnO/XANES_O_K_exp1.dat", "ZnO/XANES_O_K_exp2.dat", "ZnO/XANES_Zn_L23_EXC_xy.dat", "ZnO/XANES_Zn_L23_Im_xy.dat", "ZnO/XANES_Zn_L23_exp1.dat", "ZnO/XANES_Zn_L23_EXC_z.dat", "ZnO/XANES_Zn_L23_Im_z.dat", "ZnO/XANES_Zn_L23_exp1.dat", "ZnO/XANES_Zn_K_EXC_xy.dat", "ZnO/XANES_Zn_K_Im_xy.dat", "ZnO/XANES_Zn_K_exp1.dat", "ZnO/XANES_Zn_K_EXC_z.dat", "ZnO/XANES_Zn_K_Im_z.dat", "ZnO/XANES_Zn_K_exp1.dat"]

output_js_file = "presentation_data.js"

print(f"Generating {output_js_file}...")

with open(output_js_file, "w") as outfile:
    # Optional: Write a comment at the top of the JS file
    outfile.write("// Auto-generated data file for Graduate Presentation\n\n")

    for filename in files:
        try:
            x_vals = []
            y_vals = []

            # Read the .dat file
            with open(filename, 'r') as f:
                for line in f:
                    # Skip comments and empty lines
                    if line.strip() and not line.strip().startswith('#'):
                        cols = line.split()
                        try:
                            # Assuming 1st column is X, 2nd is Y
                            x_vals.append(float(cols[0]))
                            y_vals.append(float(cols[1]))
                        except (ValueError, IndexError):
                            continue

            # Create a variable name based on the filename (e.g., incident_data)
            var_name = filename.split('.')[0] + "_data"

            # Write valid JavaScript directly to the file
            outfile.write(f"// --- Data for {filename} ---\n")
            outfile.write(f"const {var_name} = {{\n")
            outfile.write(f"    x: {x_vals},\n")
            outfile.write(f"    y: {y_vals}\n")
            outfile.write(f"}};\n\n")

            print(f" -> Wrote {len(x_vals)} points for {filename}")

        except FileNotFoundError:
            print(f" -> Error: Could not find {filename} (Skipping)")

print("Done! You can now link 'presentation_data.js' in your HTML.")