#Contains all functions needed to calculate, aggregate and return datas

def GetMonthlySalaryOfEmployee(rate: int, contract_hours: int, worked_hours: int) -> float:
    """
    Return the monthly salary of a single employee. 
    
    [Args]\n
    rate = Hourly rate
    contract_hours = Contractual amount of hours to be worked per week
    worked_hours = Amount of actual hours worked per week
    """
    
    result = 0 #Result to be returned
    overtime_hours = 0 #Amount of overtime. Overtime is paid 1.5x hourly rate
    base_salary = 0 #Amount paid before overtime is calculated.
    isOvertime = worked_hours > contract_hours #If there is overtime to be calculated
    
    if not isOvertime: #No overtime, standard salary is calculated
        result = rate * worked_hours
    else : #Else, calculate salary with overtime hours being paid 1.5x hourly rate
        overtime_hours = worked_hours - contract_hours #Calculte the amount of overtime
        result = (rate * contract_hours) + (overtime_hours * (rate*1.5))
    
    #Return the result multiply by 4 (4 weeks in a month)
    return float(result*4)

def GetAllSalariesOfSubsidiary(sub : list) -> list:
    """ 
    Return a list of all employees' monthly salaries
    
    [Args]
    sub = A list of dictionaries containing all employees' datas.
    """
    result_ = []
    #Loop through all employee (emp) of subsidiary (sub) and append the monthly salary
    for emp in sub:
        result_.append((GetMonthlySalaryOfEmployee(emp["hourly_rate"], emp["contract_hours"], emp["weekly_hours_worked"])))
    
    return result_
    

def PrintAllSalariesOfSubsidiary(sub: list) -> str:
    """
    Return a list of all employee's salaries in a single subsidiary in the following fashion :
    Name : Salary
    
    [Args]\n
    sub = A list containing all the data of subsidiary    
    """
    str_ = "" #String to be returned
    for emp in sub: #For each employee (emp) in the subsidiary (sub), get the name and calculate the monthly salary then display it
        str_ += emp["name"] + " : "
        str_ += str(GetMonthlySalaryOfEmployee(emp["hourly_rate"], emp["contract_hours"], emp["weekly_hours_worked"]))+"\n"
    
    return str_

def AggregateAllSalaries(*args) -> float:
    """ 
    Return the aggregate of all monthly salaries for every subsidiary in args
    
    [Args]\n
    args = any number of list containing dictionaries of employees
    """
    total = 0.0 #String to be returned
    
    #Loop through all subsidiaries (sub) then loop through all employees (emp) of sub.
    #For each emp, get the monthly salary
    for sub in args:
        for emp in sub:
            total += GetMonthlySalaryOfEmployee(emp["hourly_rate"], emp["contract_hours"], emp["weekly_hours_worked"])
    
    return total

def GetCompanyAverageSalary(company: dict) -> float:
    """
    Return the average salary of all employees in company.
    
    [Args]\n
    company = A dictionary containing the datas of all subsidiaries
    """
    #Get the salaries of all employees in all subsidaries then divide by the total of employees.
    return AggregateAllSalaries(*[company[x] for x in company.keys()]) / sum((len(company[x]) for x in company.keys()))

def GetSubsidiaryAverageSalary(sub: list) -> float:
    """
    Return the average salary of all employees in subsidiary
    
    [Args]\n
    sub = A list of dictionaries containing all employees' datas.    
    """
    return sum(GetAllSalariesOfSubsidiary(sub)) / len(sub)

def GetSubsidiaryHighestSalary(sub: list) -> float:
    """
    Return the highest salary in subsidiary (sub).
    """
    
    return max(GetAllSalariesOfSubsidiary(sub))

def GetCompanyHighestSalary(company: dict) -> float:
    """ 
    Return the highest salary in company.
    """
    
    return max([GetSubsidiaryHighestSalary(company[x]) for x in company.keys()])

def GetSubsidiaryLowestSalary(sub: list) -> float:
    """
    Return the lowest salary in subsidiary (sub).
    """
    
    return min(GetAllSalariesOfSubsidiary(sub))

def GetCompanyLowestSalary(company: dict) -> float:
    """ 
    Return the lowest salary in company.
    """
    
    return min([GetSubsidiaryLowestSalary(company[x]) for x in company.keys()])

def GetEmployeeFormatedData(emp: dict) -> str:
    """ 
    Return the relevant data of an employee in the following pattern :
    Name      | Title       | Salaire Mensuelle: Monthly_Salary
    
    [Args]\n
    emp = A dictionary containing all the employee's data
    """
    
    str_ = emp["name"]
    
    #Check if name isn't exceeding character limit. While YES, remove the last character until string fits within limit
    while len(str_) > 12:
        str_ = str_[:-1]
        
    #If name is under the limit, add empty character to normalize display
    while len(str_) < 12:
        str_ += " "
    
    str_ += "| "
    str_ += emp["job"]
    
    #Same logic as for name
    while len(str_) > 30:
        str_ = str_[:-1]
        
    while len(str_) < 30:
        str_ += " "
    
    str_ += "| "
    
    str_ += "Salaire mensuel: " + str(GetMonthlySalaryOfEmployee(emp["hourly_rate"], emp["contract_hours"], emp["weekly_hours_worked"]))
    
    return str_
    
    

    