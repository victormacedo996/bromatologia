# Food Analytics

### Table-of-content
1. [Description](#Description)
    1. [Wheat Flour](#Wheat-Flour)
    1. [Honey](#Honey)
    1. [Meet and Meet products](#Meet-and-meet-products)
    1. [Milk](#Milk)
    1. [Sucrose](#Sucrose)
    1. [Water](#Water)
1. [Instalation](#Instalation)
1. [Usage](#Usage)
1. [Contribute](#Contributing)
1. [Credits](#Credits)
1. [License](#License)

### Description
This is a piece of software to help food scientists in their everyday lab routine.
At this point the program can calculate:
#### Wheat-Flour:
* Fixed Mineral Waste percentage in dry sample
* Acidity in mg of KOH in 100g of sample
* Protein using Kjedahl method in percentage in 100g of dry sample

[Back to the top](#Table-of-content)

#### Honey:
* Inverted sugar percentage in 100g of honey
* Sucrose percentage in 100g of honey
* Acidity in miliequivalent per kilogram of honey
* Formol Index per kilogram of honey

[Back to the top](#Table-of-content)

#### Meet-and-meet-products:
* Fat percentage

[Back to the top](#Table-of-content)

#### Milk:
* Lactose percentage
* Acidity in Dornic degrees and percentage of latic acid
* Fat percentage
* Total soluble solids using the Fleishmann formula
* Non fat solids percentage

[Back to the top](#Table-of-content)

#### Sucrose:
* Sucrose pecentage using polarimetry
* ICUMSA colour
* Sucrose percentage using Fehling's method

[Back to the top](#Table-of-content)

#### Water:
* Alcalinity in mg of CaCO3 per liter of water. And the alcalinity from hidroxyde, carbonate and bicarbonate
* Water hardness in mg of CaCO3 per liter of water
* Total soluble solids per liter of water
* Residual chlorine in grams per liter of water
* Chloride in mg per liter of water
* Oxigen consumed in mg per liter of water

[Back to the top](#Table-of-content)

### Instalation
You will need:
* [Python 3.x](https://www.python.org/downloads/)
* [Scipy library](https://pypi.org/project/scipy/)

[Back to the top](#Table-of-content)

### Usage
After installing Python and the SciPy library just download this souce code and execute the `Main.py` file.

When you execute the `Main.py` file a `Terminal` or `CMD` will pop up presenting the program main menu:

![MainMenu](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/MainMenu.png)



In the main menu you need to type the food you want to analyse and press enter, for this quick tutorial we are gonna select the water analysis. After pressing `4` and hitted `Enter` the program will display the water menu for us:

![WaterMenu](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/WaterMenu.png)

In this menu we just need to choose what analisys we want, for this exemple we will choose the chloride analisys, just pressing `5` and them `Enter`. After this the program will ask us for some data we collect in the lab:

* AgNO3 molarity:

![AgNO3Molarity](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/AgNO3Molarity.png)

* AgNO3 correction factor:

![AgNO3CorrectionFactor](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/AgNO3CorrectionFactor.png)

* Sample volume (in ml):

![SampleVolume](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/SampleVolume.png)

* Volume of AgNO3 spent in every sample. We need at least 3 samples and a maximum of 10. In this example we are gonna input only 3 datas:

![AgNO3Spent](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/AgNO3Spent.png)

After the input of the data we are displayed the Dixon's test menu to choose the confidence interval of the test. For this example we are gonna use the 90% confidence interval pressing `1` and them `Enter`:

![DixonTestMenu](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/DixonTestMenu.png)

When we inputed the Dixon's confidence interval the Dixon's test is applied to the data we inputed and if there is any outlier it will be removed. And then we are presented the mean of our analisys and the standard deviation. At the same page we input the confidence interval to perform the Student's T test.

In this example we are gonna use the confidence interval of 95%, as the instructions tell us we need to enter `0.95` to get the 95% interval and then press `Enter`. Then we enter our comparable wich is the value we are gonna compare to the results from our sample and press `Enter`.

![FinalOutput](https://github.com/victormacedo996/food-analytics/blob/main/Images/Tutorial/FinalOutput.png)

This is the final output of the program it tells us the P-value and the T-statistic of the Student's T test and the message `Reject H0` wich means that we reject the hypotesis that our water has too much chloride. Now we can press any key to bring us back to the main menu to perform another analisys or to exit the program.

[Back to the top](#Table-of-content)

### Contributing

There are a lot of ways to contribute with the project:
* Use the program and report bug
* Suggest new calculation methods and/or foods
* [For programmers](path_to_another_.md)

### Credits

Authors:
1. [Victor Macedo (Author)](https://github.com/victormacedo996/)
    * [Curriculum](http://lattes.cnpq.br/0770800475582252)

[Back to the top](#Table-of-content)

### License
The license intend to allow users and developers to share the software with or without the souce code, use for comercial, private and academic use and change the source code. 

* But it cannot be monetized or marketed and if it is used in any kind of academic work it has to be cited.

* The author and contributors doesn't have any responsibility in the use of the software and give no warranty.

[Check the full license](https://github.com/victormacedo996/food-analytics/blob/main/LICENSE)

[Back to the top](#Table-of-content)

### References
[Adolfo Lutz Analysis Standards (Pt-BR)](https://wp.ufpel.edu.br/nutricaobromatologia/files/2013/07/NormasADOLFOLUTZ.pdf)

[Back to the top](#Table-of-content)
