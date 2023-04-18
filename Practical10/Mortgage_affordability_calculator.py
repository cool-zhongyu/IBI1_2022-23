def mort_cal(value,salary):
    val=value/5
    if val<=salary:
        return 'Yes'
    else:
        return 'No'
print(mort_cal(18000,3500))
