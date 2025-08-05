{{ define "main" }}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trivy Scan Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2em; background: #f8f8f8; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 2em; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #eee; }
        tr:nth-child(even) { background: #f2f2f2; }
        .severity-CRITICAL { color: #b71c1c; font-weight: bold; }
        .severity-HIGH { color: #e65100; font-weight: bold; }
        .severity-MEDIUM { color: #fbc02d; font-weight: bold; }
        .severity-LOW { color: #388e3c; font-weight: bold; }
        .severity-UNKNOWN { color: #757575; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Trivy Security Scan Report</h1>
    {{ range . }}
    <h2>{{ .Target }}</h2>
    <table>
        <thead>
            <tr>
                <th>Vulnerability ID</th>
                <th>Pkg Name</th>
                <th>Installed Version</th>
                <th>Fixed Version</th>
                <th>Severity</th>
                <th>Title</th>
                <th>References</th>
            </tr>
        </thead>
        <tbody>
            {{ range .Vulnerabilities }}
            <tr>
                <td>{{ .VulnerabilityID }}</td>
                <td>{{ .PkgName }}</td>
                <td>{{ .InstalledVersion }}</td>
                <td>{{ .FixedVersion }}</td>
                <td class="severity-{{ .Severity }}">{{ .Severity }}</td>
                <td>{{ .Title }}</td>
                <td>
                    {{ range .References }}
                        <a href="{{ . }}" target="_blank">Link</a><br>
                    {{ end }}
                </td>
            </tr>
            {{ end }}
        </tbody>
    </table>
    {{ end }}
</body>
</html>
{{ end }}
