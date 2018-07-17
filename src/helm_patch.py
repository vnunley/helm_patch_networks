import json
from src.helm_setting import adsr_setting, arp_setting, helm_setting, delay_setting

class helm_patch:
    """Class containing .helm settings"""

    def __init__(self, filename):
        # Open patch file
        self.helmFilename = filename

        with open(self.helmFilename, 'r') as helmFile:
            self.jsonFile = json.loads(helmFile.read())

        print("Version is ", self.jsonFile['synth_version'])

        self.patch_name = self.jsonFile['patch_name']

        self.settings = [
            adsr_setting("amp", 
                self.jsonFile["amp_attack"],
                self.jsonFile["amp_decay"],
                self.jsonFile["amp_sustain"],
                self.jsonFile["amp_release"]
                ),
            arp_setting("arp", 
                self.jsonFile["arp_frequency"],
                self.jsonFile["arp_gate"],
                self.jsonFile["arp_octaves"],
                self.jsonFile["arp_on"],
                self.jsonFile["arp_pattern"],
                self.jsonFile["arp_sync"],
                self.jsonFile["arp_tempo"]
                ),
            helm_setting("beats_per_minute",
                self.jsonFile["beats_per_minute"], .334, 5.0)
        ]
        # Beats per minute: min .334 max 5 
        # Cross modulation: min 0 max 0.5
        # Cutoff: min 28.0 max 127.0

    def get_json(self):
        return self.jsonFile

    def set_json(self, newJsonFile):
        self.jsonFile = newJsonFile

    def load_file(self, filename):
        self.helmFilename = filename
        with open(self.helmFilename, 'r') as helmFile:
            self.jsonFile = json.loads(helmFile.read())

    def save_file(self, filename):
        self.helmFilename = filename
        with open(self.helmFilename, 'w') as helmFile:
            json.dump(self.jsonFile, helmFile)
