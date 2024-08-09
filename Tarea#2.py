def MyFunc2():
 print("2 :",a)
 def SubFun1(st): # Function is Locally defined
    print("Local Function with ",st)
 SubFun1("Local Call")
MyFunc1()
MyFunc2()
SubFun1("Global Call") 