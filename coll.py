class Salary:
    def __init__(self,basic_sal):
        self.basic_sal = basic_sal

    def cal_salary(self):
        return self.basic_sal
    
class Deductions:
    def __init__(self,insu,pf):
        self.insu = insu
        self.pf = pf

    def total_ded(self):
        total_ded = self.insu + self.pf
        return total_ded
    
class Tax:
    def __init__(self,tax_rate):
        self.tax_rate = tax_rate

    def cal_tax(self,taxable_inc):
        tax_amt = taxable_inc * self.tax_rate
        return tax_amt
    
class Employee(Salary,Deductions,Tax):
    def __init__(self,basic_sal,insu,pf,tax_rate):
        Salary.__init__(self,basic_sal)
        Deductions.__init__(self,insu,pf)
        Tax.__init__(self,tax_rate)

    def cal_net_sal(self):
            taxable_inc = self.cal_salary() - self.total_ded() 
            net_sal = taxable_inc - self.cal_tax(taxable_inc)
            return net_sal
        

emp1 = Employee(100,10,10,.10)
net_sal = emp1.cal_net_sal()
print('Net sal is: ', net_sal)