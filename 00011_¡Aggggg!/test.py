class Test(unittest.TestCase):

  def test_proporcion_cines_comeriales_provinciales_es_un_DataFrame(self):
    self.assertEquals(type(proporcion_cines_comeriales_provinciales), pd.DataFrame)