# Mettler Toledo Scale Reader

This is a simple script that reads from a connected Mettler Toledo device and writes the weight to an output csv file.

This only works on Windows for now.

## How To Use

First create a virtual env and activate it:

```
# This will create the virtual env in a 
# folder called env in the current directory
python3 -m venv env

# Activate the virtual env for current shell
env\Scripts\activate
```

Run the script:

```
python mtscale.py
```

You can also run this to see available options:

```
python mtscale.py --help
```

## Import In Excel and Refresh Data Automatically

1. From a blank work select "From Text" in the "Get External Data" section of the Data tab.
2. Use the Text Import Wizard to set how your csv file will be imported.
3. After you select Finish to exit the Import Wizard, a dialog box titled Import Text will come up.
4. Select the Properties button on this dialog box.
5. An External Data Range Properties box will come up.
6. In the Refresh Control section of the box, you should uncheck the "Prompt for file name on refresh" selection, set the frequency of refresh in minutes, and make sure there will be a refresh when you open the workbook.
7. You can return to the Properties box anytime by either right-clicking on the imported data in the worksheet or selecting "Connections" from the Data tab.
