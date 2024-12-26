<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qualys Scan Launcher</title>
</head>
<body>
    <h1>Launch a Qualys Scan</h1>
    <form id="scanForm">
        <label for="ip">IP Address:</label>
        <input type="text" id="ip" name="ip" required>
        <br><br>
        <label for="scanTitle">Scan Title:</label>
        <input type="text" id="scanTitle" name="scanTitle" required>
        <br><br>
        <button type="submit">Launch Scan</button>
    </form>

    <script>
        document.getElementById('scanForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent form from refreshing the page
            
            const ip = document.getElementById('ip').value;
            const scanTitle = document.getElementById('scanTitle').value;

            const url = "https://qualysapi.qualys.com/api/2.0/fo/scan/";
            const username = "username";
            const password = "password";
            
            const data = `action=launch&scan_title=${encodeURIComponent(scanTitle)}&ip=${encodeURIComponent(ip)}&option_id=123&iscanner_name=scanner`;

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        "X-requested-With": "curl",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic " + btoa(`${username}:${password}`)
                    },
                    body: data
                });

                if (response.ok) {
                    const result = await response.text();
                    alert("Scan Launched Successfully: " + result);
                } else {
                    alert("Error launching scan: " + response.statusText);
                }
            } catch (error) {
                console.error("Error:", error);
                alert("An error occurred while launching the scan.");
            }
        });
    </script>
</body>
</html>
