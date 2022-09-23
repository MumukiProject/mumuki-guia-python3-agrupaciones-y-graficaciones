class Test(unittest.TestCase):

  def test_pantallas_por_sector_es_un_series(self):
    self.assertEquals(type(pantallas_por_sector), pd.Series)
    
  def test_genera_el_series_correcto(self):
    self.assertEquals(pantallas_por_sector.to_dict(), {
       'Privado comercial': 29,
       'Privado independiente': 1,
       'Público municipal': 2,
       'Público provincial': 1})