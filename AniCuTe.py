from modules.malware_analysis.malware_analysis_runner import MalwareAnalysisRunner
from modules.malware_analysis import globals
from modules.notifs.telegramNotifier import TelegramNotifier

class Runner:
    def __init__(self):
        globals.initialize_colours()
    def runmalware(self):

        mode = input(
            globals.WHITE + """Enter Mode
            c - Persistent Malware Analysis
            m - Single File Malware Analyis
            >>>""" + globals.END)

        if mode == 'm': 
            fname = input(
                globals.WHITE + """Enter File name - 
                >>>""" + globals.END)
        else:
            fname = None


        #VT_API_KEY = input(
        #    globals.WHITE + """Enter VirusTotal API KEY - 
        #    >>>""" + globals.END)
        
        # Enter your VIRUSTOTAL API KEY
        VT_API_KEY = "8c3be18d935b21602ccaecb7224e1dd1dd938058b294520417681e430d962b1c"

        creds = {
            "mode": mode,
            "filename": fname,
            "virustotal_api_key": VT_API_KEY,
        }
        
        obj = MalwareAnalysisRunner(creds=creds)
        res = obj.runner()


runner_obj = Runner()
runner_obj.runmalware()