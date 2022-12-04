from modules.malware_analysis.malware_analysis_runner import SecureTeaMalwareAnalysis

def main():
    mode = input(
        """Enter Mode
        c - Persistent mal analysis
        i - Steg Analysis
        m - Malware Analyis
        >>>""")
    fname = input(
        """Enter File name - 
        >>>""")
    sscan = input(
        """Enter Steg Scan -
        If Steg Analysis Selected enter tool initials-
        >>>
        """)
    #VT_API_KEY = input(
    #    """Enter VirusTotal API KEY - 
    #    >>>""")
    
    VT_API_KEY = "8c3be18d935b21602ccaecb7224e1dd1dd938058b294520417681e430d962b1c"

    creds = {
        "mode": mode,
        "filename": fname,
        "stegscan": sscan,
        "virustotal_api_key": VT_API_KEY
    }
    
    obj = SecureTeaMalwareAnalysis(creds=creds)
    obj.runner()

main()