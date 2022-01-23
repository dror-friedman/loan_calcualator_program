from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(bg = "light grey")

        Label (window, font = 'Cagliari 12 bold', bg = "light grey", text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
        Label (window, font = 'Cagliari 12 bold', bg = "light grey", text = "Duration of Payments").grid(row = 2, column = 1, sticky = W)
        Label (window, font = 'Cagliari 12 bold', bg = "light grey", text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
        Label (window, font = 'Cagliari 12 bold', bg = "light grey", text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
        Label (window, font = 'Cagliari 12 bold', bg = "light grey", text = "Total Payment").grid(row = 5, column = 1, sticky = W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)
        self.durationVar = StringVar()
        Entry(window, textvariable = self.durationVar, justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = 'Cagliari 12 bold', bg = "light grey", textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font = 'Cagliari 12 bold', bg = "light grey", textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)

        btCalculatePayment = Button(window, text = "Calculate", font = 'Cagliari 15 bold', bg = "green", fg = "light grey",  command = self.calculatePayment).grid(row = 6, column = 2, sticky = E)
        btClear = Button(window, text = "Clear", font = 'Cagliari 15 bold', bg = "red", fg = "light grey",  command = self.delete_all).grid(row = 6, column = 8, padx = 25, pady = 25, sticky = E)

        window.mainloop()

    def calculatePayment(self):
        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.durationVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) *12 \
        *int(self.durationVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, duration):
        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1+monthlyInterestRate)**(duration*12))
        return monthlyPayment;

    def delete_all(self):
                self.annualInterestRateVar.set("")
                self.durationVar.set("")
                self.loanAmountVar.set("")
                self.monthlyPaymentVar.set("")
                self.totalPaymentVar.set("")

LoanCalculator()
