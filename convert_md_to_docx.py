import sys
import re
import subprocess
import os

if len(sys.argv) != 3:
    print("Usage: python3 convert_md_to_docx.py <input.md> <output.docx>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
temp_html = "temp_" + os.path.basename(input_file) + ".html"

html = ["<html><body>"]
in_table = False
first_row = True

with open(input_file, "r") as f:
    for line in f:
        line = line.rstrip('\n')
        stripped = line.strip()
        
        # Check for table block
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                html.append("<table border='1' style='border-collapse: collapse; width: 100%; margin-bottom: 15px;'>")
                in_table = True
                first_row = True
            
            # Skip separator line
            if re.match(r'^\|[\s:-|]+$', stripped):
                continue
                
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            html.append("<tr>")
            for cell in cells:
                cell = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell)
                cell = re.sub(r'\*(.*?)\*', r'<i>\1</i>', cell)
                if first_row:
                    html.append(f"<th style='padding: 8px; background-color: #f2f2f2; text-align: left;'>{cell}</th>")
                else:
                    html.append(f"<td style='padding: 8px;'>{cell}</td>")
            html.append("</tr>")
            first_row = False
            continue
        else:
            if in_table:
                html.append("</table>")
                in_table = False

        if not stripped:
            html.append("<br>")
            continue
            
        if stripped.startswith("# "):
            html.append(f"<h1>{stripped[2:]}</h1>")
        elif stripped.startswith("## "):
            html.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("### "):
            html.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("#### "):
            html.append(f"<h4>{stripped[5:]}</h4>")
        elif line.startswith("* "):
            content = stripped[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)
            content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', content)
            html.append(f"<ul><li style='margin-left: 20px;'>{content}</li></ul>")
        elif line.startswith("    * "):
            content = stripped[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)
            content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', content)
            html.append(f"<ul><li style='margin-left: 60px;'>{content}</li></ul>")
        elif stripped == "---":
            html.append("<hr>")
        else:
            p_text = stripped
            p_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', p_text)
            p_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', p_text)
            html.append(f"<p>{p_text}</p>")

if in_table:
    html.append("</table>")

html.append("</body></html>")

with open(temp_html, "w") as f:
    f.write("\n".join(html))

# Run textutil
subprocess.run(["textutil", "-convert", "docx", "-output", output_file, temp_html], check=True)
os.remove(temp_html)
print(f"Successfully converted {input_file} to {output_file}")

