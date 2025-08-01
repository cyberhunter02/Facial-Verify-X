import os
import stat

print("\n🚀 Launching Facial Verify X...\n")

# Automatically find the current directory of startup.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set your main app filename here (must be in same folder)
main_file = "Facial_Verify_X.py"
app_path = os.path.join(current_dir, main_file)

# Step 1: Check if file exists
if not os.path.exists(app_path):
    print(f"❌ Error: Cannot find {main_file} at {app_path}")
    print("📌 Make sure the file exists and is in the same folder as startup.py")
    exit()

# Step 2: Ensure proper permissions (read & execute for user)
st = os.stat(app_path)
os.chmod(app_path, st.st_mode | stat.S_IREAD | stat.S_IEXEC)

# Step 3: Launch the Streamlit App
os.system(f"python3 -m streamlit run \"{app_path}\"")
