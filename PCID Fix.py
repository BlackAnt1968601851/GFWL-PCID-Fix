"""
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import os
import subprocess
import pyperclip

status = 0
data = [
    ("90,c8,9a,8a,f6,57,a9,f7", "FXRHK-T8PDY-FHBCH-G6YJG-XF8PJ"),
    ("23,b3,bd,92,12,6b,c5,fc", "WBV4B-MFGR4-Y9XY7-MKRPM-HHJ96"),
    ("f3,42,a3,bb,c2,43,96,3c", "M2RHB-TDC2R-MTHXH-GP662-XG33W"),
    ("ec,9f,31,39,87,50,96,62", "WMBGX-HC2WR-JC92D-KVK2B-Q8YB3"),
    ("92,1e,37,df,f4,52,dd,01", "W6Y9P-MKP4C-FHT83-GQMMC-FYQQQ"),
    ("53,48,b4,94,11,01,d5,98", "JX3JC-CC2HX-TRWCY-49BKF-2CKYY"),
    ("eb,5f,76,a9,5d,87,d9,8d", "XH3CX-7D382-4TWG7-D9YT9-FFJMJ"),
    ("ec,78,57,e2,44,57,f2,91", "V7HM9-K3YBQ-K3XVF-4K6JF-RXXHG"),
    ("2b,2c,e1,af,16,ea,97,42", "DCKXY-JG4DH-JRDYB-KMT97-GPKPG"),
    ("d8,bf,b3,fd,49,11,9f,a7", "QGTD9-VM883-83FPP-KYKD2-FK3JD"),
    ("39,49,34,34,30,c0,7b,97", "MVKG6-8BPRK-93FPR-GTH9Y-GQJWT"),
    ("94,52,8c,e7,c8,e0,bc,80", "P72WF-GXDQM-8YTP4-7TYYB-72YGT"),
    ("1c,53,6d,92,2d,ef,26,76", "JY6GC-GD69H-G4TC2-BF9MJ-FW9YJ"),
    ("91,26,c1,de,83,b8,f8,f5", "Q38PK-B9WCR-8D8WP-C8Y28-9DW73"),
    ("f7,b0,2f,e2,18,ed,05,e8", "GXTHG-JCQMJ-WVBCP-MDVPV-JBX43"),
    ("7e,1a,c9,0c,6d,aa,4f,b1", "RHQV3-7G3FM-9T4CD-F9H8B-FT66Q"),
    ("ab,49,55,39,77,46,1d,90", "CMBMJ-CG3PC-R2HY8-6RYGG-CRWTY"),
    ("d9,bd,df,b7,aa,f9,b3,fd", "CPTJV-PYQRR-VY79Y-7PMM6-DWBF3"),
    ("40,f1,a1,5e,11,39,83,f2", "22TBG-D3PF4-YPMDJ-MMJ8Q-9Y68G"),
    ("ad,28,cc,13,2c,e2,b3,61", "CTJG4-V3MQY-3K272-6MHCV-R4GG6"),
    ("e3,c3,e6,3d,94,87,26,2e", "V3K6V-QTKQD-RDWCJ-X3WM2-G8XP8"),
    ("f8,37,19,46,ce,45,44,45", "DPQ7P-646DC-DM63Q-X4YD3-MPBMB"),
    ("24,59,1c,b5,37,2e,65,fe", "CHYXY-QYRXP-WR22C-8B47X-DGF93"),
    ("71,40,3a,3b,ad,26,98,5d", "RRQ6J-B2G7T-GMW8M-Q7QYX-3VJVQ"),
    ("d0,9e,87,b9,41,95,85,f5", "FYGQP-F7GQP-X6CX6-BFYVK-WQBBG"),
    ("86,0c,7e,9b,a5,08,5a,31", "HJKY7-6TQD6-6FPXT-DG9J3-K7YQD"),
    ("df,fa,68,3e,ed,ab,07,3b", "VY43Y-JYC9Q-84T4P-M22G8-WVBR6"),
    ("b6,37,7a,64,a9,f7,36,a3", "BYMGW-K33C2-WDDDD-VQ98P-DJC4M"),
    ("8c,b1,87,93,cd,fa,91,85", "G8FFP-FRBT6-DCKT9-HRMMX-XCMBJ"),
    ("84,a4,aa,7e,36,8a,45,b3", "DW9FC-B2DFG-TQB9Y-P3YKC-V8P7Y"),
    ("f6,01,85,6f,40,1e,26,61", "VDQBM-TYB29-QTRG6-WY7VB-YRD7J"),
    ("8a,c8,1d,58,52,bb,e6,88", "W8D7H-F2RBK-PRHCG-PRTQW-CHPDB")
    # Add the rest of the PC IDs and keys here
]

def generate_key():
    global status
    status = 1
    global key
    pcid, key = random.choice(data)

    pcid_label['text'] = f"PCID: {pcid}"
    key_label['text'] = f"Key: {key}"

    # Modify the registry key
    registry_modification = f"""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\SOFTWARE\Microsoft\XLive]
"PCID"=hex(b):{pcid}"""

    with open('reg.reg', 'w') as file:
        file.write(registry_modification)

    subprocess.call(['reg', 'import', 'reg.reg'])

    os.remove('reg.reg')
    
    ZPEdited = 0
    if os.path.exists("ZolikaPatch.ini"):
        with open("ZolikaPatch.ini", "r") as f:
            lines = f.readlines()

        with open("ZolikaPatch.temp", "w") as f:
            for line in lines:
                if "=" in line:
                    key, value = line.strip().split("=")
                    if key != "FixPCIDKickbug":
                        if value == "":
                            f.write(key + "\n")
                        else:
                            f.write(key + "=" + value + "\n")
                    else:
                        f.write(key + "=0\n")
                else:
                    f.write(line)  # Write the line as it is if it doesn't contain "="

        os.remove("ZolikaPatch.ini")
        os.rename("ZolikaPatch.temp", "ZolikaPatch.ini")
        ZPEdited = 1


root = Tk()
root.geometry("308x70")
root.minsize(308, 70)
root.maxsize(308, 70)
root.title("GFWL PCID Fix")

def clipboard1():
 if status==0:
  messagebox.showerror(title="Error", message="Error: Key has not been generated")
 if status==1:
  pyperclip.copy(key)

pcid_label = ttk.Label(root, text="PCID: Not Generated")
key_label = ttk.Label(root, text="Key: Not Generated")
generate_button = ttk.Button(root, text="Generate PCID", command=generate_key)
Clipboard = ttk.Button(root, text="Copy Text", command=clipboard1)

pcid_label.pack()
key_label.pack()
generate_button.place(x=64, y=40, width=90)
Clipboard.place(x=154, y=40, width=90)
root.mainloop()
"""
This code is Signed by BlackAnt.
-----BEGIN PGP SIGNATURE-----

iHUEARYKAB0WIQRLzsvY7ikTLf8p0YVplhagI3npXQUCZKlbJAAKCRBplhagI3np
XQU1AP0asCdzHs29AQ+FpytiaH9OlO1FxJUWjETqHHYpVameSwD/eUMfEteyCrpA
n0GAZp4RY2U5RBkhqvGD7HKFvwvUnA4=
=/Isb
-----END PGP SIGNATURE-----
"""