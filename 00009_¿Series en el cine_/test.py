class Test(unittest.TestCase):

  def test_pantallas_por_sector_es_un_series(self):
    self.assertEquals(type(butacas_por_provincia), pd.DataFrame)
    
  def test_genera_el_series_correcto(self):
    self.assertEquals(butacas_por_provincia.to_dict(), [
         {'province': 'Buenos Aires', 'seats': 5180},
         {'province': 'Ciudad Autónoma de Buenos Aires', 'seats': 306},
         {'province': 'Salta', 'seats': 354},
         {'province': 'San Juan', 'seats': 1071},
         {'province': 'Santa Fe', 'seats': 584}])