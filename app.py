from flask import Flask, request, render_template
import pandas as pd
import socket
import os
import re

app = Flask(__name__)

# Path to the Excel file in the same directory
EXCEL_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.xlsx")

def split_input(input_data):
    # Split input by commas, newlines, or spaces
    return [item.strip() for item in re.split(r'[,\s\n]+', input_data) if item.strip()]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    names = []

    # Read names from the Excel file
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
        if "Name" in df.columns:
            names = df["Name"].drop_duplicates().tolist()
    except Exception as e:
        error = f"Error reading the file: {e}"

    if request.method == 'POST':
        if 'resolve_dns' in request.form:
            # DNS to IP
            input_data = request.form['input_data']
            input_list = split_input(input_data)
            ip_set = set()
            for domain in input_list:
                try:
                    ip = socket.gethostbyname(domain)
                    ip_set.add(ip)
                except socket.gaierror:
                    error = f"Could not resolve: {domain}"
            result = ", ".join(ip_set)

        elif 'resolve_ip' in request.form:
            # IP to DNS
            input_data = request.form['input_data']
            input_list = split_input(input_data)
            dns_set = set()
            for ip in input_list:
                try:
                    dns = socket.gethostbyaddr(ip)[0]
                    dns_set.add(dns)
                except socket.herror:
                    error = f"Could not resolve: {ip}"
            result = ", ".join(dns_set)

        elif 'fetch_ips' in request.form:
            # Fetch IPs from Excel
            name_to_search = request.form['name_to_search']
            try:
                df = pd.read_excel(EXCEL_FILE_PATH)
                if "Name" not in df.columns or "IP" not in df.columns:
                    error = "The Excel file must contain 'Name' and 'IP' columns!"
                else:
                    filtered_rows = df[df["Name"] == name_to_search]
                    unique_ips = filtered_rows["IP"].drop_duplicates()
                    result = ", ".join(unique_ips)
            except Exception as e:
                error = f"Error reading the file: {e}"

        elif 'find_duplicates' in request.form:
            # Find duplicate IPs
            input_data = request.form['input_data']
            input_list = split_input(input_data)
            ip_count = {}
            for ip in input_list:
                ip_count[ip] = ip_count.get(ip, 0) + 1
            duplicates = [ip for ip, count in ip_count.items() if count > 1]
            result = ", ".join(duplicates)

    return render_template('index.html', result=result, error=error, names=names)

if __name__ == '__main__':
    app.run(debug=True)
