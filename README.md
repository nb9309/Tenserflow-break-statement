# Tenserflow-break-statement

1. break statement
			==============================================
=>break is a key word
=>break keyword must be used always inside of loops otherwise we get Syntax error
=>The purpose of break statement is that "To terminate the execution of loop logically when certain condition is satisfied  and  PVM control comes of corresponding loop and executes other statements in the program".
=>when break statement takes place inside for loop or while loop then PVM will not execute corresponding else block(bcoz loop is not becoming False)  but it executes other statements in the program.
=>Syntax1:
-------------------
			for varname  in Iterable_object:
			       ------------------------------
			       if (test cond):
			              break
			------------------------------
			------------------------------
------------------
=>Syntax2:
-------------------
			while(Test Cond-1):
			       ------------------------------
			       if (test cond-2):
			              break
