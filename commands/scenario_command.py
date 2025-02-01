class ScenarioCommand:
    def __init__(self, text):
        self.original_text = text.strip()
        self.is_valid = False
        self.scenario_name = None
        
        parts = self.original_text.split()
        if len(parts) == 2 and parts[0] == "SCENARIO":
            self.is_valid = True
            self.scenario_name = parts[1].lower()
            
    def execute(self):
        if not self.is_valid:
            return "ERROR: Invalid command format. Use: SCENARIO <name>"
            
        try:
            module = __import__(f'scenarios.{self.scenario_name}', fromlist=[None])
            scenario_class = getattr(module, self.scenario_name.capitalize())
            scenario_instance = scenario_class()
            scenario_instance.run()
            return f"OK: Executed {self.scenario_name}"
        except Exception as e:
            return f"ERROR: {str(e)}"