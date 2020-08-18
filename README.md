# AWS-Selenium-Scraper

It took me forever to get a headless version of chrome running on AWS. Here's my solution.


A few things:

	The packages and files include are intended to be used in an AWS Lambda Function to run selenium for websraping

	The lambda_function.py file contains code to classify some LTL shipping carriers based on their tracking number
	The lambda_function.py file can be edited to your desire
	
	
###  NOTE - this zip file contains linux files that windows and mac systems cannot properly re-zip. If you wish to edit, be sure you you are using a Linux system or subsystem to zip the package.

This can be accomplished in subsystems command line by using the following command: 


	zip -r lambda_function.zip *


This will zip all files into the current directory under the name lambda_function.zip


# SET UP: #

	Upload lambda_function.zip as a deployment package
	Upload deploy.zip as a deployment layer
	



# Current Implementation of lambda_function.py #

This function is intended to be used for post requests.

Query Params for post request:

	{
		"tracking": "##########",
		"carrier": "CARRIER_NAME"
	}

If the tracking number matches the carrier, the return body will contain a string with the carrier url
Otherwise, the return body will contain "false"

Supported "carrier" variables:

	'N&M Transfer'
	'R&L Carriers'
	'FedEx'    - Also supports Canada Economy (C.E. is run by FedEx)
	'Panama Transfer'
	'ABF Freight'


Unsupported "carrier" variables that can be implemented:

	'CH Robinson'  - Removed for time being but can be added back by uncommenting and changing function dictionary (Line 161)

