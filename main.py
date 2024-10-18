import json_handler
import display_data
import export_data

#Import all of the company data in a single dictionary from Json file
CompanyData = json_handler.GetEmployeesDictionary()
     
#Display in the console all the relevant datas in a nice formatting           
display_data.PrintCompanyDatas(CompanyData)

#Write a csv file with all relevant datas.
export_data.WriteCSV(CompanyData)


    
