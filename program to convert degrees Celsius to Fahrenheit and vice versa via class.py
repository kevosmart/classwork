class Temperature:
    def __init__(self, Celcius, Farenheit):
        self.Celcius = Celcius
        self.Farenheit = Farenheit
    def convert_Celcius(self):
        return (self.Celcius*(9/5) + 32)
    def convert_Farenheit(self):
        return(((self.Farenheit-32)*5)/9)
stud= Temperature(80,20)
print(stud.convert_Celcius())
print(stud.convert_Farenheit())
