#Contains

import accounting

newline = "\n"
separator = "=============================================="

def PrintCompanyDatas(company: dict) -> None:
    """
    Print all relevant datas of company, including breakdowns of all subsidiaries.
    
    [Args]\n
    company = A dictionary containing all subsidiaries' datas where values = a list of dictionaries    
    """
    print("$$$ ------------------------------------ $$$")
    print(newline, newline)
    print("Entreprise : My Imaginary Company(ltd)")
    print(newline)
    print(separator)
    print(newline)
    print("Statistiques globales des salaires pour l'entreprise My Imaginary Company(ltd) : ")
    print(f"Salaire moyen :  {accounting.GetCompanyAverageSalary(company):0.2f}")
    print(f"Salaire le plus élevé :  {accounting.GetCompanyHighestSalary(company)}")
    print(f"Salaire le plus bas :  {accounting.GetCompanyLowestSalary(company)}")
    print(newline)
    print(separator)
    
    for sub in company.keys():
        PrintSubsidiaryDatas(sub, company[sub])
    
    print(newline, newline)
    print("$$$ ---------- END OF RAPPORT ---------- $$$")
    
def PrintSubsidiaryDatas(name: str, sub: list) -> None:
    """ 
    Print the all the relevant data of subsidiary
    
    [Args]\n
    name = Name of the subsidiary
    sub = A list of dictionaries containing all employee datas
    """
    print(newline)
    print(f"Entreprise : {name}")
    print(newline)
    
    #Sort the subsidiary from highest salary to lowest salary    
    sub.sort(reverse = True, key = lambda x: accounting.GetMonthlySalaryOfEmployee(x["hourly_rate"], x["contract_hours"], x["weekly_hours_worked"]))
        
    for emp in sub:
        print(accounting.GetEmployeeFormatedData(emp))
    
    print(newline)
    print(separator)
    print(newline)
    print(f"Statistiques globales des salaires pour l'entreprise {name} : ")
    print(f"Salaire moyen :  {accounting.GetSubsidiaryAverageSalary(sub):0.2f}")
    print(f"Salaire le plus élevé :  {accounting.GetSubsidiaryHighestSalary(sub)}")
    print(f"Salaire le plus bas :  {accounting.GetSubsidiaryLowestSalary(sub)}")
    print(newline)
    print(separator)