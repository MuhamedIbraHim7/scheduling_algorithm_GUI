class RateMonotonic:
    def __init__(self, processes):
        self.processes = processes
    
    def schedule(self):
        # Sort the processes by period
        self.processes.sort(key=lambda x: x.period)
        
        # Process the jobs in order of priority
        current_time = 0
        for process in self.processes:
            num_instances = process.period // process.deadline
            for i in range(num_instances):
                process.start_time = current_time
                current_time += process.deadline
                process.end_time = current_time
        
    def get_gantt(self):
        # Create a Gantt chart
        chart = []
        for process in self.processes:
            chart.append((process.name, process.start_time, process.end_time))
        
        return chart