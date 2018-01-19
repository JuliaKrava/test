class Employee:
    def __init__(self,  full_name='', position=None, zp=0, N=0):
        self.full_name = full_name.split()[0].strip() + '\n' + full_name.split()[-1].strip()
        self.position = position
        self.zp = zp*N

class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []
        self.experience = 0

    def add_skills(self, new_skills):
        self.skills.append(new_skills)

    def find_experience(self):
        if self.experience <=2:
            result = str('Invalid value')
        elif self.experience < 3:
            result = str('Junior')
        elif 3 <= self.experience <= 6:
            result = str('Middle')
        else:
            result = str('Senior')
        return result

a=ITEmployee('Юля Кравчук', 'Middle', 100500, 12)
a.experience=6
a1=a.find_experience()
a.add_skills(['QATest', 'AutoTests'])
a.add_skills('Python')
print(a.full_name, a.zp, a1, a.skills, sep='\n')
