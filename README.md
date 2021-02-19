# fileorder
The purpose of the script is to sort files in a directory. The files can be image or video from smartphone and it works with file naming standart yyyymmdd_hhmmss.
When files are in a empty directory without any other files or directories, the script is makin a list from filenames, then from this list is making another list with elemnts consisting of the first four characters of the filename - this would be the year. this year list is checked for duplicates and they are removed. for every element of the list it creates directory with the name of the element. then checks if the first four characters of the element of the file list is equal to the name of the directory and if it is, moves the file into this directory. next the script have to check the files within the directory for characters at month position in the filename and creates list of months which will be checked for duplicates and then creates list of subdirectories named after the elements of the month list. finally checks the filenames if characters in the month position are equal to the name of the subdirectory and moves the file into that subdirectory.
as output we have a directory with subdirectories named with years which contain another one or more subdirectories named with month which at the end contains files with filenames whithin a certain month.

dictionary( year )
every element of year contains dictionary of month
every element of month contains structure with source file and desitionaion file name


//pass 1
for every file in the file_list
year = get_file_name_year;
add file_name to years list
years = dictionary(years_list);

//pass2
for every file in the file_list
get year of file
get month of file
years [ year ].lists.add( month);

for every year in years
years[year] = dictionary ( years[year] ); //convert list to dictionary

//pass 3
for every  file in the list
year_file = get year of file
month_file = get month of file
destination_file_name = year_of_file/month_of_file/file_name

years[year_file][month_file].add( file, destination_filename);



//iterate over 
years[year_file][month_file]
and copy
