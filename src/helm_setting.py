import random

class helm_setting:
    """Representation of a setting in helm's patch file"""

    def __init__(self, name, value, minimum, maximum):
        self.name = name
        self.value = value
        self.min = minimum
        self.max = maximum

    def set_random(self):
        self.value = random.uniform(self.min, self.max)

class adsr_setting(helm_setting):
    """Inhereted setting for envelopes"""

    def __init__(self, name, a, d, s, r):
        self.name = name

        self.value = [
            helm_setting(name + '_attack', a, 0.0, 16.0),
            helm_setting(name + '_decay', d, 0.0, 16.0),
            helm_setting(name + '_release', s, 0.0, 1.0),
            helm_setting(name + '_sustain', r, 0.0, 16.0)]
    
    def set_random(self):
        for x in self.value:
            x.set_random()

class arp_setting(helm_setting):
    """Inhereted settings for arpeggiator"""

    def __init__(self, name, freq, gate, octives, on, pattern, sync, tempo):
        self.name = name
        
        self.value = [
            helm_setting("arp_frequency", freq, 0.63, 2.0), 
            helm_setting("arp_gate", gate, 0.0, 1.0),
            helm_setting("arp_octives", octives, 1, 4),
            helm_setting("arp_on", on, 0, 1),
            helm_setting("arp_pattern", pattern, 0, 4),
            helm_setting("arp_sync", sync, 0, 1),
            helm_setting("arp_tempo", tempo, 0, 11)]

    def set_random(self):
        for x in self.value:
            x.set_random()

class delay_setting(helm_setting):
    """Inhereted settings for delay"""

    def __init__(self, name, dry_wet, feedback, frequency, on, sync, tempo):
        self.name = name
        
        self.value = [
            helm_setting("delay_dry_wet", dry_wet, 0.0, 1.0),
            helm_setting("delay_feedback", feedback, 0.0, 1.0),
            helm_setting("delay_frequency", frequency, -2.0, 5.0),
            helm_setting("delay_on", on, 0, 1),
            helm_setting("delay_sync", sync, 0, 1),
            helm_setting("delay_tempo", tempo, 0.0, 11)
        ]