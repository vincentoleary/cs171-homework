###############################################
#####  Vincent O'Leary (vjo25)            #####
#####  Assignment 1 for CS 171-064        #####
#####  Student Loan Calculator            #####
###############################################

###############################################
#####  Variables                          #####
#####  ppl = PRINCIPLE                    #####
#####  inr = INTEREST RATE                #####
#####  yrs = YEARS                        #####
#####  mpt = MONTHLY PAYMENT              #####
#####  pol = TOTAL PAID ON LOAN           #####
#####  iol = TOTAL INTEREST ON LOAN       #####
#####  afp = ADDITIONAL FEES PAID         #####
#####  tot = TOTAL COSTS OVER PRINCIPLE   #####
###############################################

# Print welcome statement
print("Welcome to the Student Loan Calculator")

# Ask for the PRINCIPLE
print("Enter the amount of the loan in dollars with (no commas):")
ppl = float(input())

# Ask for the length of loan in YEARS
print("Enter the number of years the loan will be for:")
yrs = float(input())

# Calculate a Subsidized Federal Direct Loan
# INTEREST RATE = 3.4
# Fee rate = 1.051
inr = 0.034
fee = 0.01051

# Calculate the MONTHLY PAYMENT
mpt = (ppl*inr)/(12*(1-(1+(inr/12))**(-yrs*12)))

# Calculate the TOTAL PAID ON LOAN by multiplying the MONTHLY PAYMENT by the length of the loan
pol = mpt*12*yrs

# Calculate the interest paid by subtracting the PRINCIPLE from the TOTAL PAID ON LOAN
iol = pol-ppl

# Calculate the fees paid by multiplying the PRINCIPLE by the fee rate
afp = ppl*fee

# Finally, calculate the TOTAL COSTS OVER PRINCIPLE by adding the fees and interest paid
tot = afp+iol

# Print results for Subsidized Federal Direct Loan
print("\nSubsidized Federal Direct Loan")
print("Principle: $",round(int(ppl),2),sep="")
print("Interest Rate: ",round(inr*100,2),"%",sep="")
print("Years: ",round(int(yrs),0),sep="")
print("Monthly Payment: $",round(mpt,2),sep="")
print("Total Paid on Loan: $",round(pol,2),sep="")
print("Total Interest Paid: $",round(iol,2),sep="")
print("Additional Fees Paid: $",round(afp,2),sep="")
print("Total Costs Over Principle: $",round(tot,2),sep="")

# Calculate an Unsubsidized Federal Direct Loan
# INTEREST RATE = 6.8
# Fee rate = 1.051
inr = 0.068
fee = 0.01051

# First calculate a new PRINCIPLE by adding the interest accrued during school
ppll = ppl*(1+(inr*4.25))

# Calculate the MONTHLY PAYMENT
mpt = (ppll*inr)/(12*(1-(1+(inr/12))**(-yrs*12)))

# Calculate the TOTAL PAID ON LOAN by multiplying the MONTHLY PAYMENT by the length of the loan
pol = mpt*12*yrs

# Calculate the interest paid by subtracting the PRINCIPLE from the TOTAL PAID ON LOAN
iol = pol-ppl

# Calculate the fees paid by multiplying the PRINCIPLE by the fee rate
afp = ppl*fee

# Finally, calculate the TOTAL COSTS OVER PRINCIPLE by adding the fees and interest paid
tot = afp+iol

# Print results for Unsubsidized Federal Direct Loan
print("\nUnsubsidized Federal Direct Loan")
print("Principle: $",round(int(ppl),2),sep="")
print("Interest Rate: ",round(inr*100,2),"%",sep="")
print("Years: ",round(int(yrs),0),sep="")
print("Monthly Payment: $",round(mpt,2),sep="")
print("Total Paid on Loan: $",round(pol,2),sep="")
print("Total Interest Paid: $",round(iol,2),sep="")
print("Additional Fees Paid: $",round(afp,2),sep="")
print("Total Costs Over Principle: $",round(tot,2),sep="")

# Calculate an Unsubsidized PLUS Loan
# INTEREST RATE = 7.9
# Fee rate = 4.204
inr = 0.079
fee = 0.04204

# First calculate a new PRINCIPLE by adding the interest accrued during school
pplll = ppl*(1+(inr*4.25))

# Calculate the MONTHLY PAYMENT
mpt = (pplll*inr)/(12*(1-(1+(inr/12))**(-yrs*12)))

# Calculate the TOTAL PAID ON LOAN by multiplying the MONTHLY PAYMENT by the length of the loan
pol = mpt*12*yrs

# Calculate the interest paid by subtracting the PRINCIPLE from the TOTAL PAID ON LOAN
iol = pol-ppl

# Calculate the fees paid by multiplying the PRINCIPLE by the fee rate
afp = ppl*fee

# Finally, calculate the TOTAL COSTS OVER PRINCIPLE by adding the fees and interest paid
tot = afp+iol

# Print results for Unsubsidized PLUS Loan
print("\nUnsubsidized PLUS Loan")
print("Principle: $",round(int(ppl),2),sep="")
print("Interest Rate: ",round(inr*100,2),"%",sep="")
print("Years: ",round(int(yrs),0),sep="")
print("Monthly Payment: $",round(mpt,2),sep="")
print("Total Paid on Loan: $",round(pol,2),sep="")
print("Total Interest Paid: $",round(iol,2),sep="")
print("Additional Fees Paid: $",round(afp,2),sep="")
print("Total Costs Over Principle: $",round(tot,2),sep="")
