class RoundRobin:
    def __init__(self, processes, time_slice):
        self.processes = processes
        self.time_slice = time_slice
    
    def schedule(self):
        # Initialize variables
        current_time = 0
        queue = list(self.processes)
        completed = []
        
        # Process the queue
        while queue:
            process = queue.pop(0)
            process.start_time = current_time
            
            # Process the job for a time slice
            for i in range(self.time_slice):
                if process.remaining_time > 0:
                    current_time += 1
                    process.remaining_time -= 1
                
                # Check for process completion
                if process.remaining_time == 0:
                    process.end_time = current_time
                    completed.append(process)
                    break
            
            # Put the process back in the queue if it's not finished
            if process.remaining_time > 0:
                queue.append(process)
        
        # Update the overall process list with the completed processes
        for process in completed:
            index = self.processes.index(process)
            self.processes[index] = process
        
    def get_gantt(self):
        # Create a Gantt chart
        chart = []
        for process in self.processes:
            chart.append((process.name, process.start_time, process.end_time))
        
        return chart