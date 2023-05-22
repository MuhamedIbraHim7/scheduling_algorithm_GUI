class DeadlineMonotonic:
    def __init__(self, processes):
        self.processes = processes
    
    def schedule(self):
        # Sort the processes by deadline
        self.processes.sort(key=lambda x: x.deadline)
        
        # Process the jobs in order of earliest deadline
        current_time = 0
        for process in self.processes:
            process.start_time = current_time
            current_time += process.burst_time
            process.end_time = current_time
        
    def get_gantt(self):
        # Create a Gantt chart
        chart = []
        for process in self.processes:
            chart.append((process.name, process.start_time, process.end_time))
        
        return chart