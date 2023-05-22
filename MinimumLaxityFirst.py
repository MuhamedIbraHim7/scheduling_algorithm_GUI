class MinimumLaxityFirst:
    def __init__(self, processes):
        self.processes = processes
    
    def schedule(self):
        # Process the jobs in order of minimum laxity
        current_time = 0
        while self.processes:
            # Calculate the minimum laxity and corresponding process
            min_laxity = float('inf')
            min_laxity_process = None
            for process in self.processes:
                laxity = process.deadline - current_time - process.remaining_time
                if laxity < min_laxity:
                    min_laxity = laxity
                    min_laxity_process = process
            
            # Schedule the process
            min_laxity_process.start_time = current_time
            current_time += min_laxity_process.burst_time
            min_laxity_process.end_time = current_time
            self.processes.remove(min_laxity_process)
        
    def get_gantt(self):
        # Create a Gantt chart
        chart = []
        for process in self.processes:
            chart.append((process.name, process.start_time, process.end_time))
        
        return chart