 P,R,T=10000,5,3
 SI=(P*R*T)/100
 print("Simple Interest: ",SI)
 P,R,T=10000,5,3
 CI=P*((1+R/100)**T)-P
 print("Compound Interest: ",round(CI,2))