from nasapy import Nasa
key="TJ0EVVNFCbMpoNkvtus5tcKaeGEpffq6b53DgBc9"
nasa=Nasa(key=key)

date='2021-05-20'
data=nasa.mars_rover(earth_date=date)
print(data)
