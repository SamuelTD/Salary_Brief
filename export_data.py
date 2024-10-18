import csv
import accounting


def GetCSVFormatting(company: dict, stats: bool) -> list:
    """
    Return a list formatted for CSV filing.
    
    [Args]\n
    company = Dictionary containing all the datas of the company
    stats = if True return the global salary datas else return the employees datas
    """
    result_ = [] #Result to be returned
    
    #Return the global salary datas
    if stats:
        result_.append({"company name": "", "average salary": "", "highest salary": "", "lowest salary": ""})
        for sub in company.keys():
            result_.append({"company name": sub, "average salary": accounting.GetSubsidiaryAverageSalary(company[sub]),\
                "highest salary": accounting.GetSubsidiaryHighestSalary(company[sub]), "lowest salary": accounting.GetSubsidiaryLowestSalary(company[sub])})
    
    #Else return the employees' salaries datas   
    else:
        result_.append({"name": "", "monthly salary": ""})
        for sub in company.keys():
            for emp in company[sub]:
                result_.append({"name": emp["name"], "monthly salary": accounting.GetMonthlySalaryOfEmployee(emp["hourly_rate"], emp["contract_hours"],\
                    emp["weekly_hours_worked"]) })
         
    return result_
    
def WriteCSV(company: dict) -> None:
        """
        Write a CSV file containing global salary datas and employees' salaries datas from company.
        
        [Args]\n
        company = Dictionary containing all the company's datas.        
        """
                
        with open("company_data.csv", "w", newline="") as cvsfile:            
            
            #First write the global datas
            Fieldnames = ["company name", "average salary", "highest salary", "lowest salary"]  
            writer = csv.DictWriter(cvsfile, fieldnames=Fieldnames)            
            writer.writeheader()
            writer.writerows(GetCSVFormatting(company, True))
            
            #Add an empty entry to separate datasets
            writer = csv.writer(cvsfile)
            writer.writerow("")
            
            #Write the employees' datas
            Fieldnames = ["name", "monthly salary"]  
            writer = csv.DictWriter(cvsfile, fieldnames=Fieldnames)            
            writer.writeheader()
            writer.writerows(GetCSVFormatting(company, False))                             
       
    