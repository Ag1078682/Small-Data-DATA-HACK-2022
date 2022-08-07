from src.log.log import log
from src.source.get_data import get_data
from src.target.upload import write_data


log("Launch application")
data = get_data()
print(data)
result = write_data(data,"csv")
print("Готово!")


