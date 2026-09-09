from abc import ABC,abstractmethod       # Abstract base class = ABC

class Car(ABC):

    @abstractmethod
    def start(self):pass

    @abstractmethod
    def accelerate(self):pass

    @abstractmethod
    def stop(self):pass

class Baleno(Car):

    def start(self):

        print("baleno is starting......")

    def accelerate(self):

        print("baleno is accelerating......")

    def stop(self):

        print("baleno is stoping......")

Baleno_instance = Baleno()
Baleno_instance.start()
Baleno_instance.stop()
Baleno_instance.accelerate()