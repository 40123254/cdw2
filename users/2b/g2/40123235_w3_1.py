result = []
with open("./../../../2016_cd_2a_2.txt", 'r') as f:
    content = f.readlines()
    #print(content)
    #print(len(content))
    # 逐 element 處理
    for i in range(len(content)):
        for line in content[i].splitlines():
            #print(content[i].splitlines())
            result.append(list(line.split(",")))
            
            g.es(result)
            
            
   "'         [['40323101', '40323102', '40323103', '40323108', '40323124', '', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', ''], ['40323110', '40323113', '40323116', '40323121', '40323151', '', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', ''], ['40323110', '40323113', '40323116', '40323121', '40323151', '', ''], ['40323112', '40323133', '40323147', '40323152', '40323155', '40323156', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', ''], ['40323110', '40323113', '40323116', '40323121', '40323151', '', ''], ['40323112', '40323133', '40323147', '40323152', '40323155', '40323156', ''], ['40323105', '40323106', '40323107', '40323146', '40223153', '40023139', '']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', ''], ['40323110', '40323113', '40323116', '40323121', '40323151', '', ''], ['40323112', '40323133', '40323147', '40323152', '40323155', '40323156', ''], ['40323105', '40323106', '40323107', '40323146', '40223153', '40023139', ''], ['40123119', '40123141', '40123149', '40123216', '40123227', '40123255', '40023234']]
[['40323101', '40323102', '40323103', '40323108', '40323124', '', ''], ['40323109', '40323130', '40323135', '40323136', '40323138', '40323144', ''], ['40323111', '40323117', '40323118', '40323119', '40323120', '40323122', ''], ['40323110', '40323113', '40323116', '40323121', '40323151', '', ''], ['40323112', '40323133', '40323147', '40323152', '40323155', '40323156', ''], ['40323105', '40323106', '40323107', '40323146', '40223153', '40023139', ''], ['40123119', '40123141', '40123149', '40123216', '40123227', '40123255', '40023234'], ['40323125', '40323126', '40323132', '40323149', '40323150', '40323153', '']]
 '4'], ['40323125', '40323126', '40323132', '40323149', '40323150', '40323153', ''], ['40323123', '40323131', '40323137', '40323143', '40323145', '40323154', ''], ['40323127', '40323128', '40323139', '40323141', '', '', '']]  "'