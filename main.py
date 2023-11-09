class Worker():
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Application():
    def __init__(self, workers):
        self.workers = workers
        
    def getWorkers(self, condition):
        workers = []
        for worker in self.workers:
            if any(str(value).lower().find(condition.lower()) != -1 for value in vars(worker).values()):
                workers.append(worker)
        return ["BAD RESULT"]