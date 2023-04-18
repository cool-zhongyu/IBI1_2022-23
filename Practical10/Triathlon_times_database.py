class triathlobn(object):
    def __init__(self,first_name,last_name,location,swim_time,cycle_time,run_time,total_time):
        self.a=first_name
        self.b=last_name
        self.c=location
        self.d=swim_time
        self.e=cycle_time
        self.f=run_time
        self.g=total_time
    def det(self):
        print(self.a,self.b,self.c,self.d,self.e,self.f,self.g)
t=triathlobn('Lebron','Jordan','Los-Angles','1','2','3','6')
t.det()
