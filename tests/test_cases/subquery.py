query = """SELECT abc
             FROM xyz
            WHERE def IN
                  (SELECT hij
                     FROM ijk)"""
query = """SELECT abc
             FROM xyz
            WHERE def IN
          (SELECT hij
             FROM ijk)"""  # Q448

query = """SELECT abc
             FROM xyz
            WHERE def = 'def';
SELECT hij
  FROM ijk"""