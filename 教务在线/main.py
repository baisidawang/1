dit = {}
for i in range(1,10):
    print(f'/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[4]')
    print(f'/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[12]')
    key_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[4]").text
    value_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[12]").text
    dit[key_j] = value_j
print(dit)