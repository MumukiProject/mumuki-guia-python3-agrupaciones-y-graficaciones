class Test(unittest.TestCase):

  def test_pantallas_por_sector_es_un_series(self):
    self.assertEquals(type(butacas_por_localidad), pd.DataFrame)
    
  def test_genera_el_series_correcto(self):
    self.assertEquals(provincias_con_cines_grandes.to_dict(), {
        'Santa Fe': 584.0, 'Buenos Aires': 1036.0, 'San Juan': 1071.0
    })