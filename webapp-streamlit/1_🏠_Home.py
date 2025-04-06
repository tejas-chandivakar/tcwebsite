import streamlit as st
import pathlib

st.set_page_config(
    page_title="TC Website",
    page_icon="🌺",
    layout="wide"
)


st.title("Main Page")
st.divider()
st.sidebar.success("Select a page above.")

st.button("Click Me!", key="green")
st.button("Click", key="blue")



reg_script = r'''
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open]
"MuiVerb"="@photoviewer.dll,-3043"

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\command]
@="\"%SystemRoot%\\System32\\rundll32.exe\" \"%ProgramFiles%\\Windows Photo Viewer\\PhotoViewer.dll\", ImageView_Fullscreen %1"

[HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\DropTarget]
"Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

[HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap]
"ImageOptionFlags"=dword:00000001
"NeverDefault"=""
"DefaultIcon"="%SystemRoot%\\System32\\imageres.dll,-72"

[HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\shell\open]
"MuiVerb"="@photoviewer.dll,-3043"

[HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\shell\open\command]
@="\"%SystemRoot%\\System32\\rundll32.exe\" \"%ProgramFiles%\\Windows Photo Viewer\\PhotoViewer.dll\", ImageView_Fullscreen %1"

[HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\shell\open\DropTarget]
"Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"
'''

st.code(reg_script, language='ini')  # or language='text'





# Function to Load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

# Load the external CSS
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)
