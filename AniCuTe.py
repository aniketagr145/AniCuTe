from modules.malware_analysis.malware_analysis_runner import SecureTeaMalwareAnalysis
from modules.malware_analysis import globals
from modules.notifs.telegramNotifier import TelegramNotifier

class Runner:
    def __init__(self):
        globals.initialize_colours()
    def runmalware(self):
        mode = input(
            globals.WHITE + """Enter Mode
            c - Persistent mal analysis
            i - Steg Analysis
            m - Malware Analyis
            >>>""" + globals.END)
        fname = input(
            globals.WHITE + """Enter File name - 
            >>>""" + globals.END)
        sscan = input(
            globals.WHITE + """Enter Steg Scan -
            If Steg Analysis Selected enter tool initials-
            >>>""" + globals.END)
        #VT_API_KEY = input(
        #    globals.WHITE + """Enter VirusTotal API KEY - 
        # #    >>>""" + globals.END)
        
        VT_API_KEY = "8c3be18d935b21602ccaecb7224e1dd1dd938058b294520417681e430d962b1c"
        TELEGRAM_TOKEN = ""
        TELEGRAM_UID = ""

        creds = {
            "mode": mode,
            "filename": fname,
            "stegscan": sscan,
            "virustotal_api_key": VT_API_KEY
        }
        
        obj = SecureTeaMalwareAnalysis(creds=creds)
        res = obj.runner()
        if(res):
            print(str(res))
            
            tele = TelegramNotifier()


runner_obj = Runner()
runner_obj.runmalware()